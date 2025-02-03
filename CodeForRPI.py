import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os;
import random
import string
import cv2 #image processing
#import RPi.GPIO as GPIO;
import time;
#from picamzero import Camera #for the camera
from PIL import Image
from pygame import mixer  # Audio
import threading
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(18,GPIO.OUT)
#print ("LED on")
#GPIO.output(18,GPIO.HIGH)
#time.sleep(1)
#print ("LED off")
#GPIO.output(18,GPIO.LOW)
#cam = Camera()
mixer.init()

while(True):
    mixer.music.unload()
    length = 8
    j = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    print(j)
    #cam.start_preview()
    #cam.take_photo("~/Desktop/new_image" + j + ".jpg")
    #cam.stop_preview()

    # Import the necessary libraries
    # load the image and convert into
    # diffrent channels
    image = cv2.imread("C:\\Users\\gscc6\\Downloads\\stainsample.jpg")
    b,g,r = cv2.split(image)
    # asarray() class is used to convert
    # PIL images into NumPy arrays
    bluedata = np.asarray(b)
    reddata = np.asarray(r)
    greendata = np.asarray(g)
    bavg= np.mean(bluedata)
    ravg= np.mean(reddata)
    gavg= np.mean(greendata)
    bstd= np.std(bluedata)
    rstd= np.std(reddata)
    gstd= np.std(greendata)

    count = bluedata.size
    print (count)
    sleeptime = 5/count
    #print(bavg,ravg,gavg)
    #print(bstd,rstd,gstd)

    i=0
    k=0
    mixer.music.load("C:\\Users\\gscc6\Downloads\\beepbeepbeep-53921.mp3")
    start = time.time()
    for y in bluedata:
        for x in y:
            if (k % 10000 == 0):
                mixer.music.play()
                time.sleep(0.4)
            if (x> bavg + bstd or x < bavg - bstd):
                #print("stain found")
                i=i+1 
            k+=1
            
    k=0
    
    #if(i==0):
    for y in reddata:
        for x in y:
            if (k % 10000 == 0):
                mixer.music.play()
                time.sleep(0.4)
            if (x> ravg + rstd or x < ravg - rstd):
                #print("stain found")
                i=i+1
            time.sleep(sleeptime)
            k+=1

    k=0

    #if(i==0):
    for y in greendata:
        for x in y:
            if (k % 10000 == 0):
                mixer.music.play()
                time.sleep(0.4)
            if (x> gavg + gstd or x < gavg - gstd):
                #print("stain found")
                i=i+1
            time.sleep(sleeptime)
            k+=1

    if (i>=1):
        mixer.music.unload()
        mixer.music.load("C:\\Users\\gscc6\\Downloads\\StainSeer-main\\StainSeer-main\\beep-06.mp3")
        mixer.music.play()
    end = time.time()
    print(end-start)
    time.sleep(1)
    

