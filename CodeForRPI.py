import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os;
import RPi.GPIO as GPIO;
import time;
from picamzero import Camera
#import mpyg321
import torch
from PIL import Image
import ultralytics
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print ("LED on")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print ("LED off")
GPIO.output(18,GPIO.LOW)
#cam = Camera()

j = 0
while(True):
    
    #cam.start_preview()
    #cam.take_photo("~/Desktop/new_image" + j + ".jpg")
    #cam.stop_preview()

    # Function to load the model
    def load_model(model_path):
        dictstr = open(model_path, 'r') 
        strtuple = dictstr.read()
        print(strtuple)
        model = torch.load(strtuple,weights_only=False)
        model.eval()  # Set the model to evaluation mode
        return model

    # Function to preprocess the image before feeding it to the model
    def preprocess_image(image_path):
        img = Image.open(image_path).convert("RGB")
        img = img.resize((4000, 3000))  # Resize to the model's expected input size
        img = np.array(img).astype(np.float32) / 255.0  # Convert to a NumPy array and normalize
        img = np.transpose(img, (2, 0, 1))  # Transpose the image to (channels, height, width)
        img = np.expand_dims(img, axis=0)  # Add a batch dimension
        return torch.tensor(img)

    # Load the model
    model_path = "/home/gscc6424/Downloads/StainSeer-main/yolo11n.pt"
    model = load_model(model_path)

    # Load the image and preprocess it
    image_path = "path/to/your/image.jpg"
    input_image = preprocess_image(image_path)

    # Run the model
    output = model(input_image)
    probs = output.probs()
    if(probs.top1==3 or probs.top1==5):
            os.system('mpg321 ~/Desktop/beep-06.mp3')
    j=j+1
