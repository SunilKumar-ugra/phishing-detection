
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from keras.optimizers import Adam
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from imutils import paths
from PhishingSiteDetection.phishingSource.lenet import LeNet
import random
import numpy as np
#import argparse
import cv2
import os

#ap= argparse.ArgumentParser()

#ap.add_argument("-d","--dataset",type=str,required=True,
 #               help="path dataset of input")

#ap.add_argument("-m","--model",type=str , required=True,
#                help="path to trained model")

#ap.add_argument("-p","--plot",type=str,default="plot.png",
 #               help="path ti output loss/accuracy plot")

#args=vars(ap.parse_args())

class work:
    def train():
        
        num_epochs = 10
        INIT_LR = 1e-3
        BS=32
        data=[]
        labels=[]
        
        train_path = sorted(list(paths.list_images('C:\Phishing_site_detection\images')))
        random.seed(42)
        random.shuffle(train_path)
        
        for file in train_path:
            image= cv2.imread(file)
            print(file)
            image = cv2.resize(image,(28,28))
            image = img_to_array(image)
            data.append(image)
            
            label= file.split(os.path.sep)[-2]
            label=0 if label == "cloned" else 1
            labels.append(label)
            
        data = np.array(data,dtype=float) /255.0
        labels=np.array(labels)
        
        (trainX, testX, trainY, testY) = train_test_split(data,
        	labels, test_size=0, random_state=42)
        
        
        trainY = to_categorical(trainY, num_classes=2)
        testY = to_categorical(testY, num_classes=2)
        
        aug = ImageDataGenerator(
                rotation_range = 30,
                width_shift_range=0.1,
                height_shift_range=0.1,
                shear_range=0.2,
                zoom_range=0.2,
                horizontal_flip =True,
                fill_mode = "nearest"
                )
        
        
        model = LeNet.build(width=28, height=28, depth=3, classes=2)
        opt = Adam(lr=INIT_LR, decay=INIT_LR / num_epochs)
        model.compile(loss="binary_crossentropy", optimizer=opt,
        	metrics=["accuracy"])
        
        
        model.fit_generator(aug.flow(trainX, trainY, batch_size=BS),
        	validation_data=(testX, testY), steps_per_epoch=len(trainX) // BS,
        	epochs=num_epochs, verbose=1)
            
        model.save('dup_not_dup.model')
        

