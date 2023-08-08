#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Wed Aug  2 08:47:25 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.2.5')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'sternberg'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '02',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/overbydl/Desktop/sternberg2/sternberg_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[2240, 1260], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='event')

# --- Initialize components for Routine "pracInstruct1" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='In this experiment you will be presented with a sequence of between 1 and 6 randomly ordered numbers.\n\nFollowing a short delay you will then be presented with a single number and you will have to decide whether this new number was a member of the sequence.\n\nPress any key to continue.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "practInstruct" ---
instr1 = visual.TextStim(win=win, name='instr1',
    text='Respond with the following keys:\n - LEFT KEY if the number was NOT in the sequence.\n - RIGHT KEY if the number WAS in the sequence.\n\nThere will be twelve practice trials in which you will be given feedback. Try to respond as quickly and as accurately as possible.\n\nWhen you are ready to begin press any key.',
    font='Arial',
    pos=[0, 0.07], height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
OK1 = keyboard.Keyboard()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.32), size=(0.4, 0.34),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-3.0)

# --- Initialize components for Routine "trial" ---
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
presentSet = visual.TextStim(win=win, name='presentSet',
    text='',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
presentTarget = visual.TextStim(win=win, name='presentTarget',
    text='',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
resp = keyboard.Keyboard()
# Run 'Begin Experiment' code from code
Corr_count_prac =0


# --- Initialize components for Routine "feedback" ---
# Run 'Begin Experiment' code from message
#msg variable just needs some value at start
msg=''
feedback_2 = visual.TextStim(win=win, name='feedback_2',
    text='',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "mainInstruct" ---
instr2 = visual.TextStim(win=win, name='instr2',
    text='OK, ready to start the main experiment?\n\nRemember:\n - LEFT CURSOR for NOT in the sequence\n - RIGHT CURSOR for IN the sequence\nTry to respond as quickly and as accurately as possible.\n\nWhen you are ready to proceed press any key.',
    font='Arial',
    pos=[0, 0], height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
OK2 = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Arial',
    pos=(0,-0.25), height=0.025, wrapWidth=None, ori=0.0, 
    color=[0.0000, 0.0000, 0.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "trial2" ---
fixation2 = visual.TextStim(win=win, name='fixation2',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
presentSet2 = visual.TextStim(win=win, name='presentSet2',
    text='',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
presentTarget2 = visual.TextStim(win=win, name='presentTarget2',
    text='',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
resp2 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code2
Corr_count =0


# --- Initialize components for Routine "feedback2" ---
# Run 'Begin Experiment' code from message2
#msg variable just needs some value at start
msg=''
feedback2_3 = visual.TextStim(win=win, name='feedback2_3',
    text='',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Break_1" ---
break_msg = visual.TextStim(win=win, name='break_msg',
    text='End of Trial 1.\n\nWhen you are ready to continue the task, press any key.\n\n',
    font='Arial',
    pos=[0, 0], height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
OK2_2 = keyboard.Keyboard()

# --- Initialize components for Routine "trial2" ---
fixation2 = visual.TextStim(win=win, name='fixation2',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
presentSet2 = visual.TextStim(win=win, name='presentSet2',
    text='',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
presentTarget2 = visual.TextStim(win=win, name='presentTarget2',
    text='',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
resp2 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code2
Corr_count =0


# --- Initialize components for Routine "feedback2" ---
# Run 'Begin Experiment' code from message2
#msg variable just needs some value at start
msg=''
feedback2_3 = visual.TextStim(win=win, name='feedback2_3',
    text='',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Break_2" ---
break_msg_2 = visual.TextStim(win=win, name='break_msg_2',
    text='End of Trial 2.\n\nWhen you are ready to continue the task, press any key.',
    font='Arial',
    pos=[0, 0], height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
OK2_3 = keyboard.Keyboard()

# --- Initialize components for Routine "trial2" ---
fixation2 = visual.TextStim(win=win, name='fixation2',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
presentSet2 = visual.TextStim(win=win, name='presentSet2',
    text='',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
presentTarget2 = visual.TextStim(win=win, name='presentTarget2',
    text='',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
resp2 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code2
Corr_count =0


# --- Initialize components for Routine "feedback2" ---
# Run 'Begin Experiment' code from message2
#msg variable just needs some value at start
msg=''
feedback2_3 = visual.TextStim(win=win, name='feedback2_3',
    text='',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "thanks" ---
thanksMsg = visual.TextStim(win=win, name='thanksMsg',
    text='The task has been completed. Thanks for taking part!\nPress any key to exit.',
    font='Arial',
    pos=[0, 0], height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
totalsc = visual.TextStim(win=win, name='totalsc',
    text='',
    font='Arial',
    pos=(0,-0.25), height=0.025, wrapWidth=None, ori=0.0, 
    color=[0.0000, 0.0000, 0.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "pracInstruct1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
pracInstruct1Components = [text_2, key_resp]
for thisComponent in pracInstruct1Components:
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

# --- Run Routine "pracInstruct1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_2.started')
        text_2.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=None, waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pracInstruct1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "pracInstruct1" ---
for thisComponent in pracInstruct1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "pracInstruct1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "practInstruct" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
OK1.keys = []
OK1.rt = []
_OK1_allKeys = []
# Run 'Begin Routine' code from code_7
if Corr_count_prac <300:
    continueRoutine = True

image.setImage('image_rem.jpg')
# keep track of which components have finished
practInstructComponents = [instr1, OK1, image]
for thisComponent in practInstructComponents:
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

# --- Run Routine "practInstruct" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr1* updates
    if instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr1.frameNStart = frameN  # exact frame index
        instr1.tStart = t  # local t and not account for scr refresh
        instr1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr1.started')
        instr1.setAutoDraw(True)
    
    # *OK1* updates
    waitOnFlip = False
    if OK1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        OK1.frameNStart = frameN  # exact frame index
        OK1.tStart = t  # local t and not account for scr refresh
        OK1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OK1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'OK1.started')
        OK1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(OK1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(OK1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if OK1.status == STARTED and not waitOnFlip:
        theseKeys = OK1.getKeys(keyList=None, waitRelease=False)
        _OK1_allKeys.extend(theseKeys)
        if len(_OK1_allKeys):
            OK1.keys = _OK1_allKeys[-1].name  # just the last key pressed
            OK1.rt = _OK1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image.started')
        image.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practInstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "practInstruct" ---
for thisComponent in practInstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if OK1.keys in ['', [], None]:  # No response was made
    OK1.keys = None
thisExp.addData('OK1.keys',OK1.keys)
if OK1.keys != None:  # we had a response
    thisExp.addData('OK1.rt', OK1.rt)
thisExp.nextEntry()
# the Routine "practInstruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pracTrials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pracTrials.xlsx'),
    seed=None, name='pracTrials')
thisExp.addLoop(pracTrials)  # add the loop to the experiment
thisPracTrial = pracTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracTrial.rgb)
if thisPracTrial != None:
    for paramName in thisPracTrial:
        exec('{} = thisPracTrial[paramName]'.format(paramName))

for thisPracTrial in pracTrials:
    currentLoop = pracTrials
    # abbreviate parameter names if possible (e.g. rgb = thisPracTrial.rgb)
    if thisPracTrial != None:
        for paramName in thisPracTrial:
            exec('{} = thisPracTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    presentSet.setText(numberSet)
    presentTarget.setText(target)
    resp.keys = []
    resp.rt = []
    _resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [fixation, presentSet, presentTarget, resp]
    for thisComponent in trialComponents:
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
    
    # --- Run Routine "trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation.started')
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.stopped')
                fixation.setAutoDraw(False)
        
        # *presentSet* updates
        if presentSet.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
            # keep track of start time/frame for later
            presentSet.frameNStart = frameN  # exact frame index
            presentSet.tStart = t  # local t and not account for scr refresh
            presentSet.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(presentSet, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'presentSet.started')
            presentSet.setAutoDraw(True)
        if presentSet.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > presentSet.tStartRefresh + 1.7-frameTolerance:
                # keep track of stop time/frame for later
                presentSet.tStop = t  # not accounting for scr refresh
                presentSet.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'presentSet.stopped')
                presentSet.setAutoDraw(False)
        
        # *presentTarget* updates
        if presentTarget.status == NOT_STARTED and tThisFlip >= 4.7-frameTolerance:
            # keep track of start time/frame for later
            presentTarget.frameNStart = frameN  # exact frame index
            presentTarget.tStart = t  # local t and not account for scr refresh
            presentTarget.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(presentTarget, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'presentTarget.started')
            presentTarget.setAutoDraw(True)
        if presentTarget.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > presentTarget.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                presentTarget.tStop = t  # not accounting for scr refresh
                presentTarget.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'presentTarget.stopped')
                presentTarget.setAutoDraw(False)
        
        # *resp* updates
        waitOnFlip = False
        if resp.status == NOT_STARTED and tThisFlip >= 4.7-frameTolerance:
            # keep track of start time/frame for later
            resp.frameNStart = frameN  # exact frame index
            resp.tStart = t  # local t and not account for scr refresh
            resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resp.started')
            resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp.status == STARTED and not waitOnFlip:
            theseKeys = resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _resp_allKeys.extend(theseKeys)
            if len(_resp_allKeys):
                resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                resp.rt = _resp_allKeys[-1].rt
                # was this correct?
                if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           resp.corr = 1;  # correct non-response
        else:
           resp.corr = 0;  # failed to respond (incorrectly)
    # store data for pracTrials (TrialHandler)
    pracTrials.addData('resp.keys',resp.keys)
    pracTrials.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        pracTrials.addData('resp.rt', resp.rt)
    # Run 'End Routine' code from code
    if resp.corr:
        Corr_count_prac +=1
       
        
        
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from message
    if resp.corr:#stored on last run routine
      msg="Correct! RT=%.3f" %(resp.rt)
     
    else:
      msg="Oops! That was wrong"
     
    feedback_2.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [feedback_2]
    for thisComponent in feedbackComponents:
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
    
    # --- Run Routine "feedback" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_2* updates
        if feedback_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_2.frameNStart = frameN  # exact frame index
            feedback_2.tStart = t  # local t and not account for scr refresh
            feedback_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_2.started')
            feedback_2.setAutoDraw(True)
        if feedback_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                feedback_2.tStop = t  # not accounting for scr refresh
                feedback_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_2.stopped')
                feedback_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'pracTrials'

# get names of stimulus parameters
if pracTrials.trialList in ([], [None], None):
    params = []
else:
    params = pracTrials.trialList[0].keys()
# save data for this loop
pracTrials.saveAsExcel(filename + '.xlsx', sheetName='pracTrials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "mainInstruct" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
OK2.keys = []
OK2.rt = []
_OK2_allKeys = []
# Run 'Begin Routine' code from code_2
if Corr_count <300:
    continueRoutine = True

text.setText('Practice Accuracy: ' + str((Corr_count_prac/12)*100) + '%')
# keep track of which components have finished
mainInstructComponents = [instr2, OK2, text]
for thisComponent in mainInstructComponents:
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

# --- Run Routine "mainInstruct" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr2* updates
    if instr2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr2.frameNStart = frameN  # exact frame index
        instr2.tStart = t  # local t and not account for scr refresh
        instr2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr2.started')
        instr2.setAutoDraw(True)
    
    # *OK2* updates
    waitOnFlip = False
    if OK2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        OK2.frameNStart = frameN  # exact frame index
        OK2.tStart = t  # local t and not account for scr refresh
        OK2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OK2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'OK2.started')
        OK2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(OK2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(OK2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if OK2.status == STARTED and not waitOnFlip:
        theseKeys = OK2.getKeys(keyList=None, waitRelease=False)
        _OK2_allKeys.extend(theseKeys)
        if len(_OK2_allKeys):
            OK2.keys = _OK2_allKeys[-1].name  # just the last key pressed
            OK2.rt = _OK2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mainInstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "mainInstruct" ---
for thisComponent in mainInstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if OK2.keys in ['', [], None]:  # No response was made
    OK2.keys = None
thisExp.addData('OK2.keys',OK2.keys)
if OK2.keys != None:  # we had a response
    thisExp.addData('OK2.rt', OK2.rt)
thisExp.nextEntry()
# the Routine "mainInstruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('mainTrials.xlsx', selection='2:43'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    presentSet2.setText(numberSet)
    presentTarget2.setText(target)
    resp2.keys = []
    resp2.rt = []
    _resp2_allKeys = []
    # keep track of which components have finished
    trial2Components = [fixation2, presentSet2, presentTarget2, resp2]
    for thisComponent in trial2Components:
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
    
    # --- Run Routine "trial2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation2* updates
        if fixation2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation2.frameNStart = frameN  # exact frame index
            fixation2.tStart = t  # local t and not account for scr refresh
            fixation2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation2.started')
            fixation2.setAutoDraw(True)
        if fixation2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation2.tStop = t  # not accounting for scr refresh
                fixation2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation2.stopped')
                fixation2.setAutoDraw(False)
        
        # *presentSet2* updates
        if presentSet2.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
            # keep track of start time/frame for later
            presentSet2.frameNStart = frameN  # exact frame index
            presentSet2.tStart = t  # local t and not account for scr refresh
            presentSet2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(presentSet2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'presentSet2.started')
            presentSet2.setAutoDraw(True)
        if presentSet2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > presentSet2.tStartRefresh + 1.7-frameTolerance:
                # keep track of stop time/frame for later
                presentSet2.tStop = t  # not accounting for scr refresh
                presentSet2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'presentSet2.stopped')
                presentSet2.setAutoDraw(False)
        
        # *presentTarget2* updates
        if presentTarget2.status == NOT_STARTED and tThisFlip >= 4.7-frameTolerance:
            # keep track of start time/frame for later
            presentTarget2.frameNStart = frameN  # exact frame index
            presentTarget2.tStart = t  # local t and not account for scr refresh
            presentTarget2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(presentTarget2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'presentTarget2.started')
            presentTarget2.setAutoDraw(True)
        if presentTarget2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > presentTarget2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                presentTarget2.tStop = t  # not accounting for scr refresh
                presentTarget2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'presentTarget2.stopped')
                presentTarget2.setAutoDraw(False)
        
        # *resp2* updates
        waitOnFlip = False
        if resp2.status == NOT_STARTED and tThisFlip >= 4.7-frameTolerance:
            # keep track of start time/frame for later
            resp2.frameNStart = frameN  # exact frame index
            resp2.tStart = t  # local t and not account for scr refresh
            resp2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resp2.started')
            resp2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp2.status == STARTED and not waitOnFlip:
            theseKeys = resp2.getKeys(keyList=['left', 'right'], waitRelease=False)
            _resp2_allKeys.extend(theseKeys)
            if len(_resp2_allKeys):
                resp2.keys = _resp2_allKeys[-1].name  # just the last key pressed
                resp2.rt = _resp2_allKeys[-1].rt
                # was this correct?
                if (resp2.keys == str(corrAns)) or (resp2.keys == corrAns):
                    resp2.corr = 1
                else:
                    resp2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial2" ---
    for thisComponent in trial2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp2.keys in ['', [], None]:  # No response was made
        resp2.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           resp2.corr = 1;  # correct non-response
        else:
           resp2.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('resp2.keys',resp2.keys)
    trials.addData('resp2.corr', resp2.corr)
    if resp2.keys != None:  # we had a response
        trials.addData('resp2.rt', resp2.rt)
    # Run 'End Routine' code from code2
    if resp2.corr:
        Corr_count +=1
       
        
        
    # the Routine "trial2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from message2
    if resp2.corr:#stored on last run routine
      msg="Correct! RT=%.3f" %(resp2.rt)
     
    else:
      msg="Oops! That was wrong"
     
    feedback2_3.setText(msg)
    # keep track of which components have finished
    feedback2Components = [feedback2_3]
    for thisComponent in feedback2Components:
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
    
    # --- Run Routine "feedback2" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback2_3* updates
        if feedback2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback2_3.frameNStart = frameN  # exact frame index
            feedback2_3.tStart = t  # local t and not account for scr refresh
            feedback2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback2_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback2_3.started')
            feedback2_3.setAutoDraw(True)
        if feedback2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback2_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                feedback2_3.tStop = t  # not accounting for scr refresh
                feedback2_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback2_3.stopped')
                feedback2_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback2" ---
    for thisComponent in feedback2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "Break_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
OK2_2.keys = []
OK2_2.rt = []
_OK2_2_allKeys = []
# keep track of which components have finished
Break_1Components = [break_msg, OK2_2]
for thisComponent in Break_1Components:
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

# --- Run Routine "Break_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *break_msg* updates
    if break_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        break_msg.frameNStart = frameN  # exact frame index
        break_msg.tStart = t  # local t and not account for scr refresh
        break_msg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break_msg, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'break_msg.started')
        break_msg.setAutoDraw(True)
    
    # *OK2_2* updates
    waitOnFlip = False
    if OK2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        OK2_2.frameNStart = frameN  # exact frame index
        OK2_2.tStart = t  # local t and not account for scr refresh
        OK2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OK2_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'OK2_2.started')
        OK2_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(OK2_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(OK2_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if OK2_2.status == STARTED and not waitOnFlip:
        theseKeys = OK2_2.getKeys(keyList=None, waitRelease=False)
        _OK2_2_allKeys.extend(theseKeys)
        if len(_OK2_2_allKeys):
            OK2_2.keys = _OK2_2_allKeys[-1].name  # just the last key pressed
            OK2_2.rt = _OK2_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Break_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Break_1" ---
for thisComponent in Break_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if OK2_2.keys in ['', [], None]:  # No response was made
    OK2_2.keys = None
thisExp.addData('OK2_2.keys',OK2_2.keys)
if OK2_2.keys != None:  # we had a response
    thisExp.addData('OK2_2.rt', OK2_2.rt)
thisExp.nextEntry()
# the Routine "Break_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('mainTrials.xlsx', selection='43:85'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    presentSet2.setText(numberSet)
    presentTarget2.setText(target)
    resp2.keys = []
    resp2.rt = []
    _resp2_allKeys = []
    # keep track of which components have finished
    trial2Components = [fixation2, presentSet2, presentTarget2, resp2]
    for thisComponent in trial2Components:
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
    
    # --- Run Routine "trial2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation2* updates
        if fixation2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation2.frameNStart = frameN  # exact frame index
            fixation2.tStart = t  # local t and not account for scr refresh
            fixation2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation2.started')
            fixation2.setAutoDraw(True)
        if fixation2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation2.tStop = t  # not accounting for scr refresh
                fixation2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation2.stopped')
                fixation2.setAutoDraw(False)
        
        # *presentSet2* updates
        if presentSet2.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
            # keep track of start time/frame for later
            presentSet2.frameNStart = frameN  # exact frame index
            presentSet2.tStart = t  # local t and not account for scr refresh
            presentSet2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(presentSet2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'presentSet2.started')
            presentSet2.setAutoDraw(True)
        if presentSet2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > presentSet2.tStartRefresh + 1.7-frameTolerance:
                # keep track of stop time/frame for later
                presentSet2.tStop = t  # not accounting for scr refresh
                presentSet2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'presentSet2.stopped')
                presentSet2.setAutoDraw(False)
        
        # *presentTarget2* updates
        if presentTarget2.status == NOT_STARTED and tThisFlip >= 4.7-frameTolerance:
            # keep track of start time/frame for later
            presentTarget2.frameNStart = frameN  # exact frame index
            presentTarget2.tStart = t  # local t and not account for scr refresh
            presentTarget2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(presentTarget2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'presentTarget2.started')
            presentTarget2.setAutoDraw(True)
        if presentTarget2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > presentTarget2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                presentTarget2.tStop = t  # not accounting for scr refresh
                presentTarget2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'presentTarget2.stopped')
                presentTarget2.setAutoDraw(False)
        
        # *resp2* updates
        waitOnFlip = False
        if resp2.status == NOT_STARTED and tThisFlip >= 4.7-frameTolerance:
            # keep track of start time/frame for later
            resp2.frameNStart = frameN  # exact frame index
            resp2.tStart = t  # local t and not account for scr refresh
            resp2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resp2.started')
            resp2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp2.status == STARTED and not waitOnFlip:
            theseKeys = resp2.getKeys(keyList=['left', 'right'], waitRelease=False)
            _resp2_allKeys.extend(theseKeys)
            if len(_resp2_allKeys):
                resp2.keys = _resp2_allKeys[-1].name  # just the last key pressed
                resp2.rt = _resp2_allKeys[-1].rt
                # was this correct?
                if (resp2.keys == str(corrAns)) or (resp2.keys == corrAns):
                    resp2.corr = 1
                else:
                    resp2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial2" ---
    for thisComponent in trial2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp2.keys in ['', [], None]:  # No response was made
        resp2.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           resp2.corr = 1;  # correct non-response
        else:
           resp2.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('resp2.keys',resp2.keys)
    trials_2.addData('resp2.corr', resp2.corr)
    if resp2.keys != None:  # we had a response
        trials_2.addData('resp2.rt', resp2.rt)
    # Run 'End Routine' code from code2
    if resp2.corr:
        Corr_count +=1
       
        
        
    # the Routine "trial2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from message2
    if resp2.corr:#stored on last run routine
      msg="Correct! RT=%.3f" %(resp2.rt)
     
    else:
      msg="Oops! That was wrong"
     
    feedback2_3.setText(msg)
    # keep track of which components have finished
    feedback2Components = [feedback2_3]
    for thisComponent in feedback2Components:
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
    
    # --- Run Routine "feedback2" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback2_3* updates
        if feedback2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback2_3.frameNStart = frameN  # exact frame index
            feedback2_3.tStart = t  # local t and not account for scr refresh
            feedback2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback2_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback2_3.started')
            feedback2_3.setAutoDraw(True)
        if feedback2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback2_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                feedback2_3.tStop = t  # not accounting for scr refresh
                feedback2_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback2_3.stopped')
                feedback2_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback2" ---
    for thisComponent in feedback2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'

# get names of stimulus parameters
if trials_2.trialList in ([], [None], None):
    params = []
else:
    params = trials_2.trialList[0].keys()
# save data for this loop
trials_2.saveAsExcel(filename + '.xlsx', sheetName='trials_2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "Break_2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_6
if Corr_count <300:
    continueRoutine = True

OK2_3.keys = []
OK2_3.rt = []
_OK2_3_allKeys = []
# keep track of which components have finished
Break_2Components = [break_msg_2, OK2_3]
for thisComponent in Break_2Components:
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

# --- Run Routine "Break_2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *break_msg_2* updates
    if break_msg_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        break_msg_2.frameNStart = frameN  # exact frame index
        break_msg_2.tStart = t  # local t and not account for scr refresh
        break_msg_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break_msg_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'break_msg_2.started')
        break_msg_2.setAutoDraw(True)
    
    # *OK2_3* updates
    waitOnFlip = False
    if OK2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        OK2_3.frameNStart = frameN  # exact frame index
        OK2_3.tStart = t  # local t and not account for scr refresh
        OK2_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OK2_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'OK2_3.started')
        OK2_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(OK2_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(OK2_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if OK2_3.status == STARTED and not waitOnFlip:
        theseKeys = OK2_3.getKeys(keyList=None, waitRelease=False)
        _OK2_3_allKeys.extend(theseKeys)
        if len(_OK2_3_allKeys):
            OK2_3.keys = _OK2_3_allKeys[-1].name  # just the last key pressed
            OK2_3.rt = _OK2_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Break_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Break_2" ---
for thisComponent in Break_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if OK2_3.keys in ['', [], None]:  # No response was made
    OK2_3.keys = None
thisExp.addData('OK2_3.keys',OK2_3.keys)
if OK2_3.keys != None:  # we had a response
    thisExp.addData('OK2_3.rt', OK2_3.rt)
thisExp.nextEntry()
# the Routine "Break_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('mainTrials.xlsx', selection='85:127'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    presentSet2.setText(numberSet)
    presentTarget2.setText(target)
    resp2.keys = []
    resp2.rt = []
    _resp2_allKeys = []
    # keep track of which components have finished
    trial2Components = [fixation2, presentSet2, presentTarget2, resp2]
    for thisComponent in trial2Components:
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
    
    # --- Run Routine "trial2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation2* updates
        if fixation2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation2.frameNStart = frameN  # exact frame index
            fixation2.tStart = t  # local t and not account for scr refresh
            fixation2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation2.started')
            fixation2.setAutoDraw(True)
        if fixation2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation2.tStop = t  # not accounting for scr refresh
                fixation2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation2.stopped')
                fixation2.setAutoDraw(False)
        
        # *presentSet2* updates
        if presentSet2.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
            # keep track of start time/frame for later
            presentSet2.frameNStart = frameN  # exact frame index
            presentSet2.tStart = t  # local t and not account for scr refresh
            presentSet2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(presentSet2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'presentSet2.started')
            presentSet2.setAutoDraw(True)
        if presentSet2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > presentSet2.tStartRefresh + 1.7-frameTolerance:
                # keep track of stop time/frame for later
                presentSet2.tStop = t  # not accounting for scr refresh
                presentSet2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'presentSet2.stopped')
                presentSet2.setAutoDraw(False)
        
        # *presentTarget2* updates
        if presentTarget2.status == NOT_STARTED and tThisFlip >= 4.7-frameTolerance:
            # keep track of start time/frame for later
            presentTarget2.frameNStart = frameN  # exact frame index
            presentTarget2.tStart = t  # local t and not account for scr refresh
            presentTarget2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(presentTarget2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'presentTarget2.started')
            presentTarget2.setAutoDraw(True)
        if presentTarget2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > presentTarget2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                presentTarget2.tStop = t  # not accounting for scr refresh
                presentTarget2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'presentTarget2.stopped')
                presentTarget2.setAutoDraw(False)
        
        # *resp2* updates
        waitOnFlip = False
        if resp2.status == NOT_STARTED and tThisFlip >= 4.7-frameTolerance:
            # keep track of start time/frame for later
            resp2.frameNStart = frameN  # exact frame index
            resp2.tStart = t  # local t and not account for scr refresh
            resp2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resp2.started')
            resp2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp2.status == STARTED and not waitOnFlip:
            theseKeys = resp2.getKeys(keyList=['left', 'right'], waitRelease=False)
            _resp2_allKeys.extend(theseKeys)
            if len(_resp2_allKeys):
                resp2.keys = _resp2_allKeys[-1].name  # just the last key pressed
                resp2.rt = _resp2_allKeys[-1].rt
                # was this correct?
                if (resp2.keys == str(corrAns)) or (resp2.keys == corrAns):
                    resp2.corr = 1
                else:
                    resp2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial2" ---
    for thisComponent in trial2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp2.keys in ['', [], None]:  # No response was made
        resp2.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           resp2.corr = 1;  # correct non-response
        else:
           resp2.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('resp2.keys',resp2.keys)
    trials_3.addData('resp2.corr', resp2.corr)
    if resp2.keys != None:  # we had a response
        trials_3.addData('resp2.rt', resp2.rt)
    # Run 'End Routine' code from code2
    if resp2.corr:
        Corr_count +=1
       
        
        
    # the Routine "trial2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from message2
    if resp2.corr:#stored on last run routine
      msg="Correct! RT=%.3f" %(resp2.rt)
     
    else:
      msg="Oops! That was wrong"
     
    feedback2_3.setText(msg)
    # keep track of which components have finished
    feedback2Components = [feedback2_3]
    for thisComponent in feedback2Components:
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
    
    # --- Run Routine "feedback2" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback2_3* updates
        if feedback2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback2_3.frameNStart = frameN  # exact frame index
            feedback2_3.tStart = t  # local t and not account for scr refresh
            feedback2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback2_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback2_3.started')
            feedback2_3.setAutoDraw(True)
        if feedback2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback2_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                feedback2_3.tStop = t  # not accounting for scr refresh
                feedback2_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback2_3.stopped')
                feedback2_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback2" ---
    for thisComponent in feedback2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_3'

# get names of stimulus parameters
if trials_3.trialList in ([], [None], None):
    params = []
else:
    params = trials_3.trialList[0].keys()
# save data for this loop
trials_3.saveAsExcel(filename + '.xlsx', sheetName='trials_3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "thanks" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
totalsc.setText('Accuracy: ' + str((Corr_count/126)*100) + '%')
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
thanksComponents = [thanksMsg, totalsc, key_resp_2]
for thisComponent in thanksComponents:
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

# --- Run Routine "thanks" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanksMsg* updates
    if thanksMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanksMsg.frameNStart = frameN  # exact frame index
        thanksMsg.tStart = t  # local t and not account for scr refresh
        thanksMsg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanksMsg, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'thanksMsg.started')
        thanksMsg.setAutoDraw(True)
    
    # *totalsc* updates
    if totalsc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        totalsc.frameNStart = frameN  # exact frame index
        totalsc.tStart = t  # local t and not account for scr refresh
        totalsc.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(totalsc, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'totalsc.started')
        totalsc.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_2.started')
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=None, waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "thanks" ---
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "thanks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
