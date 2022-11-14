from psychopy import core, gui, visual, monitors, event
from datetime import datetime
import os
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

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks
for block in range(nBlocks):
    #-present block start message
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
    my_image.draw()
    win.flip()
    event.waitKeys()
        #=====================
        #START TRIAL
        #=====================  
        #-draw fixation
    fix_text.draw()
        #-flip window
    win.flip()
    event.waitKeys()
        
        #-wait time (stimulus duration)
    core.wait(2.0)
        
        #-draw image
    my_image.draw()
        #-flip window
    win.flip()
    event.waitKeys()
        
        #-wait time (stimulus duration)
    core.wait(2.0)
        
        #-draw end trial text
    end_trial_text = visual.TextStim(win, text=end_trial_msg)
    end_text.draw()
        
        #-flip window
    win.flip()
    event.waitKeys()
        
        #-wait time (stimulus duration)
    core.wait(2.0)
        
#======================
# END OF EXPERIMENT
#======================        
#-close window
win.close()

#Stimulus exercises question 1

my_image = visual.ImageStim(win, units = 'pix', size = 400,400)
nTrials = 3
image_dir = os.path.join(main_dir, 'images')
stims = ['face01.jpg', 'face02.jpg', 'face03.jpg']

for trial in range(nTrials):
    my_image.image = os.path.join(image_dir, stims[trial])
    my_image.draw()
    fix_text.draw()
    win.flip()
    event.waitKeys()

win.close()

#Answer:Enlarges photo and makes it unclear
    #Change the units into pixels

#Stimulus exercises question 2
mon = monitors.Monitor('myMonitor', width=30.41, distance=60)
mon.setSizePix([1440,900])
mon.save()
thisSize = mon.getSizePix()
thisWidth = thisSize[0]
thisHeight = thisSize[1]

win = visual.Window(monitor = mon, fullscr = True)

my_image = visual.ImageStim(win)
nTrials = 4
image_dir = os.path.join(main_dir, 'images')
stims = ['face01.jpg', 'face02.jpg', 'face03.jpg']

horizMult = [-1, 1, 1, -1]
verMult = [1, 1, -1, -1]

for trial in range(nTrials):
    my_image.image = os.path.join(image_dir, stims[trial])
    
    my_image.pos = (horizMult[trial] * thisWidth/4, verMult[trial] * thisHeight/4)
    my_image.draw()
    fix_text.draw()
    win.flip()
    event.waitKeys()

win.close()