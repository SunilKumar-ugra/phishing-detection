import pyautogui as py
import numpy as np
from PhishingSiteDetection import loadModel as lm
# import cv2
import cv2

def Screenshot(url):    
    file  = 'site_list.txt'
    with open(file,'r') as f:
        for line in f:
            spltAr = line.split("://")
            j = (0,1)[len(spltAr)>1];
            dm = spltAr[j].split("?")[0].split("\n")[0].lower();
            if(dm == url):
                image = py.screenshot()
                image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                image = np.array(image)
                lm.testCase(image)
            else:
                return "Site as not been trained"
                
            
    
    
    
    
    
    
    
    


