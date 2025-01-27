import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os;
import cv2 #image processing
#import RPi.GPIO as GPIO;
import time;
#from picamzero import Camera #for the camera
from PIL import Image
from pygame import mixer  # Audio
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(18,GPIO.OUT)
#print ("LED on")
#GPIO.output(18,GPIO.HIGH)
#time.sleep(1)
#print ("LED off")
#GPIO.output(18,GPIO.LOW)
#cam = Camera()
j=0
while(j==0):
    
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

    print(bavg,ravg,gavg)
    print(bstd,rstd,gstd)
    i=0
    for y in bluedata:
        for x in y:
            if (x> bavg + 3*bstd or x < bavg - 3*bstd):
                print("stain found")
                i=i+1
                break
                for y in reddata:
                    for x in y:
                        if (x> ravg + 3*rstd or x < ravg - 3* rstd):
                            print("stain found")
                            i=i+1
                            break

                            for y in greendata:
                                for x in y:
                                    if (x> gavg + 3*gstd or x < gavg - 3*gstd):
                                        print("stain found")
                                        i=i+1
                                        break
    if (i>=1):
        mixer.init()
        mixer.music.load("C:\\Users\\gscc6\\Downloads\\StainSeer-main\\StainSeer-main\\beep-06.mp3")
        mixer.music.play()
    j=1

