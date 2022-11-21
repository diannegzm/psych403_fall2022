from psychopy import core, gui, visual, monitors, event
from datetime import datetime
import os
os.chdir('/Applications/PsychoPy.app/Contents/Resources/psychopy')

import numpy as np

#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
exp_info = {'subject_nr':0, 
            'age':0, 
            'handedness':('right','left','ambi'), 
            'gender':0,
            'session': 1}

print(exp_info)
print('All variables have been created! Now ready to show the dialog box!')

my_dlg = gui.DlgFromDict(dictionary=exp_info, 
        title = "subject info", 
        fixed = ['session'],
        order = ['session', 'subject_nr', 'age', 'gender', 'handedness'])

#get date and time
date = datetime.now()
print(date)

exp_info['date'] = str(date.hour) + '-' + str(date.day) + '/' + str(date.month) + '/' + str(date.year)
print(exp_info['date'])

#-create a unique filename for the data
filename = str(exp_info['subject_nr']) + '_' + exp_info['date'] + '.csv'
print(filename)

main_dir = os.getcwd()
sub_dir = os.path.join(main_dir,'sub_info',filename)

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width=30.41, distance=60) 
mon.setSizePix([1440,900])
mon.save()

#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, size=(800,800), color=[-1,-1,-1])

#-define experiment start text using psychopy functions

nBlocks = 2
nTrials = 3

start_msg = "Welcome to my experiment!" #(message not showing, look at it later)

#-define block (start)/end text using psychopy functions
block_msg = "Press any key to continue to the next block"
end_trial_msg = "End of trial"

#-define stimuli using psychopy functions (images, fixation cross)
fix_text = visual.TextStim(win, text = '+')
my_image = visual.ImageStim(win)
main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')
stims = ['face01.jpg', 'face02.jpg', 'face03.jpg']

#=====================
#START EXPERIMENT
#=====================
#-present start message text
start_text = visual.TextStim(win, text=start_msg)

#-allow participant to begin experiment with button press
start_text.draw()
win.flip()
event.waitKeys()

blockTimer = core.Clock()
trialTimer = core.Clock()
stimTimer = core.Clock()
respTimer = core.Clock()

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks
for block in range(nBlocks):
    #-present block start message
    blockTimer.reset()
    blockStart = blockTimer.getTime()
    block_text = visual.TextStim(win, text=block_msg)
    
    block_text.draw()
    win.flip()
    event.waitKeys()

    #-randomize order of trials here
    np.random.shuffle(stims)

    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials
        #-set stimuli and stimulus properties for the current trial
    for trial in range(nTrials):
        my_image.image = os.path.join(image_dir, stims[trial])
        trialTimer.reset()
        trialStart = trialTimer.getTime()
    #=====================
    #START TRIAL
    #=====================  
        stimTimer.reset()
        while stimTimer.getTime() <= 1:
            fix_text.draw()
            win.flip()

        stimTimer.reset()
        respTimer.reset()
        while stimTimer.getTime() <= .5:
            my_image.draw()
            win.flip()
            
        stimTimer.reset()
        while stimTimer.getTime() <= 1:
            fix_text.draw()
            win.flip()
        
        event.waitKeys()
        respTimer.getTime()
        
        trialEnd = trialTimer.getTime()
        
    blockEnd = blockTimer.getTime()
#-draw end trial text
end_trial_text = visual.TextStim(win, text=end_trial_msg)
end_trial_text.draw()
        
#-flip window
win.flip()
event.waitKeys()
        
#======================
# END OF EXPERIMENT
#======================        
#-close window
win.close()