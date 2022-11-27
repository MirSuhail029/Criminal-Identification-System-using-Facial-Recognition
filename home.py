from tkinter import *
from PIL import Image, ImageTk
import commonStructure
userGuideVar=False
def homeModule():
    # Right frame
    right=Frame(commonStructure.root, height=646, bd=2, width=1116, bg="white", relief=RIDGE)
    right.place(x=251,y=121)
    #Right frame image background
    global homeImage # images stored in local variables do not show up inside functions
    if userGuideVar==True:
        homeImage=Image.open("resources\homeOriginal.jpg")
    else:
        homeImage=Image.open("resources\home.jpg")
    homeImage=homeImage.resize((1105,636), Image.ANTIALIAS)
    homeImage=ImageTk.PhotoImage(homeImage)
    # Home label for inserting image 
    homeLabel=Label(right, image=homeImage)
    homeLabel.place(x=0,y=0)
    if userGuideVar==True:
        guideLabelFrame=LabelFrame(right, text="Welcome to the CISFR User Guide", font=("helvetica",15,"bold"), bd=7, relief=RIDGE)
        guideLabelFrame.place(x=100,y=15, width=930, height=575)
        # Used for wrapping text
        textWrappingSize=890
        registerCriminalLabel=Label(guideLabelFrame, text="Registering a criminal:", justify=LEFT, font=("times new roman",12,"bold"))
        registerCriminalLabel.place(x=10, y=10)
        registerDetailsLabel=Label(guideLabelFrame, wraplength=textWrappingSize, justify=LEFT, font=("times new roman",10), text="If the application is not being run for the first time, make sure to scan the face of a person to check for any previous records available in the database before adding any details of that person. This can be done using the Scan module, click on the Scan tab to open up the scan interface, then click the scan button to scan the face of a person to check for any available records.\nIf the application is being run for the very first time or no criminal record for a person is found after scanning his/her face, click on the register tab to open up the register interface. click on the facial biometrics button to capture the facial biometrics of the criminal, after that, proceed with entering all his/her personal details. Once all the personal details have been entered, fill in the crime details for the criminal. Crime details can be one or multiple, once the details for a crime are entered, click the add crime button and proceed to enter more crime details if any. once all the crime details are entered and added, click on the submit button to register the criminal record for a particular criminal.")
        registerDetailsLabel.place(x=10, y=35)
        trainingLabel=Label(guideLabelFrame, text="Training the model:", justify=LEFT, font=("times new roman",12,"bold"))
        trainingLabel.place(x=10, y=160)
        trainingDetailsLabel=Label(guideLabelFrame, wraplength=textWrappingSize, justify=LEFT, font=("times new roman",10), text="After capturing the criminal biometrics and other details, the next step is to train the classifier so that it links the biometrics collected to the particular criminal. Go to the Train tab and click it to open the training interface. Click on train button and wait for the model to be trained, at the end you will be displayed a success message. click ok to proceed.")
        trainingDetailsLabel.place(x=10, y=185)
        scanLabel=Label(guideLabelFrame, text="Scanning the criminal:", justify=LEFT, font=("times new roman",12,"bold"))
        scanLabel.place(x=10, y=240)
        scanDetailsLabel=Label(guideLabelFrame, wraplength=textWrappingSize, justify=LEFT, font=("times new roman",10), text="To identify a criminal, click on the Scan tab and it will open up the scan interface. Click the Scan button to scan and identify a criminal, if the database contains the record of the person being scanned, it will identify the person and display his/her criminal ID and recent crime. If more details are required, long press the enter key and the scanning window will close and the details of the criminal will pop up on to the screen. In case, no record for a person being scanned is available in the database, the scanning window will display the person as unknown. To add a record for unknown criminal, you would then need to go to the register tab and create a fresh criminal record for that person.")
        scanDetailsLabel.place(x=10, y=265)
        recordsLabel=Label(guideLabelFrame, text="Viewing the records and making changes:", justify=LEFT, font=("times new roman",12,"bold"))
        recordsLabel.place(x=10, y=350)
        recordsDetailsLabel=Label(guideLabelFrame, wraplength=textWrappingSize, justify=LEFT, font=("times new roman",10), text="To view all the criminal records present in the database, go to the Records tab and click on it to open up the records interface. All the criminal details will be displayed on the screen, if you want to view all the crime records alongside the criminal records, click the show crimes checkbox for that purpose.\nIn case you want to view the records for a particular criminal only, then you need to choose the select search filter and choose the option of criminal id to search using the id or criminal name to search using the name. once the options are chosen, enter the id or name and click on the search button and all the records for the id or name will be displayed on to the screen.\nTo delete a criminal record, select the row displaying the criminal record and click on the delete button and proceed further to delete that record.\nTo make changes to the existing criminal record, select the criminal record and click on edit criminal button and proceed further to make the necessary changes.\nTo make changes to the existing crime record, select the crime record and click on edit crime button and proceed further to make the necessary changes.\nTo add new crime records for a criminal whose record already exists in the database, select the criminal details and click on add more crimes button and proceed further to add new crime details for that criminal.")
        recordsDetailsLabel.place(x=10, y=375)
    def UserGuideFunction():
        global userGuideVar
        userGuideVar=True
        homeModule()
    userGuide_button=Button(right, text="User Guide", cursor="hand2", font=("helvetica",8,"bold"), command=UserGuideFunction)
    userGuide_button.place(x=1000,y=600)
    if userGuideVar==True:
        closeGuideButton=Button(guideLabelFrame, text="X", font=("helvetica",13,"bold"), command=homeModule)
        closeGuideButton.place(x=880, y=0)
    def resetUserGuideVar():
        global userGuideVar
        userGuideVar=False
    resetUserGuideVar()