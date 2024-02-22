#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on February 03, 2024, at 10:33
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'PEACEskeleton'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'fileset': '',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s_%s' % (expInfo['participant'], expName, expInfo['fileset'], expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\rache\\Desktop\\UNLV\\Thesis\\PsychoPy Tests\\PEACEskeleton.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1280, 720], fullscr=True, screen=0,
            winType='pyglet', allowStencil=True,
            monitor='testMonitor', color='black', colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = 'black'
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='event')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='Pyglet')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "break_2" ---
    begin = visual.TextStim(win=win, name='begin',
        text="Press the 'space bar' to begin the video",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    startresp2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Videos" ---
    varietyvideos = visual.MovieStim(
        win, name='varietyvideos',
        filename=None, movieLib='ffpyplayer',
        loop=False, volume=1.0, noAudio=False,
        pos=(0, 0), size=(2,1), units=win.units,
        ori=0.0, anchor='center',opacity=None, contrast=1.0,
        depth=0
    )
    
    # --- Initialize components for Routine "instructionsreaction2" ---
    reactioninstructions = visual.TextStim(win=win, name='reactioninstructions',
        text="Now you will be asked to rate how the video made you feel.\n\nYou will be shown four different rating scales.\n\nFor each scale, click on the image that best represehnts how you felt.\n\nClicking will move you on to the next scale.\n\nPress the 'space bar' to continue.",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    startresp3 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "affect" ---
    affectrating = visual.ImageStim(
        win=win,
        name='affectrating', units='norm', 
        image='AAPE Images for PsychoPy/Photoshop/Affect.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.5, .75),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    mouseaffect = event.Mouse(win=win)
    x, y = [None, None]
    mouseaffect.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "anxiety" ---
    image = visual.ImageStim(
        win=win,
        name='image', units='norm', 
        image='AAPE Images for PsychoPy/Photoshop/Anxiety.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.5, .75),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    mouseanxiety = event.Mouse(win=win)
    x, y = [None, None]
    mouseanxiety.mouseClock = core.Clock()
    slider = visual.Slider(win=win, name='slider',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=win.units,
        labels=None, ticks=(1, 2, 3, 4, 5), granularity=0.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-2, readOnly=False)
    
    # --- Initialize components for Routine "energy" ---
    energyimage = visual.ImageStim(
        win=win,
        name='energyimage', units='norm', 
        image='AAPE Images for PsychoPy/Photoshop/Energy.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.5, .75),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    mouseenergy = event.Mouse(win=win)
    x, y = [None, None]
    mouseenergy.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "pride" ---
    imagepride = visual.ImageStim(
        win=win,
        name='imagepride', 
        image='AAPE Images for PsychoPy/Photoshop/Pride.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.25, .35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    mousepride = event.Mouse(win=win)
    x, y = [None, None]
    mousepride.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "typeinstructions" ---
    text = visual.TextStim(win=win, name='text',
        text='Now, you will explain how the video made you feel.\n\nPlease try to find one word that suits your emotion.\n\nAfter you type in your word, hit \'return\' or \'enter\' to submit your response.\n\nPress the "spacebar" to continue.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "typedresponse" ---
    typed_response = visual.TextBox2(
         win, text=None, placeholder=None, font='Arial',
         pos=(0,0),     letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='typed_response',
         depth=0, autoLog=True,
    )
    key_resp = keyboard.Keyboard()
    text_2 = visual.TextStim(win=win, name='text_2',
        text='Please type your response.',
        font='Open Sans',
        pos=(0, 2), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "thankyou" ---
    thankyoutext = visual.TextStim(win=win, name='thankyoutext',
        text="Thank you for participating!\n\nPress the 'spacebar' to end the session.",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_3 = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Order' + expInfo['fileset'] + '.csv'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "break_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('break_2.started', globalClock.getTime())
        startresp2.keys = []
        startresp2.rt = []
        _startresp2_allKeys = []
        # keep track of which components have finished
        break_2Components = [begin, startresp2]
        for thisComponent in break_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "break_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *begin* updates
            
            # if begin is starting this frame...
            if begin.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                begin.frameNStart = frameN  # exact frame index
                begin.tStart = t  # local t and not account for scr refresh
                begin.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(begin, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'begin.started')
                # update status
                begin.status = STARTED
                begin.setAutoDraw(True)
            
            # if begin is active this frame...
            if begin.status == STARTED:
                # update params
                pass
            
            # *startresp2* updates
            waitOnFlip = False
            
            # if startresp2 is starting this frame...
            if startresp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                startresp2.frameNStart = frameN  # exact frame index
                startresp2.tStart = t  # local t and not account for scr refresh
                startresp2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(startresp2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'startresp2.started')
                # update status
                startresp2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(startresp2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(startresp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if startresp2.status == STARTED and not waitOnFlip:
                theseKeys = startresp2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _startresp2_allKeys.extend(theseKeys)
                if len(_startresp2_allKeys):
                    startresp2.keys = _startresp2_allKeys[-1].name  # just the last key pressed
                    startresp2.rt = _startresp2_allKeys[-1].rt
                    startresp2.duration = _startresp2_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in break_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "break_2" ---
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('break_2.stopped', globalClock.getTime())
        # check responses
        if startresp2.keys in ['', [], None]:  # No response was made
            startresp2.keys = None
        trials.addData('startresp2.keys',startresp2.keys)
        if startresp2.keys != None:  # we had a response
            trials.addData('startresp2.rt', startresp2.rt)
            trials.addData('startresp2.duration', startresp2.duration)
        # the Routine "break_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Videos" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Videos.started', globalClock.getTime())
        varietyvideos.setMovie(movie_filename)
        # keep track of which components have finished
        VideosComponents = [varietyvideos]
        for thisComponent in VideosComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Videos" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *varietyvideos* updates
            
            # if varietyvideos is starting this frame...
            if varietyvideos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                varietyvideos.frameNStart = frameN  # exact frame index
                varietyvideos.tStart = t  # local t and not account for scr refresh
                varietyvideos.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(varietyvideos, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'varietyvideos.started')
                # update status
                varietyvideos.status = STARTED
                varietyvideos.setAutoDraw(True)
                varietyvideos.play()
            
            # if varietyvideos is stopping this frame...
            if varietyvideos.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > varietyvideos.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    varietyvideos.tStop = t  # not accounting for scr refresh
                    varietyvideos.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'varietyvideos.stopped')
                    # update status
                    varietyvideos.status = FINISHED
                    varietyvideos.setAutoDraw(False)
                    varietyvideos.stop()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in VideosComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Videos" ---
        for thisComponent in VideosComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Videos.stopped', globalClock.getTime())
        varietyvideos.stop()  # ensure movie has stopped at end of Routine
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        
        # --- Prepare to start Routine "instructionsreaction2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('instructionsreaction2.started', globalClock.getTime())
        startresp3.keys = []
        startresp3.rt = []
        _startresp3_allKeys = []
        # keep track of which components have finished
        instructionsreaction2Components = [reactioninstructions, startresp3]
        for thisComponent in instructionsreaction2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "instructionsreaction2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *reactioninstructions* updates
            
            # if reactioninstructions is starting this frame...
            if reactioninstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                reactioninstructions.frameNStart = frameN  # exact frame index
                reactioninstructions.tStart = t  # local t and not account for scr refresh
                reactioninstructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reactioninstructions, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'reactioninstructions.started')
                # update status
                reactioninstructions.status = STARTED
                reactioninstructions.setAutoDraw(True)
            
            # if reactioninstructions is active this frame...
            if reactioninstructions.status == STARTED:
                # update params
                pass
            
            # *startresp3* updates
            waitOnFlip = False
            
            # if startresp3 is starting this frame...
            if startresp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                startresp3.frameNStart = frameN  # exact frame index
                startresp3.tStart = t  # local t and not account for scr refresh
                startresp3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(startresp3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'startresp3.started')
                # update status
                startresp3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(startresp3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(startresp3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if startresp3.status == STARTED and not waitOnFlip:
                theseKeys = startresp3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _startresp3_allKeys.extend(theseKeys)
                if len(_startresp3_allKeys):
                    startresp3.keys = _startresp3_allKeys[-1].name  # just the last key pressed
                    startresp3.rt = _startresp3_allKeys[-1].rt
                    startresp3.duration = _startresp3_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instructionsreaction2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "instructionsreaction2" ---
        for thisComponent in instructionsreaction2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('instructionsreaction2.stopped', globalClock.getTime())
        # check responses
        if startresp3.keys in ['', [], None]:  # No response was made
            startresp3.keys = None
        trials.addData('startresp3.keys',startresp3.keys)
        if startresp3.keys != None:  # we had a response
            trials.addData('startresp3.rt', startresp3.rt)
            trials.addData('startresp3.duration', startresp3.duration)
        # the Routine "instructionsreaction2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "affect" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('affect.started', globalClock.getTime())
        # setup some python lists for storing info about the mouseaffect
        mouseaffect.x = []
        mouseaffect.y = []
        mouseaffect.leftButton = []
        mouseaffect.midButton = []
        mouseaffect.rightButton = []
        mouseaffect.time = []
        gotValidClick = False  # until a click is received
        mouseaffect.mouseClock.reset()
        # keep track of which components have finished
        affectComponents = [affectrating, mouseaffect]
        for thisComponent in affectComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "affect" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *affectrating* updates
            
            # if affectrating is starting this frame...
            if affectrating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                affectrating.frameNStart = frameN  # exact frame index
                affectrating.tStart = t  # local t and not account for scr refresh
                affectrating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(affectrating, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'affectrating.started')
                # update status
                affectrating.status = STARTED
                affectrating.setAutoDraw(True)
            
            # if affectrating is active this frame...
            if affectrating.status == STARTED:
                # update params
                pass
            # *mouseaffect* updates
            
            # if mouseaffect is starting this frame...
            if mouseaffect.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouseaffect.frameNStart = frameN  # exact frame index
                mouseaffect.tStart = t  # local t and not account for scr refresh
                mouseaffect.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouseaffect, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouseaffect.status = STARTED
                prevButtonState = mouseaffect.getPressed()  # if button is down already this ISN'T a new click
            if mouseaffect.status == STARTED:  # only update if started and not finished!
                buttons = mouseaffect.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        x, y = mouseaffect.getPos()
                        mouseaffect.x.append(x)
                        mouseaffect.y.append(y)
                        buttons = mouseaffect.getPressed()
                        mouseaffect.leftButton.append(buttons[0])
                        mouseaffect.midButton.append(buttons[1])
                        mouseaffect.rightButton.append(buttons[2])
                        mouseaffect.time.append(mouseaffect.mouseClock.getTime())
                        
                        continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in affectComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "affect" ---
        for thisComponent in affectComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('affect.stopped', globalClock.getTime())
        # store data for trials (TrialHandler)
        trials.addData('mouseaffect.x', mouseaffect.x)
        trials.addData('mouseaffect.y', mouseaffect.y)
        trials.addData('mouseaffect.leftButton', mouseaffect.leftButton)
        trials.addData('mouseaffect.midButton', mouseaffect.midButton)
        trials.addData('mouseaffect.rightButton', mouseaffect.rightButton)
        trials.addData('mouseaffect.time', mouseaffect.time)
        # the Routine "affect" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "anxiety" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('anxiety.started', globalClock.getTime())
        # setup some python lists for storing info about the mouseanxiety
        mouseanxiety.x = []
        mouseanxiety.y = []
        mouseanxiety.leftButton = []
        mouseanxiety.midButton = []
        mouseanxiety.rightButton = []
        mouseanxiety.time = []
        gotValidClick = False  # until a click is received
        mouseanxiety.mouseClock.reset()
        slider.reset()
        # keep track of which components have finished
        anxietyComponents = [image, mouseanxiety, slider]
        for thisComponent in anxietyComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "anxiety" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            
            # if image is starting this frame...
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.started')
                # update status
                image.status = STARTED
                image.setAutoDraw(True)
            
            # if image is active this frame...
            if image.status == STARTED:
                # update params
                pass
            # *mouseanxiety* updates
            
            # if mouseanxiety is starting this frame...
            if mouseanxiety.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouseanxiety.frameNStart = frameN  # exact frame index
                mouseanxiety.tStart = t  # local t and not account for scr refresh
                mouseanxiety.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouseanxiety, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouseanxiety.status = STARTED
                prevButtonState = mouseanxiety.getPressed()  # if button is down already this ISN'T a new click
            if mouseanxiety.status == STARTED:  # only update if started and not finished!
                buttons = mouseanxiety.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        x, y = mouseanxiety.getPos()
                        mouseanxiety.x.append(x)
                        mouseanxiety.y.append(y)
                        buttons = mouseanxiety.getPressed()
                        mouseanxiety.leftButton.append(buttons[0])
                        mouseanxiety.midButton.append(buttons[1])
                        mouseanxiety.rightButton.append(buttons[2])
                        mouseanxiety.time.append(mouseanxiety.mouseClock.getTime())
                        
                        continueRoutine = False  # end routine on response
            
            # *slider* updates
            
            # if slider is starting this frame...
            if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider.frameNStart = frameN  # exact frame index
                slider.tStart = t  # local t and not account for scr refresh
                slider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider.started')
                # update status
                slider.status = STARTED
                slider.setAutoDraw(True)
            
            # if slider is active this frame...
            if slider.status == STARTED:
                # update params
                pass
            
            # Check slider for response to end Routine
            if slider.getRating() is not None and slider.status == STARTED:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in anxietyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "anxiety" ---
        for thisComponent in anxietyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('anxiety.stopped', globalClock.getTime())
        # store data for trials (TrialHandler)
        trials.addData('mouseanxiety.x', mouseanxiety.x)
        trials.addData('mouseanxiety.y', mouseanxiety.y)
        trials.addData('mouseanxiety.leftButton', mouseanxiety.leftButton)
        trials.addData('mouseanxiety.midButton', mouseanxiety.midButton)
        trials.addData('mouseanxiety.rightButton', mouseanxiety.rightButton)
        trials.addData('mouseanxiety.time', mouseanxiety.time)
        trials.addData('slider.response', slider.getRating())
        trials.addData('slider.rt', slider.getRT())
        # the Routine "anxiety" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "energy" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('energy.started', globalClock.getTime())
        # setup some python lists for storing info about the mouseenergy
        mouseenergy.x = []
        mouseenergy.y = []
        mouseenergy.leftButton = []
        mouseenergy.midButton = []
        mouseenergy.rightButton = []
        mouseenergy.time = []
        gotValidClick = False  # until a click is received
        mouseenergy.mouseClock.reset()
        # keep track of which components have finished
        energyComponents = [energyimage, mouseenergy]
        for thisComponent in energyComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "energy" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *energyimage* updates
            
            # if energyimage is starting this frame...
            if energyimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                energyimage.frameNStart = frameN  # exact frame index
                energyimage.tStart = t  # local t and not account for scr refresh
                energyimage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(energyimage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'energyimage.started')
                # update status
                energyimage.status = STARTED
                energyimage.setAutoDraw(True)
            
            # if energyimage is active this frame...
            if energyimage.status == STARTED:
                # update params
                pass
            # *mouseenergy* updates
            
            # if mouseenergy is starting this frame...
            if mouseenergy.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouseenergy.frameNStart = frameN  # exact frame index
                mouseenergy.tStart = t  # local t and not account for scr refresh
                mouseenergy.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouseenergy, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouseenergy.status = STARTED
                prevButtonState = mouseenergy.getPressed()  # if button is down already this ISN'T a new click
            if mouseenergy.status == STARTED:  # only update if started and not finished!
                buttons = mouseenergy.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        x, y = mouseenergy.getPos()
                        mouseenergy.x.append(x)
                        mouseenergy.y.append(y)
                        buttons = mouseenergy.getPressed()
                        mouseenergy.leftButton.append(buttons[0])
                        mouseenergy.midButton.append(buttons[1])
                        mouseenergy.rightButton.append(buttons[2])
                        mouseenergy.time.append(mouseenergy.mouseClock.getTime())
                        
                        continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in energyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "energy" ---
        for thisComponent in energyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('energy.stopped', globalClock.getTime())
        # store data for trials (TrialHandler)
        trials.addData('mouseenergy.x', mouseenergy.x)
        trials.addData('mouseenergy.y', mouseenergy.y)
        trials.addData('mouseenergy.leftButton', mouseenergy.leftButton)
        trials.addData('mouseenergy.midButton', mouseenergy.midButton)
        trials.addData('mouseenergy.rightButton', mouseenergy.rightButton)
        trials.addData('mouseenergy.time', mouseenergy.time)
        # the Routine "energy" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "pride" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('pride.started', globalClock.getTime())
        # setup some python lists for storing info about the mousepride
        mousepride.x = []
        mousepride.y = []
        mousepride.leftButton = []
        mousepride.midButton = []
        mousepride.rightButton = []
        mousepride.time = []
        gotValidClick = False  # until a click is received
        mousepride.mouseClock.reset()
        # keep track of which components have finished
        prideComponents = [imagepride, mousepride]
        for thisComponent in prideComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "pride" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *imagepride* updates
            
            # if imagepride is starting this frame...
            if imagepride.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                imagepride.frameNStart = frameN  # exact frame index
                imagepride.tStart = t  # local t and not account for scr refresh
                imagepride.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imagepride, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imagepride.started')
                # update status
                imagepride.status = STARTED
                imagepride.setAutoDraw(True)
            
            # if imagepride is active this frame...
            if imagepride.status == STARTED:
                # update params
                pass
            # *mousepride* updates
            
            # if mousepride is starting this frame...
            if mousepride.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mousepride.frameNStart = frameN  # exact frame index
                mousepride.tStart = t  # local t and not account for scr refresh
                mousepride.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mousepride, 'tStartRefresh')  # time at next scr refresh
                # update status
                mousepride.status = STARTED
                prevButtonState = mousepride.getPressed()  # if button is down already this ISN'T a new click
            if mousepride.status == STARTED:  # only update if started and not finished!
                buttons = mousepride.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        x, y = mousepride.getPos()
                        mousepride.x.append(x)
                        mousepride.y.append(y)
                        buttons = mousepride.getPressed()
                        mousepride.leftButton.append(buttons[0])
                        mousepride.midButton.append(buttons[1])
                        mousepride.rightButton.append(buttons[2])
                        mousepride.time.append(mousepride.mouseClock.getTime())
                        
                        continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prideComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pride" ---
        for thisComponent in prideComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('pride.stopped', globalClock.getTime())
        # store data for trials (TrialHandler)
        trials.addData('mousepride.x', mousepride.x)
        trials.addData('mousepride.y', mousepride.y)
        trials.addData('mousepride.leftButton', mousepride.leftButton)
        trials.addData('mousepride.midButton', mousepride.midButton)
        trials.addData('mousepride.rightButton', mousepride.rightButton)
        trials.addData('mousepride.time', mousepride.time)
        # the Routine "pride" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "typeinstructions" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('typeinstructions.started', globalClock.getTime())
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        typeinstructionsComponents = [text, key_resp_2]
        for thisComponent in typeinstructionsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "typeinstructions" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # *key_resp_2* updates
            waitOnFlip = False
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2.started')
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in typeinstructionsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "typeinstructions" ---
        for thisComponent in typeinstructionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('typeinstructions.stopped', globalClock.getTime())
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        trials.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            trials.addData('key_resp_2.rt', key_resp_2.rt)
            trials.addData('key_resp_2.duration', key_resp_2.duration)
        # the Routine "typeinstructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "typedresponse" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('typedresponse.started', globalClock.getTime())
        typed_response.reset()
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        typedresponseComponents = [typed_response, key_resp, text_2]
        for thisComponent in typedresponseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "typedresponse" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *typed_response* updates
            
            # if typed_response is starting this frame...
            if typed_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                typed_response.frameNStart = frameN  # exact frame index
                typed_response.tStart = t  # local t and not account for scr refresh
                typed_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(typed_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'typed_response.started')
                # update status
                typed_response.status = STARTED
                typed_response.setAutoDraw(True)
            
            # if typed_response is active this frame...
            if typed_response.status == STARTED:
                # update params
                pass
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in typedresponseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "typedresponse" ---
        for thisComponent in typedresponseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('typedresponse.stopped', globalClock.getTime())
        trials.addData('typed_response.text',typed_response.text)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
            trials.addData('key_resp.duration', key_resp.duration)
        # the Routine "typedresponse" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "thankyou" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('thankyou.started', globalClock.getTime())
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    thankyouComponents = [thankyoutext, key_resp_3]
    for thisComponent in thankyouComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "thankyou" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *thankyoutext* updates
        
        # if thankyoutext is starting this frame...
        if thankyoutext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            thankyoutext.frameNStart = frameN  # exact frame index
            thankyoutext.tStart = t  # local t and not account for scr refresh
            thankyoutext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thankyoutext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thankyoutext.started')
            # update status
            thankyoutext.status = STARTED
            thankyoutext.setAutoDraw(True)
        
        # if thankyoutext is active this frame...
        if thankyoutext.status == STARTED:
            # update params
            pass
        
        # *key_resp_3* updates
        waitOnFlip = False
        
        # if key_resp_3 is starting this frame...
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            # update status
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in thankyouComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "thankyou" ---
    for thisComponent in thankyouComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('thankyou.stopped', globalClock.getTime())
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    thisExp.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        thisExp.addData('key_resp_3.rt', key_resp_3.rt)
        thisExp.addData('key_resp_3.duration', key_resp_3.duration)
    thisExp.nextEntry()
    # the Routine "thankyou" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
