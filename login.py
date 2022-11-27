from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import serialGenerator as sg
from createUser import createAccountModule 
import commonStructure

def loginModule():
    root= Tk()
    root.geometry("666x568+400+100")
    root.title("Criminal Identification System using Facial Recognition")
    # Boolean value for Width,Height
    root.resizable(False,False)
    root.overrideredirect(True)
    # To keep the window on top of other windows
    root.attributes('-topmost',True)
    global loginImage # images stored in local variables do not show up inside functions
    loginImage=Image.open("resources\loginBackground.jpg")
    loginImage=loginImage.resize((666,500), Image.ANTIALIAS)
    loginImage=ImageTk.PhotoImage(loginImage)
    # Home label for inserting image 
    loginLabel=Label(root, image=loginImage)
    loginLabel.place(x=0,y=0)

    # User credentials entry and submit
    # Username
    username=StringVar()
    usernameLabel=ttk.Label(loginLabel, text="Username", font=("helvetica",15,"bold"))
    usernameLabel.place(x=380, y=230)
    usernameEntry=ttk.Entry(loginLabel, textvariable=username, width=15, font=("helvetica",15,"bold"))
    usernameEntry.place(x=480, y=230)
    # Password
    password=StringVar()
    passwordLabel=ttk.Label(loginLabel, text="Password", font=("helvetica",15,"bold"))
    passwordLabel.place(x=380, y=280)
    passwordEntry=ttk.Entry(loginLabel, textvariable=password, show="*", width=15, font=("helvetica",15,"bold"))
    passwordEntry.place(x=480, y=280)
    
    # Create user account function
    def createUserAccount():
        try:
            database=mysql.connector.connect(host="localhost", username="Admin", password="password", database="criminal_identification_db")
            cursor=database.cursor()
            cursor.execute("SELECT username FROM admin")
            result=cursor.fetchone()
            if result==None:
                root.destroy()
                createAccountModule("no admin")
            else:
                root.destroy()
                createAccountModule("admin exists")
        except Exception as es:
            messagebox.showerror("Error",f"An exception has occured {str(es)}")
    #Create user account
    userAccountButton=Button(loginLabel, text="Create Account", cursor="hand2", font=("helvetica",8,"bold"), command=createUserAccount)
    userAccountButton.place(x=475,y=317)

    # Login Function
    def loginFunction():
        if username.get() == "" and password.get() == "":
            messagebox.showerror("Error","Enter All Details")
        elif username.get() =="" and password.get() != "":
            messagebox.showerror("Error","Username not entered")
        elif username.get() !="" and password.get() == "":
            messagebox.showerror("Error","Password not entered")
        else:
            try:
                database=mysql.connector.connect(host="localhost", username="Admin", password="password", database="criminal_identification_db")
                cursor=database.cursor()
                cursor.execute("SELECT * from admin WHERE username=%s",(username.get(),))
                result=cursor.fetchone()
                if result != None and result[0]==username.get():
                    if password.get()==result[1]:
                        sg.login()
                        root.destroy()
                    else:
                        messagebox.showerror("Error","Invalid Password")                           
                else:
                    messagebox.showinfo("Info","Username not found")
                database.commit()
                database.close()
            except Exception as es:
                messagebox.showerror("Error",f"An exception has occured {str(es)}")
    # Login button
    loginButton=Button(loginLabel, text="Login", cursor="hand2", width=10, font=("helvetica",15,"bold"), command=loginFunction)
    loginButton.place(x=455,y=350)
    
    # Exit button 
    exitButton=Button(root, text="Exit", cursor="hand2", width=20, font=("helvetica",20,"bold"), command=root.destroy)
    exitButton.place(x=170,y=510)
    
    root.mainloop()