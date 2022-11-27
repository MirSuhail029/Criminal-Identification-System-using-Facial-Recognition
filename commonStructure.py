from tkinter import *
from scan import scanModule
from home import homeModule
from register import registerModule
from train import trainModule
from records import recordsModule
from developer import developerModule
from login import loginModule
import serialGenerator as sg

# Calling the login module for authentication before access is granted
loginModule()

root=Tk()
root.iconbitmap(default=r"icons\sheriff.ico")
root.title("Criminal Identification System using Facial Recognition")
root.wm_attributes('-fullscreen','True')

# Heading fwhite
head=Frame(root, height=120, bd=2, width=1366, bg="white", relief=RIDGE)
head.place(x=0,y=0)
# Heading frame label
headLabel=Label(head,text="Criminal Identification System Using Facial Recognition", font=("helvetica",30,"bold"), bg="lightblue")
headLabel.place(x=0,y=0,height=114, width=1360)

# Left frame
left=Frame(root, height=648, bd=2, width=250, bg="white", relief=RIDGE)
left.place(x=0,y=121)
# Sub frames within left frame
home=Frame(left, height=88, bd=2, width=242, bg="white", relief=RIDGE)
home.place(x=0,y=0)
scan=Frame(left, height=88, bd=2, width=242, bg="white", relief=RIDGE)
scan.place(x=0,y=90)
fir=Frame(left, height=88, bd=2, width=242, bg="white", relief=RIDGE)
fir.place(x=0,y=180)
training=Frame(left, height=88, bd=2, width=242, bg="white", relief=RIDGE)
training.place(x=0,y=270)
records=Frame(left, height=88, bd=2, width=242, bg="white", relief=RIDGE)
records.place(x=0,y=360)
developer=Frame(left, height=88, bd=2, width=242, bg="white", relief=RIDGE)
developer.place(x=0,y=450)
exit=Frame(left, height=88, bd=2, width=242, bg="white", relief=RIDGE)
exit.place(x=0,y=540)

# Sub frame menu buttons
homeButton=Button(home,text="Home", cursor="hand2", font=("helvetica",24,"bold"), bg="lightblue", command=homeModule)
homeButton.place(x=0,y=0, height=84, width=238)
scanButton=Button(scan,text="Scan", cursor="hand2",font=("helvetica",24,"bold"), bg="lightblue", command=scanModule)
scanButton.place(x=0,y=0, height=84, width=238)
registerButton=Button(fir,text="Register", cursor="hand2",font=("helvetica",24,"bold"), bg="lightblue", command=registerModule)
registerButton.place(x=0,y=0, height=84, width=238)
trainingButton=Button(training,text="Train", cursor="hand2",font=("helvetica",24,"bold"), bg="lightblue", command=trainModule)
trainingButton.place(x=0,y=0, height=84, width=238)
recordsButton=Button(records,text="Records", cursor="hand2",font=("helvetica",24,"bold"), bg="lightblue", command=recordsModule)
recordsButton.place(x=0,y=0, height=84, width=238)
developerButton=Button(developer,text="Developer", cursor="hand2",font=("helvetica",24,"bold"), bg="lightblue", command=developerModule)
developerButton.place(x=0,y=0, height=84, width=238)
exitButton=Button(exit,text="Exit", cursor="hand2",font=("helvetica",24,"bold"), bg="lightblue", command=root.destroy)
exitButton.place(x=0,y=0, height=84, width=238)

homeModule()
# Runs when a user exits without logging in
if sg.exit_status()==True:
    root.destroy()
root.mainloop()