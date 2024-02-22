/********************** 
 * Peaceskeleton *
 **********************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.2.3.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'PEACEskeleton';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'fileset': '',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color('black'),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(welcomeRoutineBegin());
flowScheduler.add(welcomeRoutineEachFrame());
flowScheduler.add(welcomeRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);










flowScheduler.add(thankyouRoutineBegin());
flowScheduler.add(thankyouRoutineEachFrame());
flowScheduler.add(thankyouRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'Practice45VideosListmov.xlsx', 'path': 'Practice45VideosListmov.xlsx'},
    {'name': 'practicelistof45/057 copy.mp4', 'path': 'practicelistof45/057 copy.mp4'},
    {'name': 'practicelistof45/057 copy.webm', 'path': 'practicelistof45/057 copy.webm'},
    {'name': 'AAPE Images for PsychoPy/Jpeg - not great/affectAAPE.jpg', 'path': 'AAPE Images for PsychoPy/Jpeg - not great/affectAAPE.jpg'},
    {'name': 'AAPE Images for PsychoPy/Jpeg - not great/anxietyAAPE.jpg', 'path': 'AAPE Images for PsychoPy/Jpeg - not great/anxietyAAPE.jpg'},
    {'name': 'AAPE Images for PsychoPy/Jpeg - not great/energyAAPE.jpg', 'path': 'AAPE Images for PsychoPy/Jpeg - not great/energyAAPE.jpg'},
    {'name': 'AAPE Images for PsychoPy/Jpeg - not great/prideAAPE.jpeg', 'path': 'AAPE Images for PsychoPy/Jpeg - not great/prideAAPE.jpeg'},
    {'name': 'AAPE Images for PsychoPy/Photoshop/Affect.png', 'path': 'AAPE Images for PsychoPy/Photoshop/Affect.png'},
    {'name': 'AAPE Images for PsychoPy/Photoshop/Anxiety.png', 'path': 'AAPE Images for PsychoPy/Photoshop/Anxiety.png'},
    {'name': 'AAPE Images for PsychoPy/Photoshop/Energy.png', 'path': 'AAPE Images for PsychoPy/Photoshop/Energy.png'},
    {'name': 'AAPE Images for PsychoPy/Photoshop/Pride.png', 'path': 'AAPE Images for PsychoPy/Photoshop/Pride.png'},
    {'name': 'practicelistof45/057 copy.avi', 'path': 'practicelistof45/057 copy.avi'},
    {'name': 'fileorders/Order001.csv', 'path': 'fileorders/Order001.csv'},
    {'name': 'fileorders/Order002.csv', 'path': 'fileorders/Order002.csv'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.2.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["fileset"]}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var welcomeClock;
var Intro;
var startresp;
var resources_2;
var loop_beginClock;
var begin_video_loop;
var startresp2;
var VideosClock;
var varietyvideosClock;
var varietyvideos;
var reaction_instructionsClock;
var textbox;
var startresp3;
var affectClock;
var affect_image;
var affect_slider;
var anxietyClock;
var anxiety_image;
var anxiety_slider;
var energyClock;
var energy_image;
var energy_slider;
var prideClock;
var pride_image;
var pride_slider;
var type_instructionsClock;
var word_instructions;
var key_resp_2;
var typed_word_responseClock;
var typed_response;
var text_2;
var key_resp;
var thankyouClock;
var thankyoutext;
var key_resp_3;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "welcome"
  welcomeClock = new util.Clock();
  Intro = new visual.TextBox({
    win: psychoJS.window,
    name: 'Intro',
    text: "Today you will watch several video clips that will elicit an emotional reaction. Each clip is approximately 3-5 seconds in duration. \n\nAfter each video, you will be asked to rate the video using a visual scale. Then you will describe how the video made you feel by typing a word or short phrase (1-3 words).\n\nWe will first have you complete a practice so you can familiarize yourself with the task. \n\nPress the 'space bar' to begin the practice.\n",
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1.5, 1.5],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  startresp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  resources_2 = {
    status: PsychoJS.Status.NOT_STARTED
  };
  // Initialize components for Routine "loop_begin"
  loop_beginClock = new util.Clock();
  begin_video_loop = new visual.TextStim({
    win: psychoJS.window,
    name: 'begin_video_loop',
    text: "Press the 'space bar' to begin the video.",
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  startresp2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Videos"
  VideosClock = new util.Clock();
  varietyvideosClock = new util.Clock();
  varietyvideos = new visual.MovieStim({
    win: psychoJS.window,
    name: 'varietyvideos',
    units: psychoJS.window.units,
    movie: undefined,
    pos: [0, 0],
    anchor: 'center',
    size: [2, 1],
    ori: 0.0,
    opacity: undefined,
    loop: false,
    noAudio: false,
    depth: 0
    });
  // Initialize components for Routine "reaction_instructions"
  reaction_instructionsClock = new util.Clock();
  textbox = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox',
    text: "Now you will be asked to rate how the video made you feel using a set of pictorial rating scales.\n\nYou will be shown four different rating scales consisting of five pictures each. Please use the mouse to click the number under the picture that most closely resembles how this video clip made you feel. \n\nClicking the number will advance you on to the next scale.\n\nPress the 'space bar' to continue.\n\n",
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1.5, 1.5],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  startresp3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "affect"
  affectClock = new util.Clock();
  affect_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'affect_image', units : 'norm', 
    image : 'AAPE Images for PsychoPy/Photoshop/Affect.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [1.5, 0.75],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  affect_slider = new visual.Slider({
    win: psychoJS.window, name: 'affect_slider',
    startValue: undefined,
    size: [1.0, 0.1], pos: [0, (- 0.4)], ori: 0.0, units: psychoJS.window.units,
    labels: [1, 2, 3, 4, 5], fontSize: 0.05, ticks: [1, 2, 3, 4, 5],
    granularity: 0.0, style: ["RADIO"],
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]), markerColor: new util.Color([(- 0.2549), 0.2392, 0.2549]), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  // Initialize components for Routine "anxiety"
  anxietyClock = new util.Clock();
  anxiety_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'anxiety_image', units : 'norm', 
    image : 'AAPE Images for PsychoPy/Photoshop/Anxiety.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [1.5, 0.75],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  anxiety_slider = new visual.Slider({
    win: psychoJS.window, name: 'anxiety_slider',
    startValue: undefined,
    size: [1.0, 0.1], pos: [0, (- 0.4)], ori: 0.0, units: psychoJS.window.units,
    labels: [1, 2, 3, 4, 5], fontSize: 0.05, ticks: [1, 2, 3, 4, 5],
    granularity: 0.0, style: ["RADIO"],
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]), markerColor: new util.Color([(- 0.2549), 0.2392, 0.2549]), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  // Initialize components for Routine "energy"
  energyClock = new util.Clock();
  energy_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'energy_image', units : 'norm', 
    image : 'AAPE Images for PsychoPy/Photoshop/Energy.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [1.5, 0.75],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  energy_slider = new visual.Slider({
    win: psychoJS.window, name: 'energy_slider',
    startValue: undefined,
    size: [1.0, 0.1], pos: [0, (- 0.4)], ori: 0.0, units: psychoJS.window.units,
    labels: [1, 2, 3, 4, 5], fontSize: 0.05, ticks: [1, 2, 3, 4, 5],
    granularity: 0.0, style: ["RADIO"],
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]), markerColor: new util.Color([(- 0.2549), 0.2392, 0.2549]), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  // Initialize components for Routine "pride"
  prideClock = new util.Clock();
  pride_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'pride_image', units : undefined, 
    image : 'AAPE Images for PsychoPy/Photoshop/Pride.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [1.25, 0.35],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  pride_slider = new visual.Slider({
    win: psychoJS.window, name: 'pride_slider',
    startValue: undefined,
    size: [1.0, 0.1], pos: [0, (- 0.4)], ori: 0.0, units: psychoJS.window.units,
    labels: [1, 2, 3, 4, 5], fontSize: 0.05, ticks: [1, 2, 3, 4, 5],
    granularity: 0.0, style: ["RADIO"],
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]), markerColor: new util.Color([(- 0.2549), 0.2392, 0.2549]), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  // Initialize components for Routine "type_instructions"
  type_instructionsClock = new util.Clock();
  word_instructions = new visual.TextBox({
    win: psychoJS.window,
    name: 'word_instructions',
    text: "Now, you will explain how the video made you feel by typing a word or short phrase.\n\nAfter you type in your word or phrase, hit 'return' or 'enter' to submit your response.\n\nPress the 'space bar' to continue.\n",
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1.5, 1.5],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center-left',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "typed_word_response"
  typed_word_responseClock = new util.Clock();
  typed_response = new visual.TextBox({
    win: psychoJS.window,
    name: 'typed_response',
    text: '',
    placeholder: undefined,
    font: 'Arial',
    pos: [0, 0], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1.5, 0.2],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: [(- 0.2549), 0.2392, 0.2549],
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Please type your response.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 2], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "thankyou"
  thankyouClock = new util.Clock();
  thankyoutext = new visual.TextStim({
    win: psychoJS.window,
    name: 'thankyoutext',
    text: "Thank you for participating! \n\nPress the 'spacebar' to end the session.",
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _startresp_allKeys;
var welcomeComponents;
function welcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'welcome' ---
    t = 0;
    welcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('welcome.started', globalClock.getTime());
    startresp.keys = undefined;
    startresp.rt = undefined;
    _startresp_allKeys = [];
    // keep track of which components have finished
    welcomeComponents = [];
    welcomeComponents.push(Intro);
    welcomeComponents.push(startresp);
    welcomeComponents.push(resources_2);
    
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function welcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'welcome' ---
    // get current time
    t = welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Intro* updates
    if (t >= 0.0 && Intro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Intro.tStart = t;  // (not accounting for frame time here)
      Intro.frameNStart = frameN;  // exact frame index
      
      Intro.setAutoDraw(true);
    }
    
    
    // *startresp* updates
    if (t >= 0.0 && startresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startresp.tStart = t;  // (not accounting for frame time here)
      startresp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { startresp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { startresp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { startresp.clearEvents(); });
    }
    
    if (startresp.status === PsychoJS.Status.STARTED) {
      let theseKeys = startresp.getKeys({keyList: ['space'], waitRelease: false});
      _startresp_allKeys = _startresp_allKeys.concat(theseKeys);
      if (_startresp_allKeys.length > 0) {
        startresp.keys = _startresp_allKeys[_startresp_allKeys.length - 1].name;  // just the last key pressed
        startresp.rt = _startresp_allKeys[_startresp_allKeys.length - 1].rt;
        startresp.duration = _startresp_allKeys[_startresp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // start downloading resources specified by component resources_2
    if (t >= 0 && resources_2.status === PsychoJS.Status.NOT_STARTED) {
      console.log('register and start downloading resources specified by component resources_2');
      await psychoJS.serverManager.prepareResources(['practicelistof45/057 copy.avi', 'fileorders/Order001.csv']);
      resources_2.status = PsychoJS.Status.STARTED;
    }
    // check on the resources specified by component resources_2
    if (t >= null && resources_2.status === PsychoJS.Status.STARTED) {
      if (psychoJS.serverManager.getResourceStatus(['practicelistof45/057 copy.avi', 'fileorders/Order001.csv']) === core.ServerManager.ResourceStatus.DOWNLOADED) {
        console.log('finished downloading resources specified by component resources_2');
        resources_2.status = PsychoJS.Status.FINISHED;
      } else {
        console.log('resource specified in resources_2 took longer than expected to download');
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'welcome' ---
    for (const thisComponent of welcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('welcome.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(startresp.corr, level);
    }
    psychoJS.experiment.addData('startresp.keys', startresp.keys);
    if (typeof startresp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('startresp.rt', startresp.rt);
        psychoJS.experiment.addData('startresp.duration', startresp.duration);
        routineTimer.reset();
        }
    
    startresp.stop();
    // the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: (("fileorders/Order" + expInfo["fileset"]) + ".csv"),
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(loop_beginRoutineBegin(snapshot));
      trialsLoopScheduler.add(loop_beginRoutineEachFrame());
      trialsLoopScheduler.add(loop_beginRoutineEnd(snapshot));
      trialsLoopScheduler.add(VideosRoutineBegin(snapshot));
      trialsLoopScheduler.add(VideosRoutineEachFrame());
      trialsLoopScheduler.add(VideosRoutineEnd(snapshot));
      trialsLoopScheduler.add(reaction_instructionsRoutineBegin(snapshot));
      trialsLoopScheduler.add(reaction_instructionsRoutineEachFrame());
      trialsLoopScheduler.add(reaction_instructionsRoutineEnd(snapshot));
      trialsLoopScheduler.add(affectRoutineBegin(snapshot));
      trialsLoopScheduler.add(affectRoutineEachFrame());
      trialsLoopScheduler.add(affectRoutineEnd(snapshot));
      trialsLoopScheduler.add(anxietyRoutineBegin(snapshot));
      trialsLoopScheduler.add(anxietyRoutineEachFrame());
      trialsLoopScheduler.add(anxietyRoutineEnd(snapshot));
      trialsLoopScheduler.add(energyRoutineBegin(snapshot));
      trialsLoopScheduler.add(energyRoutineEachFrame());
      trialsLoopScheduler.add(energyRoutineEnd(snapshot));
      trialsLoopScheduler.add(prideRoutineBegin(snapshot));
      trialsLoopScheduler.add(prideRoutineEachFrame());
      trialsLoopScheduler.add(prideRoutineEnd(snapshot));
      trialsLoopScheduler.add(type_instructionsRoutineBegin(snapshot));
      trialsLoopScheduler.add(type_instructionsRoutineEachFrame());
      trialsLoopScheduler.add(type_instructionsRoutineEnd(snapshot));
      trialsLoopScheduler.add(typed_word_responseRoutineBegin(snapshot));
      trialsLoopScheduler.add(typed_word_responseRoutineEachFrame());
      trialsLoopScheduler.add(typed_word_responseRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var _startresp2_allKeys;
var loop_beginComponents;
function loop_beginRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'loop_begin' ---
    t = 0;
    loop_beginClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('loop_begin.started', globalClock.getTime());
    startresp2.keys = undefined;
    startresp2.rt = undefined;
    _startresp2_allKeys = [];
    // keep track of which components have finished
    loop_beginComponents = [];
    loop_beginComponents.push(begin_video_loop);
    loop_beginComponents.push(startresp2);
    
    for (const thisComponent of loop_beginComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function loop_beginRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'loop_begin' ---
    // get current time
    t = loop_beginClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *begin_video_loop* updates
    if (t >= 0.0 && begin_video_loop.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      begin_video_loop.tStart = t;  // (not accounting for frame time here)
      begin_video_loop.frameNStart = frameN;  // exact frame index
      
      begin_video_loop.setAutoDraw(true);
    }
    
    
    // *startresp2* updates
    if (t >= 0.0 && startresp2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startresp2.tStart = t;  // (not accounting for frame time here)
      startresp2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { startresp2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { startresp2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { startresp2.clearEvents(); });
    }
    
    if (startresp2.status === PsychoJS.Status.STARTED) {
      let theseKeys = startresp2.getKeys({keyList: ['space'], waitRelease: false});
      _startresp2_allKeys = _startresp2_allKeys.concat(theseKeys);
      if (_startresp2_allKeys.length > 0) {
        startresp2.keys = _startresp2_allKeys[_startresp2_allKeys.length - 1].name;  // just the last key pressed
        startresp2.rt = _startresp2_allKeys[_startresp2_allKeys.length - 1].rt;
        startresp2.duration = _startresp2_allKeys[_startresp2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of loop_beginComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function loop_beginRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'loop_begin' ---
    for (const thisComponent of loop_beginComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('loop_begin.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(startresp2.corr, level);
    }
    psychoJS.experiment.addData('startresp2.keys', startresp2.keys);
    if (typeof startresp2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('startresp2.rt', startresp2.rt);
        psychoJS.experiment.addData('startresp2.duration', startresp2.duration);
        routineTimer.reset();
        }
    
    startresp2.stop();
    // the Routine "loop_begin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var VideosComponents;
function VideosRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Videos' ---
    t = 0;
    VideosClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('Videos.started', globalClock.getTime());
    varietyvideos.setMovie(movie_filename);
    // keep track of which components have finished
    VideosComponents = [];
    VideosComponents.push(varietyvideos);
    
    for (const thisComponent of VideosComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function VideosRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Videos' ---
    // get current time
    t = VideosClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *varietyvideos* updates
    if (t >= 0.0 && varietyvideos.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      varietyvideos.tStart = t;  // (not accounting for frame time here)
      varietyvideos.frameNStart = frameN;  // exact frame index
      
      varietyvideos.setAutoDraw(true);
      varietyvideos.play();
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (varietyvideos.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      varietyvideos.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of VideosComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function VideosRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Videos' ---
    for (const thisComponent of VideosComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Videos.stopped', globalClock.getTime());
    varietyvideos.stop();  // ensure movie has stopped at end of Routine
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _startresp3_allKeys;
var reaction_instructionsComponents;
function reaction_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reaction_instructions' ---
    t = 0;
    reaction_instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('reaction_instructions.started', globalClock.getTime());
    startresp3.keys = undefined;
    startresp3.rt = undefined;
    _startresp3_allKeys = [];
    // keep track of which components have finished
    reaction_instructionsComponents = [];
    reaction_instructionsComponents.push(textbox);
    reaction_instructionsComponents.push(startresp3);
    
    for (const thisComponent of reaction_instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function reaction_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reaction_instructions' ---
    // get current time
    t = reaction_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textbox* updates
    if (t >= 0.0 && textbox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox.tStart = t;  // (not accounting for frame time here)
      textbox.frameNStart = frameN;  // exact frame index
      
      textbox.setAutoDraw(true);
    }
    
    
    // *startresp3* updates
    if (t >= 0.0 && startresp3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startresp3.tStart = t;  // (not accounting for frame time here)
      startresp3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { startresp3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { startresp3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { startresp3.clearEvents(); });
    }
    
    if (startresp3.status === PsychoJS.Status.STARTED) {
      let theseKeys = startresp3.getKeys({keyList: ['space'], waitRelease: false});
      _startresp3_allKeys = _startresp3_allKeys.concat(theseKeys);
      if (_startresp3_allKeys.length > 0) {
        startresp3.keys = _startresp3_allKeys[_startresp3_allKeys.length - 1].name;  // just the last key pressed
        startresp3.rt = _startresp3_allKeys[_startresp3_allKeys.length - 1].rt;
        startresp3.duration = _startresp3_allKeys[_startresp3_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of reaction_instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reaction_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reaction_instructions' ---
    for (const thisComponent of reaction_instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('reaction_instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(startresp3.corr, level);
    }
    psychoJS.experiment.addData('startresp3.keys', startresp3.keys);
    if (typeof startresp3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('startresp3.rt', startresp3.rt);
        psychoJS.experiment.addData('startresp3.duration', startresp3.duration);
        routineTimer.reset();
        }
    
    startresp3.stop();
    // the Routine "reaction_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var affectComponents;
function affectRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'affect' ---
    t = 0;
    affectClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('affect.started', globalClock.getTime());
    affect_slider.reset()
    // keep track of which components have finished
    affectComponents = [];
    affectComponents.push(affect_image);
    affectComponents.push(affect_slider);
    
    for (const thisComponent of affectComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function affectRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'affect' ---
    // get current time
    t = affectClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *affect_image* updates
    if (t >= 0.0 && affect_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      affect_image.tStart = t;  // (not accounting for frame time here)
      affect_image.frameNStart = frameN;  // exact frame index
      
      affect_image.setAutoDraw(true);
    }
    
    
    // *affect_slider* updates
    if (t >= 0.0 && affect_slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      affect_slider.tStart = t;  // (not accounting for frame time here)
      affect_slider.frameNStart = frameN;  // exact frame index
      
      affect_slider.setAutoDraw(true);
    }
    
    
    // Check affect_slider for response to end Routine
    if (affect_slider.getRating() !== undefined && affect_slider.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of affectComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function affectRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'affect' ---
    for (const thisComponent of affectComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('affect.stopped', globalClock.getTime());
    psychoJS.experiment.addData('affect_slider.response', affect_slider.getRating());
    psychoJS.experiment.addData('affect_slider.rt', affect_slider.getRT());
    // the Routine "affect" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var anxietyComponents;
function anxietyRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'anxiety' ---
    t = 0;
    anxietyClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('anxiety.started', globalClock.getTime());
    anxiety_slider.reset()
    // keep track of which components have finished
    anxietyComponents = [];
    anxietyComponents.push(anxiety_image);
    anxietyComponents.push(anxiety_slider);
    
    for (const thisComponent of anxietyComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function anxietyRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'anxiety' ---
    // get current time
    t = anxietyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *anxiety_image* updates
    if (t >= 0.0 && anxiety_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      anxiety_image.tStart = t;  // (not accounting for frame time here)
      anxiety_image.frameNStart = frameN;  // exact frame index
      
      anxiety_image.setAutoDraw(true);
    }
    
    
    // *anxiety_slider* updates
    if (t >= 0.0 && anxiety_slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      anxiety_slider.tStart = t;  // (not accounting for frame time here)
      anxiety_slider.frameNStart = frameN;  // exact frame index
      
      anxiety_slider.setAutoDraw(true);
    }
    
    
    // Check anxiety_slider for response to end Routine
    if (anxiety_slider.getRating() !== undefined && anxiety_slider.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of anxietyComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function anxietyRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'anxiety' ---
    for (const thisComponent of anxietyComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('anxiety.stopped', globalClock.getTime());
    psychoJS.experiment.addData('anxiety_slider.response', anxiety_slider.getRating());
    psychoJS.experiment.addData('anxiety_slider.rt', anxiety_slider.getRT());
    // the Routine "anxiety" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var energyComponents;
function energyRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'energy' ---
    t = 0;
    energyClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('energy.started', globalClock.getTime());
    energy_slider.reset()
    // keep track of which components have finished
    energyComponents = [];
    energyComponents.push(energy_image);
    energyComponents.push(energy_slider);
    
    for (const thisComponent of energyComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function energyRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'energy' ---
    // get current time
    t = energyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *energy_image* updates
    if (t >= 0.0 && energy_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      energy_image.tStart = t;  // (not accounting for frame time here)
      energy_image.frameNStart = frameN;  // exact frame index
      
      energy_image.setAutoDraw(true);
    }
    
    
    // *energy_slider* updates
    if (t >= 0.0 && energy_slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      energy_slider.tStart = t;  // (not accounting for frame time here)
      energy_slider.frameNStart = frameN;  // exact frame index
      
      energy_slider.setAutoDraw(true);
    }
    
    
    // Check energy_slider for response to end Routine
    if (energy_slider.getRating() !== undefined && energy_slider.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of energyComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function energyRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'energy' ---
    for (const thisComponent of energyComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('energy.stopped', globalClock.getTime());
    psychoJS.experiment.addData('energy_slider.response', energy_slider.getRating());
    psychoJS.experiment.addData('energy_slider.rt', energy_slider.getRT());
    // the Routine "energy" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var prideComponents;
function prideRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'pride' ---
    t = 0;
    prideClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('pride.started', globalClock.getTime());
    pride_slider.reset()
    // keep track of which components have finished
    prideComponents = [];
    prideComponents.push(pride_image);
    prideComponents.push(pride_slider);
    
    for (const thisComponent of prideComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function prideRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'pride' ---
    // get current time
    t = prideClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *pride_image* updates
    if (t >= 0.0 && pride_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pride_image.tStart = t;  // (not accounting for frame time here)
      pride_image.frameNStart = frameN;  // exact frame index
      
      pride_image.setAutoDraw(true);
    }
    
    
    // *pride_slider* updates
    if (t >= 0.0 && pride_slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pride_slider.tStart = t;  // (not accounting for frame time here)
      pride_slider.frameNStart = frameN;  // exact frame index
      
      pride_slider.setAutoDraw(true);
    }
    
    
    // Check pride_slider for response to end Routine
    if (pride_slider.getRating() !== undefined && pride_slider.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of prideComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prideRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'pride' ---
    for (const thisComponent of prideComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('pride.stopped', globalClock.getTime());
    psychoJS.experiment.addData('pride_slider.response', pride_slider.getRating());
    psychoJS.experiment.addData('pride_slider.rt', pride_slider.getRT());
    // the Routine "pride" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_2_allKeys;
var type_instructionsComponents;
function type_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'type_instructions' ---
    t = 0;
    type_instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('type_instructions.started', globalClock.getTime());
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    type_instructionsComponents = [];
    type_instructionsComponents.push(word_instructions);
    type_instructionsComponents.push(key_resp_2);
    
    for (const thisComponent of type_instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function type_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'type_instructions' ---
    // get current time
    t = type_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *word_instructions* updates
    if (t >= 0.0 && word_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      word_instructions.tStart = t;  // (not accounting for frame time here)
      word_instructions.frameNStart = frameN;  // exact frame index
      
      word_instructions.setAutoDraw(true);
    }
    
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }
    
    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        key_resp_2.duration = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of type_instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function type_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'type_instructions' ---
    for (const thisComponent of type_instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('type_instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        psychoJS.experiment.addData('key_resp_2.duration', key_resp_2.duration);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "type_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_allKeys;
var typed_word_responseComponents;
function typed_word_responseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'typed_word_response' ---
    t = 0;
    typed_word_responseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('typed_word_response.started', globalClock.getTime());
    typed_response.setText('');
    typed_response.refresh();
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    typed_word_responseComponents = [];
    typed_word_responseComponents.push(typed_response);
    typed_word_responseComponents.push(text_2);
    typed_word_responseComponents.push(key_resp);
    
    for (const thisComponent of typed_word_responseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function typed_word_responseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'typed_word_response' ---
    // get current time
    t = typed_word_responseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *typed_response* updates
    if (t >= 0.0 && typed_response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      typed_response.tStart = t;  // (not accounting for frame time here)
      typed_response.frameNStart = frameN;  // exact frame index
      
      typed_response.setAutoDraw(true);
    }
    
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }
    
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['return'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of typed_word_responseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function typed_word_responseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'typed_word_response' ---
    for (const thisComponent of typed_word_responseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('typed_word_response.stopped', globalClock.getTime());
    psychoJS.experiment.addData('typed_response.text',typed_response.text)
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "typed_word_response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_3_allKeys;
var thankyouComponents;
function thankyouRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'thankyou' ---
    t = 0;
    thankyouClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('thankyou.started', globalClock.getTime());
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    thankyouComponents = [];
    thankyouComponents.push(thankyoutext);
    thankyouComponents.push(key_resp_3);
    
    for (const thisComponent of thankyouComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function thankyouRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'thankyou' ---
    // get current time
    t = thankyouClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *thankyoutext* updates
    if (t >= 0.0 && thankyoutext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      thankyoutext.tStart = t;  // (not accounting for frame time here)
      thankyoutext.frameNStart = frameN;  // exact frame index
      
      thankyoutext.setAutoDraw(true);
    }
    
    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }
    
    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        key_resp_3.duration = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of thankyouComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function thankyouRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'thankyou' ---
    for (const thisComponent of thankyouComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('thankyou.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        psychoJS.experiment.addData('key_resp_3.duration', key_resp_3.duration);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "thankyou" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
