from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import commonStructure

def createAccountModule(status):
    root= Tk()
    root.geometry("666x568+400+100")
    root.title("Criminal Identification System using Facial Recognition")
    # Boolean value for Width,Height
    root.resizable(False,False)
    root.overrideredirect(True)
    # To keep the window on top of other windows
    root.attributes('-topmost',True)
    # Window heading
    heading=Label(root,text="Create User Account",font=("helvetica",30,"bold"))
    heading.place(x=140, y=100)
    # New user credentials
    newUserLabelFrame=LabelFrame(root, text="Enter New User Details",font=("helvetica",10,"bold"),fg="red")
    newUserLabelFrame.place(x=20, y=230, width=300, height=200)
    # New username
    newUsername=StringVar()
    newUsernameLabel=ttk.Label(newUserLabelFrame, text="New Username", font=("helvetica",13,"bold"))
    newUsernameLabel.place(x=5, y=30)
    newUsernameEntry=ttk.Entry(newUserLabelFrame, textvariable=newUsername, width=15, font=("helvetica",13,"bold"))
    newUsernameEntry.place(x=135, y=30)
    # New password
    newPassword=StringVar()
    newPasswordLabel=ttk.Label(newUserLabelFrame, text="New Password", font=("helvetica",13,"bold"))
    newPasswordLabel.place(x=5, y=90)
    newPasswordEntry=ttk.Entry(newUserLabelFrame, textvariable=newPassword, show="*", width=15, font=("helvetica",13,"bold"))
    newPasswordEntry.place(x=135, y=90)
    # Authorized Admin's credentials
    adminLabelFrame=LabelFrame(root, text="Enter the authorizing admin's details",font=("helvetica",10,"bold"),fg="red")
    adminLabelFrame.place(x=350, y=230, width=300, height=200)
    # Admin Username
    adminUsername=StringVar()
    adminUsernameLabel=ttk.Label(adminLabelFrame, text="Admin Username", font=("helvetica",13,"bold"))
    adminUsernameLabel.place(x=5, y=30)
    adminUsernameEntry=ttk.Entry(adminLabelFrame, textvariable=adminUsername, width=15, font=("helvetica",13,"bold"))
    if status=="no admin":
        adminUsernameEntry.config(state='disabled')
    adminUsernameEntry.place(x=145, y=30)
    # Admin Password
    adminPassword=StringVar()
    adminPasswordLabel=ttk.Label(adminLabelFrame, text="Admin Password", font=("helvetica",13,"bold"))
    adminPasswordLabel.place(x=5, y=90)
    adminPasswordEntry=ttk.Entry(adminLabelFrame, textvariable=adminPassword, show="*", width=15, font=("helvetica",13,"bold"))
    if status=="no admin":
        adminPasswordEntry.config(state='disabled')
    adminPasswordEntry.place(x=145, y=90)
    # Submit function for account creation
    def submitFunction():
        if status=="no admin":
            if newUsernameEntry.get()=="" or newPasswordEntry.get()=="":
                messagebox.showerror("Error","All fields required")
            else:
                try:
                    database=mysql.connector.connect(host="localhost", username="Admin", password="password", database="criminal_identification_db")
                    cursor=database.cursor()
                    cursor.execute("INSERT INTO admin VALUES(%s,%s)",(newUsernameEntry.get(),newPasswordEntry.get(),))
                    database.commit()
                    database.close()
                    messagebox.showinfo("Success","Account Created Successfully")
                    root.destroy()
                    commonStructure.loginModule()
                except Exception as es:
                    messagebox.showerror("Error",f"An exception has occured {str(es)}")
        elif status=="admin exists":
            if newUsernameEntry.get()=="" or newPasswordEntry.get()=="" or adminUsernameEntry.get()=="" or adminPasswordEntry.get()=="":
                messagebox.showerror("Error","All fields required")
            else:
                try:
                    database=mysql.connector.connect(host="localhost", username="Admin", password="password", database="criminal_identification_db")
                    cursor=database.cursor()
                    cursor.execute("SELECT password from admin WHERE username=%s",(adminUsernameEntry.get(),))
                    result=cursor.fetchone()
                    if result != None:
                        if result[0]==adminPasswordEntry.get():
                            cursor.execute("INSERT INTO admin VALUES(%s, %s)",(newUsernameEntry.get(),newPasswordEntry.get(),))
                            messagebox.showinfo("Success","Account Created Successfully")
                            database.commit()
                            database.close()
                            root.destroy()
                            commonStructure.loginModule()
                        else:
                            messagebox.showerror("Error","Authorized Admin Password Mismatch")
                    else:
                        messagebox.showerror("Error","Wrong Authorized Admin Details Provided")     
                except Exception as es:
                    messagebox.showerror("Error",f"An exception has occured {str(es)}")
    # Submit button
    submitButton=Button(root, text="Submit", cursor="hand2", width=10, font=("helvetica",15,"bold"), command=submitFunction)
    submitButton.place(x=270,y=450)
    # destroy the create user window and reopen the login window
    def createUserDestroy():
        root.destroy()
        commonStructure.loginModule()
    # Exit button 
    exitButton=Button(root, text="Exit", cursor="hand2", width=20, font=("helvetica",20,"bold"), command=createUserDestroy)
    exitButton.place(x=170,y=510)
    root.mainloop()