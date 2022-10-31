#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions *
import numpy as np

#-import psychopy functions
from psychopy import core, gui, visual, event

#-import file save functions
import json

#-(import other functions as necessary: os...)
import os

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
#-define the directory where you will save your data
#-if you will be presenting images, define the image directory
#-check that these directories exist
print(os.getcwd())
main_dir = os.getcwd()
image_dir = os.path.join(main_dir,'images')
data_dir = os.path.join(main_dir,'data')

if not os.path.isdir(image_dir):
    raise Exception("Could not find the path!")

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
nTrials = 10
nBlocks = 2
#-stimulus names (and stimulus extensions, if images) *
cats = ['faces']*10
imgs = ['im1.png', 'im2.png', 'im3.png', 'im4.png' 'im5.png', 'im6.png', 'im7.png', 'im8.png', 'im9.png', 'im10.png']*2

#-stimulus properties like size, orientation, location, duration *
stimSize = [200,200]; 
stimDur = 1;
stimOrien = [10];

#-start message text *
startMessage = "Welcome to the experiment. Press any key to begin"
print(startMessage)

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
pics = ['face01.jpg','face02.jpg','face03.jpg','face04.jpg','face05.jpg','face06.jpg','face07.jpg','face08.jpg','face09.jpg','face10.jpg']

'face' + str(number) + '.jpg'
ims_in_dir = sorted(os.listdir(image_dir))
if not pics == ims_in_dir:
    raise Exception("The image lists do not match up!")

#-create counterbalanced list of all conditions *
catimgs = list(zip(cats,imgs))

#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#-create an empty list for correct responses (e.g., "on this trial, a response of X is correct") *
corrResp = []
corrResp = np.zeros(20);

#-create an empty list for participant responses (e.g., "on this trial, response was a X") *
corrResp = np.zeros(20);

#-create an empty list for response accuracy collection (e.g., "was participant correct?") *
corrResp = np.zeros(20);

#-create an empty list for response time collection *
corrResp = np.zeros(20);

#-create an empty list for recording the order of stimulus identities *
idOrder = []
idOrder = idOrder.append(catimgs)

#-create an empty list for recording the order of stimulus properties *
propOrder = []
propOrder = propOrder.append(stimSize + stimDur + stimOrien)

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for thisBlock in range(nBlocks):
    #-present block start message
    print('Welcome to block ' + str(thisBlock + 1))
    
    #-randomize order of trials here *
    np.random.shuffle(catimgs)

    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for thisTrial in range(nTrials):
        print('Trial ' + str(thisTrial + 1))
        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses