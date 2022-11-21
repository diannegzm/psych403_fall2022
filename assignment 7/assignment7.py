from psychopy import visual, monitors, event, core, logging

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon) #define a window

import os
#stuff you only have to define once at the top of your script
os.chdir('/Applications/PsychoPy.app/Contents/Resources/psychopy')
main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')

end_trial_msg = "End of trial"

fix_text = visual.TextStim(win, text='+')
my_image = visual.ImageStim(win)
end_trial_text = visual.TextStim(win, text=end_trial_msg)

stims = ['face01.jpg','face02.jpg','face03.jpg']

nBlocks=2
nTrials=3

wait_timer = core.Clock()
clock_wait_timer = core.Clock()
countdown_timer = core.CountdownTimer()

#=====================
#START TRIAL
#===================== 

for trial in range(nTrials):
    my_image.image = os.path.join(image_dir,stims[trial])
    fix_text.draw()
    win.flip()
    core.wait(.5)
    countdown_timer.reset()
    countdown_timer.addTime(1)
    imgStartTime=wait_timer.getTime()
    while countdown_timer.getTime() > 0:
        my_image.draw()
        win.flip()

    imgEndTime = wait_timer.getTime()
        
print("Image Duration was {} seconds".format(imgEndTime - imgStartTime))
    
#-draw end trial text
end_trial_text.draw()
#-flip window
win.flip()
#-wait time (stimulus duration)
core.wait(.5)

win.close()