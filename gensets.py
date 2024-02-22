#!/usr/bin/env python
###################################################################
#
# This small program is intended to generate blocks of "file sets"
# or "orders" which can then be read into PscchoPy (or anything)
# The notion of the "blocks" is that they act as a modular group
# which can itself be re-used to get as many sitings of each
# item as is desired
#
# The main ideas:
# An ITEM is an individual "thing" that will be in the list
# A CATEGORY is a grouping of items that share some property
# An ORDER is a specific instance of a LIST of ITEMS
# A BLOCK is a SET of ORDERS which makes the following guarantees:
#
#
# * No CATEGORY will appear more than `MAX_SEQUENTIAL` times in a row
# * No ITEM will be seen less than `MIN_SEEN` times in the BLOCK
# * Each ORDER will contain exactly `ITEMS_PER_CAT` ITEMS per CATEGORY
#
# A note about `MIN_SEEN` and `MAX_SEQUENTIAL`
# Both of these are intended to introduce variability in the "environment"
# of an item: `MAX_SEQUENTIAL` reduces "strings" of a particular category
# in cases where that might influence the response. `MIN_SEEN` applies
# *across* ORDERS to ensure that, e.g. a particular item isn't only ever
# seen as the 5th item in the ORDER following some other specific ITEM.
#
# Playing with those two values should be a good way to ensure whatever
# amount of "randomness" is desired. In the extreme case of not wanting to
# re-use any ORDERS you could set `MIN_SEEN` to be the TOTAL number of ratings
# you want each item to have for the entire experiment (rather than getting
# that total by re-using the blocks)
#
# Finally there are some constants intended to ensure that generation 
# will terminate (possibly in failure). Those are commented where they appaer
import argparse
import os
import pprint
import random
import sys

# how many times will we show a single category in a row
MAX_SEQUENTIAL = 2

# for the generated set of blocks, what's the minimum
# number of times to see an item. Another way to think of
# this is the minimum number of "variations" that
# a single item appears in so you don't get too much
# polarization
MIN_SEEN = 5

# how much wiggle room do we have an "equal"
MAX_SEEN_RANGE = 3

# This must be <= to the smallest category set
DEFAULT_ITEMS_PER_CAT = 15

## Some "sanity" variables
# How many times will we try to grab the "next"
# item that matches our contraints before giving up
MAX_ATTEMPTS = 10

# What's the most number of total blocks we'll generate
# before giving up
MAX_BLOCKS = 150

# Assuming retries, etc what is the most number of total
# iterations we're willing to make
MAX_RUNS = MAX_BLOCKS * 10

# list of the filenames (indexes really)
# this is where we read in the input data
# alternatively can just use indexes here and
# process any set of data through it with the indexes

parser = argparse.ArgumentParser(
    prog = "gensets.py",
    description = "Generate file orderings meeting statistical requirements",
)

# parser.add_argument('outdirectory')
parser.add_argument('-i', '--indir')
parser.add_argument('-v', '--verbose',action='store_true')
parser.add_argument('-t', '--testmode', action='store_true')
parser.add_argument('-n', '--items-per-cat', type=int, dest='itemspercat', default=DEFAULT_ITEMS_PER_CAT)

args = parser.parse_args()
args.indir = 'sourcelists'
args.outdirectory = 'fileorders'
args.testmode = False
args.verbose = False
args.itemspercat = 8

# Write each order as <destdir>/Orders<num>.csv
def write_orders(filelists, destdir):
    if os.path.exists(destdir) and len(os.listdir(destdir)) > 0:
        print("ERROR: %s already exists, please rename or all entries in it" % (destdir, ))
        sys.exit(1)
    
    if not os.path.exists(destdir):
        os.makedirs(destdir)
        
    for (order, files) in enumerate(filelists):
        filename = "Order{:03d}.csv".format(order + 1)
        print("Writing to %s" % (os.path.join(destdir, filename), ))
        with open(os.path.join(destdir, filename), 'w') as f:
            # this just matches the originals
            f.write('movie_filename\n')
            for line in files:
                f.write(line + '\n')

print("Reading category files from %s" % (args.indir,))
print("Order files will be written to %s" % (args.outdirectory, ))

category_files = []

if args.testmode:
    category_files = [
        ['cat1_' + str(x) for x in range(0, 61)],
        ['cat2_' + str(x) for x in range(0, 61)],
        ['cat3_' + str(x) for x in range(0,61)],
    ]
else:
    for filename in os.listdir(args.indir):
        if not filename.endswith('.txt'):
            continue
        with open(args.indir + '/' + filename, 'r') as f:
            cat_files = [line.strip() for line in f.readlines() if len(line) > 1]
            if len(cat_files) < args.itemspercat:
                print("ERROR: %s only has %d entries, need at least %d" % (
                        filename,
                        len(cat_files),
                        args.itemspercat,
                    )
                )
                sys.exit(1)
            category_files.append(cat_files)

print("Successfully read in %d category lists" % (len(category_files), ))

# counter for each entry of the list
seen_count = [ [0] * len(files) for files in category_files ];

total_len = args.itemspercat * len(category_files)

# our final output
orders = []

# Now we are going to keep generating sequences until
# each file has approximately equal viewing count

cat_indexes = [ list(range(len(files))) for files in category_files ]

for i in range(len(cat_indexes)):
    random.shuffle(cat_indexes[i])

# we guarantee that we don't get duplicates
# within a block by pre-shuffling and
# walking that. We re-shuffle a category
# when we get to the end of it
cat_index = [0] * len(category_files)

#print("INDEXES:")
#print(cat_indexes)
run = 0
block = 1
success = False

print("""
Beginning generation using the following parameters:
\tMaximum category repeats (MAX_SEQUENTIAL): %d
\tMinimum item instances (MIN_SEEN): %d
\tCategory instances per order (ITEMS_PER_CAT): %d
""" % (MAX_SEQUENTIAL, MIN_SEEN, args.itemspercat))
while block <= MAX_BLOCKS and run < MAX_RUNS:

    run += 1
    print("## Generating block %s" % (block,))
    
    # what was our most recent category
    last_cat = -1
    
    # how many times has it been seen already
    dupe_count = 0
    
    used_per_cat = [0] * len(category_files)
    
    this_order = []
    
    completed = True
    
    state = {
        'cat_index': cat_index.copy(),
        'cat_indexes': [
            idx.copy() for idx in cat_indexes
        ],
        'seen_count' : [
            idx.copy() for idx in seen_count
        ]
    };
    
    # Attempt to generate an order
    while len(this_order) < total_len:
        
        cat = random.randrange(0, len(category_files))
        
        attempts = 0
        
        while (
            attempts <= MAX_ATTEMPTS and
            (
                (cat == last_cat and dupe_count >= MAX_SEQUENTIAL)
                or used_per_cat[cat] >= args.itemspercat
            )
            ):
            
            attempts += 1
            cat = random.randrange(0, len(category_files))
        
        if attempts >= MAX_ATTEMPTS:
            #print("ERROR: Unable to properly identify a new value %d %d" % (dupe_count, used_per_cat[cat]))
            break
            
        if cat == last_cat:
            dupe_count += 1
        else:
            dupe_count = 1
            last_cat = cat
            
        used_per_cat[cat] += 1
        
        # do the business
        # so, we'd want to use random.choice, but since
        # we are tracking statistics, we grab index instead
        element = cat_indexes[cat][cat_index[cat]]
        cat_index[cat] += 1
    
        if cat_index[cat] >= len(cat_indexes[cat]):
            random.shuffle(cat_indexes[cat])
            cat_index[cat] = 0

        
        this_order.append(category_files[cat][element]);
        
        #this_order.append(random.choice(category_files[cat]))
    
        # add to our measurements to see how w're doing
        seen_count[cat][element] += 1
    
    # its possible we weren't able to generate an order
    if len(this_order) < total_len:
        #print("\tResetting state")
        # reset state so we can try again
        cat_indexes = state['cat_indexes']
        cat_index = state['cat_index']
        seen_count = state['seen_count']
        continue
    
    block += 1
    orders.append(this_order)
    
    # check our stats
    # ideally we'd use a cool flatten, but not that important
    min_seen = block
    max_seen = 0
    
    for i in range(len(seen_count)):
        min_seen = min(min_seen, min(seen_count[i]))
        max_seen = max(max_seen, max(seen_count[i]))
        
    #print("%d - %d" % (min_seen, max_seen))
    # are we good?
    if min_seen < MIN_SEEN:
        continue
    
    if max_seen - min_seen <= MAX_SEEN_RANGE:
        print("## Done! %d - %d" % (min_seen, max_seen))
        success = True
        break
    else:
        print("MIN: %d MAX: %d" % (min_seen, max_seen))
if success:
    #pprint.pprint(orders)
    write_orders(orders, args.outdirectory)
else:
    print("ERROR: Unable to resolve the given constraints")
