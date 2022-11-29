from psychopy import core, event, visual, monitors

mon = monitors.Monitor('myMonitor', width=30.41, distance=60) 
mon.setSizePix([1440,900])
mon.save()
win = visual.Window(monitor=mon, size=(800,800), color=[-1,-1,-1])

nTrials=10
my_text = visual.TextStim(win)
fix=visual.TextStim(win, text='+')

for trial in range(nTrials):
    
    keys = event.getKeys(keyList=['1','2'])
    my_text.text = "trial %i" %trial
    
    fix.draw()
    win.flip()
    core.wait(2)
    
    event.clearEvents()
    
    my_text.draw()
    win.flip()
    core.wait(1)
    
    print("keys that were pressed", keys)
    
    if keys:
        sub_resp = keys[0]
        
    print("response that was counted", sub_resp)
    
win.close()