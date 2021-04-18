import webbrowser as w
import pyautogui as py
import numpy as np
import cv2 
import os
import time
from PhishingSiteDetection.saveModels import work

def Write():
    
    time.sleep(15)
    image =py.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    val=cv2.imwrite("screenshot"+str(i)+".jpeg",image)
    print(val)
    os.chdir("C:\Phishing_site_detection\images")
    
    
file ='siteList.txt'
i=0
with open(file,'r') as f:
   for line in f:
       opensite = w.open(line)
       if(opensite):
           spltAr = line.split("://")
           j = (0,1)[len(spltAr)>1];
           dm = spltAr[j].split("?")[0].split("\n")[0].lower();
           path = dm+"/"
           if not os.path.exists(path):
               os.makedirs(path)
               os.chdir(path)
               Write()
           else:
               os.chdir(path)
               Write()
           i=i+1
work.train()


           

        
    