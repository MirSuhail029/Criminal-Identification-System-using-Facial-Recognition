from tkinter import *
from tkinter import ttk
import os
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2
import commonStructure

def trainModule():
    # Right frame
    right=Frame(commonStructure.root, width=1116, height=646, bd=2, bg="lightgreen", relief=RIDGE)
    right.place(x=251,y=121)
    global trainImage   # images stored in local variables do not show up inside functions
    trainImage=Image.open("resources\\trainBackground.jpg")
    trainImage=trainImage.resize((1105,636), Image.ANTIALIAS)
    trainImage=ImageTk.PhotoImage(trainImage)
    rightLabel=Label(right, image=trainImage, width=1110, height=640, bd=2, relief=RIDGE)
    rightLabel.place(x=0,y=0)
    
    def train_classifier():
        # Path of the directory/folder where all the samples are stored
        sampleLocation=r"C:\Users\Admin\Desktop\Criminal identification system with facial recognition\facial recognition samples"
        sampleDirectory=(sampleLocation)
        # List that will be used to store the complete path of all the samples
        # i.e. the directory path joined with the sample path along with its file extension
        samplePaths=[]
        for file in os.listdir(sampleDirectory):
            samplePaths.append(os.path.join(sampleDirectory,file))
        # A list the will store the sample image values of all the samples in the form of an array   
        faceArrays=[]
        # A list the will store the id's associated with collected samples   
        criminalId=[]
        for img in samplePaths:
            image=Image.open(img).convert('L')
            imageArray=np.array(image,'uint8')
            faceArrays.append(imageArray)
            id=os.path.split(img)[1].split('.')[0]
            # Convert id from string to int because train function does not accept string value arrays
            criminalId.append(int(id))
            winname = "Training"
            cv2.namedWindow(winname)
            cv2.setWindowProperty(winname, cv2.WND_PROP_TOPMOST, 1)
            cv2.moveWindow(winname, 600,200)
            cv2.imshow(winname, imageArray)
            cv2.waitKey(10)
        # An array created using the criminalId list (it contains all the id's in the form of an array)
        idArray=np.array(criminalId)
    
        classifier=cv2.face.LBPHFaceRecognizer_create()
        classifier.train(faceArrays,idArray)
        classifier.write("resources\classifier.xml")
        
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Completed")

    
    

    

    # Options frame
    options=Frame(right, bg="white")
    options.place(x=0, y=551, width=1110, height=90)

    # Options frame division
    # Train button
    train_frame=Frame(options, bg="white")
    train_frame.place(x=278, y=0, width=554, height=89)
    style=ttk.Style()
    style.configure("train.TButton", font=("helvetica",20,"bold"))
    train_button=ttk.Button(train_frame, style="train.TButton", cursor="hand2", text="Train", command=train_classifier)
    train_button.place(x=65, y=15, width=424, height=60)

    
    
    
    
    