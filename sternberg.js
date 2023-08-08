/****************** 
 * Sternberg Test *
 ******************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2022.2.5.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'sternberg';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'session': '02',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color('white'),
  units: 'height',
  waitBlanking: true
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
flowScheduler.add(pracInstruct1RoutineBegin());
flowScheduler.add(pracInstruct1RoutineEachFrame());
flowScheduler.add(pracInstruct1RoutineEnd());
flowScheduler.add(practInstructRoutineBegin());
flowScheduler.add(practInstructRoutineEachFrame());
flowScheduler.add(practInstructRoutineEnd());
const pracTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(pracTrialsLoopBegin(pracTrialsLoopScheduler));
flowScheduler.add(pracTrialsLoopScheduler);
flowScheduler.add(pracTrialsLoopEnd);
flowScheduler.add(mainInstructRoutineBegin());
flowScheduler.add(mainInstructRoutineEachFrame());
flowScheduler.add(mainInstructRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(Break_1RoutineBegin());
flowScheduler.add(Break_1RoutineEachFrame());
flowScheduler.add(Break_1RoutineEnd());
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin(trials_2LoopScheduler));
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);
flowScheduler.add(Break_2RoutineBegin());
flowScheduler.add(Break_2RoutineEachFrame());
flowScheduler.add(Break_2RoutineEnd());
const trials_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_3LoopBegin(trials_3LoopScheduler));
flowScheduler.add(trials_3LoopScheduler);
flowScheduler.add(trials_3LoopEnd);
flowScheduler.add(thanksRoutineBegin());
flowScheduler.add(thanksRoutineEachFrame());
flowScheduler.add(thanksRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'pracTrials.xlsx', 'path': 'pracTrials.xlsx'},
    {'name': 'image_rem.jpg', 'path': 'image_rem.jpg'},
    {'name': 'mainTrials.xlsx', 'path': 'mainTrials.xlsx'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.WARNING);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.5';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);


  return Scheduler.Event.NEXT;
}


var pracInstruct1Clock;
var text_2;
var key_resp;
var practInstructClock;
var instr1;
var OK1;
var image;
var trialClock;
var fixation;
var presentSet;
var presentTarget;
var resp;
var Corr_count_prac;
var feedbackClock;
var msg;
var feedback_2;
var mainInstructClock;
var instr2;
var OK2;
var text;
var trial2Clock;
var fixation2;
var presentSet2;
var presentTarget2;
var resp2;
var Corr_count;
var feedback2Clock;
var feedback2_3;
var Break_1Clock;
var break_msg;
var OK2_2;
var Break_2Clock;
var break_msg_2;
var OK2_3;
var thanksClock;
var thanksMsg;
var totalsc;
var key_resp_2;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "pracInstruct1"
  pracInstruct1Clock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'In this experiment you will be presented with a sequence of between 1 and 6 randomly ordered numbers.\n\nFollowing a short delay you will then be presented with a single number and you will have to decide whether this new number was a member of the sequence.\n\nPress any key to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practInstruct"
  practInstructClock = new util.Clock();
  instr1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr1',
    text: 'Respond with the following keys:\n - LEFT KEY if the number was NOT in the sequence.\n - RIGHT KEY if the number WAS in the sequence.\n\nThere will be twelve practice trials in which you will be given feedback. Try to respond as quickly and as accurately as possible.\n\nWhen you are ready to begin press any key.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.07], height: 0.035,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  OK1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, (- 0.32)], size : [0.4, 0.34],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : false, depth : -3.0 
  });
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  fixation = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  presentSet = new visual.TextStim({
    win: psychoJS.window,
    name: 'presentSet',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  presentTarget = new visual.TextStim({
    win: psychoJS.window,
    name: 'presentTarget',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from code
  Corr_count_prac = 0;
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  // Run 'Begin Experiment' code from message
  msg = "";
  
  feedback_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "mainInstruct"
  mainInstructClock = new util.Clock();
  instr2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr2',
    text: 'OK, ready to start the main experiment?\n\nRemember:\n - LEFT CURSOR for NOT in the sequence\n - RIGHT CURSOR for IN the sequence\nTry to respond as quickly and as accurately as possible.\n\nWhen you are ready to proceed press any key.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  OK2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.25)], height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.0, 0.0, 0.0]),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "trial2"
  trial2Clock = new util.Clock();
  fixation2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  presentSet2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'presentSet2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  presentTarget2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'presentTarget2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  resp2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from code2
  Corr_count = 0;
  
  // Initialize components for Routine "feedback2"
  feedback2Clock = new util.Clock();
  // Run 'Begin Experiment' code from message2
  msg = "";
  
  feedback2_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback2_3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "Break_1"
  Break_1Clock = new util.Clock();
  break_msg = new visual.TextStim({
    win: psychoJS.window,
    name: 'break_msg',
    text: 'End of Trial 1.\n\nWhen you are ready to continue the task, press any key.\n\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  OK2_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Break_2"
  Break_2Clock = new util.Clock();
  break_msg_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'break_msg_2',
    text: 'End of Trial 2.\n\nWhen you are ready to continue the task, press any key.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  OK2_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "thanks"
  thanksClock = new util.Clock();
  thanksMsg = new visual.TextStim({
    win: psychoJS.window,
    name: 'thanksMsg',
    text: 'The task has been completed. Thanks for taking part!\nPress any key to exit.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  totalsc = new visual.TextStim({
    win: psychoJS.window,
    name: 'totalsc',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.25)], height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.0, 0.0, 0.0]),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp_allKeys;
var pracInstruct1Components;
function pracInstruct1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'pracInstruct1' ---
    t = 0;
    pracInstruct1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    pracInstruct1Components = [];
    pracInstruct1Components.push(text_2);
    pracInstruct1Components.push(key_resp);
    
    for (const thisComponent of pracInstruct1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function pracInstruct1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'pracInstruct1' ---
    // get current time
    t = pracInstruct1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
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
      let theseKeys = key_resp.getKeys({keyList: [], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of pracInstruct1Components)
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


function pracInstruct1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'pracInstruct1' ---
    for (const thisComponent of pracInstruct1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "pracInstruct1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _OK1_allKeys;
var practInstructComponents;
function practInstructRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practInstruct' ---
    t = 0;
    practInstructClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    OK1.keys = undefined;
    OK1.rt = undefined;
    _OK1_allKeys = [];
    // Run 'Begin Routine' code from code_7
    if ((Corr_count_prac < 300)) {
        continueRoutine = true;
    }
    
    image.setImage('image_rem.jpg');
    // keep track of which components have finished
    practInstructComponents = [];
    practInstructComponents.push(instr1);
    practInstructComponents.push(OK1);
    practInstructComponents.push(image);
    
    for (const thisComponent of practInstructComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function practInstructRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practInstruct' ---
    // get current time
    t = practInstructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr1* updates
    if (t >= 0.0 && instr1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr1.tStart = t;  // (not accounting for frame time here)
      instr1.frameNStart = frameN;  // exact frame index
      
      instr1.setAutoDraw(true);
    }

    
    // *OK1* updates
    if (t >= 0.0 && OK1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      OK1.tStart = t;  // (not accounting for frame time here)
      OK1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { OK1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { OK1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { OK1.clearEvents(); });
    }

    if (OK1.status === PsychoJS.Status.STARTED) {
      let theseKeys = OK1.getKeys({keyList: [], waitRelease: false});
      _OK1_allKeys = _OK1_allKeys.concat(theseKeys);
      if (_OK1_allKeys.length > 0) {
        OK1.keys = _OK1_allKeys[_OK1_allKeys.length - 1].name;  // just the last key pressed
        OK1.rt = _OK1_allKeys[_OK1_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
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
    for (const thisComponent of practInstructComponents)
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


function practInstructRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practInstruct' ---
    for (const thisComponent of practInstructComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(OK1.corr, level);
    }
    psychoJS.experiment.addData('OK1.keys', OK1.keys);
    if (typeof OK1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('OK1.rt', OK1.rt);
        routineTimer.reset();
        }
    
    OK1.stop();
    // the Routine "practInstruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var pracTrials;
function pracTrialsLoopBegin(pracTrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    pracTrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'pracTrials.xlsx',
      seed: undefined, name: 'pracTrials'
    });
    psychoJS.experiment.addLoop(pracTrials); // add the loop to the experiment
    currentLoop = pracTrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPracTrial of pracTrials) {
      snapshot = pracTrials.getSnapshot();
      pracTrialsLoopScheduler.add(importConditions(snapshot));
      pracTrialsLoopScheduler.add(trialRoutineBegin(snapshot));
      pracTrialsLoopScheduler.add(trialRoutineEachFrame());
      pracTrialsLoopScheduler.add(trialRoutineEnd(snapshot));
      pracTrialsLoopScheduler.add(feedbackRoutineBegin(snapshot));
      pracTrialsLoopScheduler.add(feedbackRoutineEachFrame());
      pracTrialsLoopScheduler.add(feedbackRoutineEnd(snapshot));
      pracTrialsLoopScheduler.add(pracTrialsLoopEndIteration(pracTrialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function pracTrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(pracTrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function pracTrialsLoopEndIteration(scheduler, snapshot) {
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


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'mainTrials.xlsx', '2:43'),
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(trial2RoutineBegin(snapshot));
      trialsLoopScheduler.add(trial2RoutineEachFrame());
      trialsLoopScheduler.add(trial2RoutineEnd(snapshot));
      trialsLoopScheduler.add(feedback2RoutineBegin(snapshot));
      trialsLoopScheduler.add(feedback2RoutineEachFrame());
      trialsLoopScheduler.add(feedback2RoutineEnd(snapshot));
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


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'mainTrials.xlsx', '43:85'),
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_2 of trials_2) {
      snapshot = trials_2.getSnapshot();
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(trial2RoutineBegin(snapshot));
      trials_2LoopScheduler.add(trial2RoutineEachFrame());
      trials_2LoopScheduler.add(trial2RoutineEnd(snapshot));
      trials_2LoopScheduler.add(feedback2RoutineBegin(snapshot));
      trials_2LoopScheduler.add(feedback2RoutineEachFrame());
      trials_2LoopScheduler.add(feedback2RoutineEnd(snapshot));
      trials_2LoopScheduler.add(trials_2LoopEndIteration(trials_2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_2LoopEndIteration(scheduler, snapshot) {
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


var trials_3;
function trials_3LoopBegin(trials_3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'mainTrials.xlsx', '85:127'),
      seed: undefined, name: 'trials_3'
    });
    psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
    currentLoop = trials_3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_3 of trials_3) {
      snapshot = trials_3.getSnapshot();
      trials_3LoopScheduler.add(importConditions(snapshot));
      trials_3LoopScheduler.add(trial2RoutineBegin(snapshot));
      trials_3LoopScheduler.add(trial2RoutineEachFrame());
      trials_3LoopScheduler.add(trial2RoutineEnd(snapshot));
      trials_3LoopScheduler.add(feedback2RoutineBegin(snapshot));
      trials_3LoopScheduler.add(feedback2RoutineEachFrame());
      trials_3LoopScheduler.add(feedback2RoutineEnd(snapshot));
      trials_3LoopScheduler.add(trials_3LoopEndIteration(trials_3LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_3LoopEndIteration(scheduler, snapshot) {
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


var _resp_allKeys;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    presentSet.setText(numberSet);
    presentTarget.setText(target);
    resp.keys = undefined;
    resp.rt = undefined;
    _resp_allKeys = [];
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(fixation);
    trialComponents.push(presentSet);
    trialComponents.push(presentTarget);
    trialComponents.push(resp);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation* updates
    if (t >= 0.0 && fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation.tStart = t;  // (not accounting for frame time here)
      fixation.frameNStart = frameN;  // exact frame index
      
      fixation.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation.setAutoDraw(false);
    }
    
    // *presentSet* updates
    if (t >= 1.2 && presentSet.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      presentSet.tStart = t;  // (not accounting for frame time here)
      presentSet.frameNStart = frameN;  // exact frame index
      
      presentSet.setAutoDraw(true);
    }

    frameRemains = 1.2 + 1.7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (presentSet.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      presentSet.setAutoDraw(false);
    }
    
    // *presentTarget* updates
    if (t >= 4.7 && presentTarget.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      presentTarget.tStart = t;  // (not accounting for frame time here)
      presentTarget.frameNStart = frameN;  // exact frame index
      
      presentTarget.setAutoDraw(true);
    }

    frameRemains = 4.7 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (presentTarget.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      presentTarget.setAutoDraw(false);
    }
    
    // *resp* updates
    if (t >= 4.7 && resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp.tStart = t;  // (not accounting for frame time here)
      resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp.clearEvents(); });
    }

    if (resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _resp_allKeys = _resp_allKeys.concat(theseKeys);
      if (_resp_allKeys.length > 0) {
        resp.keys = _resp_allKeys[_resp_allKeys.length - 1].name;  // just the last key pressed
        resp.rt = _resp_allKeys[_resp_allKeys.length - 1].rt;
        // was this correct?
        if (resp.keys == corrAns) {
            resp.corr = 1;
        } else {
            resp.corr = 0;
        }
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
    for (const thisComponent of trialComponents)
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


function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (resp.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         resp.corr = 1;  // correct non-response
      } else {
         resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp.corr, level);
    }
    psychoJS.experiment.addData('resp.keys', resp.keys);
    psychoJS.experiment.addData('resp.corr', resp.corr);
    if (typeof resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp.rt', resp.rt);
        routineTimer.reset();
        }
    
    resp.stop();
    // Run 'End Routine' code from code
    if (resp.corr) {
        Corr_count_prac += 1;
    }
    
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback' ---
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from message
    if (resp.corr) {
        msg = `Correct! RT=${resp.rt}`;
    } else {
        msg = "Oops! That was wrong";
    }
    
    feedback_2.setText(msg);
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(feedback_2);
    
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback' ---
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_2* updates
    if (t >= 0.0 && feedback_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_2.tStart = t;  // (not accounting for frame time here)
      feedback_2.frameNStart = frameN;  // exact frame index
      
      feedback_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedback_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_2.setAutoDraw(false);
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
    for (const thisComponent of feedbackComponents)
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


function feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback' ---
    for (const thisComponent of feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _OK2_allKeys;
var mainInstructComponents;
function mainInstructRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'mainInstruct' ---
    t = 0;
    mainInstructClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    OK2.keys = undefined;
    OK2.rt = undefined;
    _OK2_allKeys = [];
    // Run 'Begin Routine' code from code_2
    if ((Corr_count < 300)) {
        continueRoutine = true;
    }
    
    text.setText((("Practice Accuracy: " + ((Corr_count_prac / 12) * 100).toString()) + "%"));
    // keep track of which components have finished
    mainInstructComponents = [];
    mainInstructComponents.push(instr2);
    mainInstructComponents.push(OK2);
    mainInstructComponents.push(text);
    
    for (const thisComponent of mainInstructComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function mainInstructRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'mainInstruct' ---
    // get current time
    t = mainInstructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr2* updates
    if (t >= 0.0 && instr2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr2.tStart = t;  // (not accounting for frame time here)
      instr2.frameNStart = frameN;  // exact frame index
      
      instr2.setAutoDraw(true);
    }

    
    // *OK2* updates
    if (t >= 0.0 && OK2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      OK2.tStart = t;  // (not accounting for frame time here)
      OK2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { OK2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { OK2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { OK2.clearEvents(); });
    }

    if (OK2.status === PsychoJS.Status.STARTED) {
      let theseKeys = OK2.getKeys({keyList: [], waitRelease: false});
      _OK2_allKeys = _OK2_allKeys.concat(theseKeys);
      if (_OK2_allKeys.length > 0) {
        OK2.keys = _OK2_allKeys[_OK2_allKeys.length - 1].name;  // just the last key pressed
        OK2.rt = _OK2_allKeys[_OK2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
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
    for (const thisComponent of mainInstructComponents)
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


function mainInstructRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'mainInstruct' ---
    for (const thisComponent of mainInstructComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(OK2.corr, level);
    }
    psychoJS.experiment.addData('OK2.keys', OK2.keys);
    if (typeof OK2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('OK2.rt', OK2.rt);
        routineTimer.reset();
        }
    
    OK2.stop();
    // the Routine "mainInstruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _resp2_allKeys;
var trial2Components;
function trial2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial2' ---
    t = 0;
    trial2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    presentSet2.setText(numberSet);
    presentTarget2.setText(target);
    resp2.keys = undefined;
    resp2.rt = undefined;
    _resp2_allKeys = [];
    // keep track of which components have finished
    trial2Components = [];
    trial2Components.push(fixation2);
    trial2Components.push(presentSet2);
    trial2Components.push(presentTarget2);
    trial2Components.push(resp2);
    
    for (const thisComponent of trial2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trial2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial2' ---
    // get current time
    t = trial2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation2* updates
    if (t >= 0.0 && fixation2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation2.tStart = t;  // (not accounting for frame time here)
      fixation2.frameNStart = frameN;  // exact frame index
      
      fixation2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation2.setAutoDraw(false);
    }
    
    // *presentSet2* updates
    if (t >= 1.2 && presentSet2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      presentSet2.tStart = t;  // (not accounting for frame time here)
      presentSet2.frameNStart = frameN;  // exact frame index
      
      presentSet2.setAutoDraw(true);
    }

    frameRemains = 1.2 + 1.7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (presentSet2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      presentSet2.setAutoDraw(false);
    }
    
    // *presentTarget2* updates
    if (t >= 4.7 && presentTarget2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      presentTarget2.tStart = t;  // (not accounting for frame time here)
      presentTarget2.frameNStart = frameN;  // exact frame index
      
      presentTarget2.setAutoDraw(true);
    }

    frameRemains = 4.7 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (presentTarget2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      presentTarget2.setAutoDraw(false);
    }
    
    // *resp2* updates
    if (t >= 4.7 && resp2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp2.tStart = t;  // (not accounting for frame time here)
      resp2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp2.clearEvents(); });
    }

    if (resp2.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp2.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _resp2_allKeys = _resp2_allKeys.concat(theseKeys);
      if (_resp2_allKeys.length > 0) {
        resp2.keys = _resp2_allKeys[_resp2_allKeys.length - 1].name;  // just the last key pressed
        resp2.rt = _resp2_allKeys[_resp2_allKeys.length - 1].rt;
        // was this correct?
        if (resp2.keys == corrAns) {
            resp2.corr = 1;
        } else {
            resp2.corr = 0;
        }
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
    for (const thisComponent of trial2Components)
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


function trial2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial2' ---
    for (const thisComponent of trial2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (resp2.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         resp2.corr = 1;  // correct non-response
      } else {
         resp2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp2.corr, level);
    }
    psychoJS.experiment.addData('resp2.keys', resp2.keys);
    psychoJS.experiment.addData('resp2.corr', resp2.corr);
    if (typeof resp2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp2.rt', resp2.rt);
        routineTimer.reset();
        }
    
    resp2.stop();
    // Run 'End Routine' code from code2
    if (resp2.corr) {
        Corr_count += 1;
    }
    
    // the Routine "trial2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback2Components;
function feedback2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback2' ---
    t = 0;
    feedback2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from message2
    if (resp2.corr) {
        msg = `Correct! RT=${resp2.rt}`;
    } else {
        msg = "Oops! That was wrong";
    }
    
    feedback2_3.setText(msg);
    // keep track of which components have finished
    feedback2Components = [];
    feedback2Components.push(feedback2_3);
    
    for (const thisComponent of feedback2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback2' ---
    // get current time
    t = feedback2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback2_3* updates
    if (t >= 0.0 && feedback2_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback2_3.tStart = t;  // (not accounting for frame time here)
      feedback2_3.frameNStart = frameN;  // exact frame index
      
      feedback2_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedback2_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback2_3.setAutoDraw(false);
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
    for (const thisComponent of feedback2Components)
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


function feedback2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback2' ---
    for (const thisComponent of feedback2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _OK2_2_allKeys;
var Break_1Components;
function Break_1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Break_1' ---
    t = 0;
    Break_1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    OK2_2.keys = undefined;
    OK2_2.rt = undefined;
    _OK2_2_allKeys = [];
    // keep track of which components have finished
    Break_1Components = [];
    Break_1Components.push(break_msg);
    Break_1Components.push(OK2_2);
    
    for (const thisComponent of Break_1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Break_1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Break_1' ---
    // get current time
    t = Break_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *break_msg* updates
    if (t >= 0.0 && break_msg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      break_msg.tStart = t;  // (not accounting for frame time here)
      break_msg.frameNStart = frameN;  // exact frame index
      
      break_msg.setAutoDraw(true);
    }

    
    // *OK2_2* updates
    if (t >= 0.0 && OK2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      OK2_2.tStart = t;  // (not accounting for frame time here)
      OK2_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { OK2_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { OK2_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { OK2_2.clearEvents(); });
    }

    if (OK2_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = OK2_2.getKeys({keyList: [], waitRelease: false});
      _OK2_2_allKeys = _OK2_2_allKeys.concat(theseKeys);
      if (_OK2_2_allKeys.length > 0) {
        OK2_2.keys = _OK2_2_allKeys[_OK2_2_allKeys.length - 1].name;  // just the last key pressed
        OK2_2.rt = _OK2_2_allKeys[_OK2_2_allKeys.length - 1].rt;
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
    for (const thisComponent of Break_1Components)
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


function Break_1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Break_1' ---
    for (const thisComponent of Break_1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(OK2_2.corr, level);
    }
    psychoJS.experiment.addData('OK2_2.keys', OK2_2.keys);
    if (typeof OK2_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('OK2_2.rt', OK2_2.rt);
        routineTimer.reset();
        }
    
    OK2_2.stop();
    // the Routine "Break_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _OK2_3_allKeys;
var Break_2Components;
function Break_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Break_2' ---
    t = 0;
    Break_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_6
    if ((Corr_count < 300)) {
        continueRoutine = true;
    }
    
    OK2_3.keys = undefined;
    OK2_3.rt = undefined;
    _OK2_3_allKeys = [];
    // keep track of which components have finished
    Break_2Components = [];
    Break_2Components.push(break_msg_2);
    Break_2Components.push(OK2_3);
    
    for (const thisComponent of Break_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Break_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Break_2' ---
    // get current time
    t = Break_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *break_msg_2* updates
    if (t >= 0.0 && break_msg_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      break_msg_2.tStart = t;  // (not accounting for frame time here)
      break_msg_2.frameNStart = frameN;  // exact frame index
      
      break_msg_2.setAutoDraw(true);
    }

    
    // *OK2_3* updates
    if (t >= 0.0 && OK2_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      OK2_3.tStart = t;  // (not accounting for frame time here)
      OK2_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { OK2_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { OK2_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { OK2_3.clearEvents(); });
    }

    if (OK2_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = OK2_3.getKeys({keyList: [], waitRelease: false});
      _OK2_3_allKeys = _OK2_3_allKeys.concat(theseKeys);
      if (_OK2_3_allKeys.length > 0) {
        OK2_3.keys = _OK2_3_allKeys[_OK2_3_allKeys.length - 1].name;  // just the last key pressed
        OK2_3.rt = _OK2_3_allKeys[_OK2_3_allKeys.length - 1].rt;
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
    for (const thisComponent of Break_2Components)
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


function Break_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Break_2' ---
    for (const thisComponent of Break_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(OK2_3.corr, level);
    }
    psychoJS.experiment.addData('OK2_3.keys', OK2_3.keys);
    if (typeof OK2_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('OK2_3.rt', OK2_3.rt);
        routineTimer.reset();
        }
    
    OK2_3.stop();
    // the Routine "Break_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_2_allKeys;
var thanksComponents;
function thanksRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'thanks' ---
    t = 0;
    thanksClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    totalsc.setText((("Accuracy: " + ((Corr_count / 126) * 100).toString()) + "%"));
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    thanksComponents = [];
    thanksComponents.push(thanksMsg);
    thanksComponents.push(totalsc);
    thanksComponents.push(key_resp_2);
    
    for (const thisComponent of thanksComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function thanksRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'thanks' ---
    // get current time
    t = thanksClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *thanksMsg* updates
    if (t >= 0.0 && thanksMsg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      thanksMsg.tStart = t;  // (not accounting for frame time here)
      thanksMsg.frameNStart = frameN;  // exact frame index
      
      thanksMsg.setAutoDraw(true);
    }

    
    // *totalsc* updates
    if (t >= 0.0 && totalsc.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      totalsc.tStart = t;  // (not accounting for frame time here)
      totalsc.frameNStart = frameN;  // exact frame index
      
      totalsc.setAutoDraw(true);
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
      let theseKeys = key_resp_2.getKeys({keyList: [], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
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
    for (const thisComponent of thanksComponents)
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


function thanksRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'thanks' ---
    for (const thisComponent of thanksComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "thanks" was not non-slip safe, so reset the non-slip timer
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
