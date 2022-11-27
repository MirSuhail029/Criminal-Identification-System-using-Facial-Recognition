from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# Tkinter does not support date selector hence, tkcalendar
from tkcalendar import DateEntry
import mysql.connector
import cv2
import os
import serialGenerator as sg
import commonStructure

updateFlag=False
idValue="0"
crimeValue="0"
addMoreCrimes=False
def updateFunction(choice, idx, crimex):
    global idValue
    idValue=idx
    if choice=="criminal":
        sg.editCriminal_set()   
    elif choice=="crime":
        global crimeValue
        crimeValue=crimex
        sg.editCrime_set()
    elif choice=="add":
        global addMoreCrimes
        addMoreCrimes=True  
    global updateFlag
    updateFlag=True
    registerModule()

def registerModule():
    # Right frame
    right=Frame(commonStructure.root, height=646, bd=2, width=1116, bg="white", relief=RIDGE)
    right.place(x=251,y=121)
    # Criminal label frame
    criminal=LabelFrame(right,text="Criminal Information", font=("helvetica",15,"bold"), fg="red")
    criminal.place(x=0, y=0, width=555, height=550)

    # Criminal form
    # Face biometrics (detect faces using haarcascade classifier and capture and store the samples onto the disk)
    def capture():
        faceClassifier=cv2.CascadeClassifier(r"C:\Users\Admin\Desktop\Criminal identification system with facial recognition\resources\haarcascade_frontalface_default.xml")
        serialNumber=sg.readOldSerial()
        # Collecting samples using webcam feed
        collectSamples = cv2.VideoCapture(0)
        # keeps track of the number of samples collected
        count=1
        #path to the directory/folder where all the collected samples will be stored
        path=r"C:\Users\Admin\Desktop\Criminal identification system with facial recognition\facial recognition samples"
        if os.path.exists(path)!=True: 
            os.mkdir(path)
        
        def faceCropped(img):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces=faceClassifier.detectMultiScale(gray,1.3,5)
            for(x,y,w,h) in faces:
                faceCropped=img[y:y+h,x:x+w]
                return faceCropped
        
        while True:
            if count==101:
                break
            ret, frame=collectSamples.read()
            gray = cv2.resize(faceCropped(frame),(400,400))
            gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
            # Sets the current directory to one in which we want to store our samples
            os.chdir(path)
            cv2.imwrite(serialNumber+"."+str(count)+".jpg",gray)
            winname = "Collecting Samples"
            cv2.namedWindow(winname)
            cv2.setWindowProperty(winname, cv2.WND_PROP_TOPMOST, 1)
            cv2.moveWindow(winname, 450,150) 
            cv2. imshow(winname, gray)
            cv2.waitKey(10)
            count+=1
        # After the loop ends, release the collectSamples object
        collectSamples.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        messagebox.showinfo("Status","Samples Collected Successfully")
        # calls the samples captured function to set the samples captured value to True
        sg.samples_captured()
        os.chdir(r"C:\Users\Admin\Desktop\Criminal identification system with facial recognition")
  
    # Criminal Facial Biometrics
    if updateFlag==False and addMoreCrimes==False :
        c_biometrics=Label(criminal,text="Facial Biometrics ", font=("helvetica",12,"bold"))
        c_biometrics.grid(row=0,column=0)
        c_biometrics_button=Button(criminal,text="Capture Biometrics", cursor="hand2", font=("helvetica",12,"bold"), command=capture)
        c_biometrics_button.grid(row=0, column=1, padx=5, pady=5)
    
    # Criminal ID
    crim_id=StringVar() # newly added for use in update function
    c_id=Label(criminal,text="Criminal ID ", font=("helvetica",12,"bold"))
    c_id.grid(row=1,column=0)
    c_id_entry=ttk.Entry(criminal, textvariable=crim_id, font=("helvetica",13))
    c_id_entry.config(state='disabled')
    c_id_entry.grid(row=1, column=1, ipadx=20, ipady=3, padx=5, pady=5)
    # Criminal name
    crim_name=StringVar()
    c_name=Label(criminal,text="Name ", font=("helvetica",12,"bold"))
    c_name.grid(row=2,column=0)
    c_name_entry=ttk.Entry(criminal,textvariable=crim_name, font=("helvetica",13))
    if sg.editCrime_status()==True or addMoreCrimes==True:
        c_name_entry.config(state='disabled')
    c_name_entry.grid(row=2, column=1, ipadx=20, ipady=3, padx=5, pady=5)
    # Criminal Parentage
    crim_parentage=StringVar()
    c_parentage=Label(criminal,text="Parentage ", font=("helvetica",12,"bold"))
    c_parentage.grid(row=3,column=0)
    c_parentage_entry=ttk.Entry(criminal,textvariable=crim_parentage, font=("helvetica",13))
    if sg.editCrime_status()==True or addMoreCrimes==True:
        c_parentage_entry.config(state='disabled')
    c_parentage_entry.grid(row=3, column=1, ipadx=20, ipady=3, padx=5, pady=5)
    # Criminal address
    crim_address=StringVar()
    c_address=Label(criminal,text="Address ", font=("helvetica",12,"bold"))
    c_address.grid(row=4,column=0)
    c_address_entry=ttk.Entry(criminal,textvariable=crim_address, font=("helvetica",13))
    if sg.editCrime_status()==True or addMoreCrimes==True:
        c_address_entry.config(state='disabled')
    c_address_entry.grid(row=4, column=1, ipadx=20, ipady=3, padx=5, pady=5)
    # Criminal gender
    crim_gender=StringVar()
    c_gender=Label(criminal,text="Gender ", font=("helvetica",12,"bold"))
    c_gender.grid(row=5,column=0)
    c_gender_radio=ttk.Radiobutton(criminal,text="Male",value="male", variable=crim_gender)
    if sg.editCrime_status()==True or addMoreCrimes==True:
        c_gender_radio.config(state='disabled')
    c_gender_radio.grid(row=5, column=1, sticky=W)
    c_gender_radio=ttk.Radiobutton(criminal,text="Female",value="female", variable=crim_gender)
    if sg.editCrime_status()==True or addMoreCrimes==True:
        c_gender_radio.config(state='disabled')
    c_gender_radio.grid(row=5, column=1, sticky=N)
    c_gender_radio=ttk.Radiobutton(criminal,text="Other",value="other", variable=crim_gender)
    if sg.editCrime_status()==True or addMoreCrimes==True:
        c_gender_radio.config(state='disabled')
    c_gender_radio.grid(row=5, column=3, sticky=E)
    # Criminal DOB
    crim_dob=StringVar()
    c_dob=Label(criminal, text="Date of Birth ", font=("helvetica",12,"bold"))
    c_dob.grid(row=6,column=0)
    if sg.editCrime_status()==True or addMoreCrimes==True:
        c_dob_entry=DateEntry(criminal,state=DISABLED, textvariable=crim_dob, font=("helvetica",13))
    else:
        c_dob_entry=DateEntry(criminal, textvariable=crim_dob, font=("helvetica",13))
    c_dob_entry.grid(row=6, column=1, ipadx=47, ipady=3, padx=5, pady=5)
    # Criminal height
    crim_height=StringVar()
    c_height=Label(criminal,text="Height (in cms) ", font=("helvetica",12,"bold"))
    c_height.grid(row=7,column=0)
    c_height_entry=ttk.Entry(criminal,textvariable=crim_height, font=("helvetica",13))
    if sg.editCrime_status()==True or addMoreCrimes==True:
        c_height_entry.config(state='disabled')
    c_height_entry.grid(row=7, column=1, ipadx=20, ipady=3, padx=5, pady=5)
    # Criminal weight
    crim_weight=StringVar()
    c_weight=Label(criminal,text="Weight (in Kg) ", font=("helvetica",12,"bold"))
    c_weight.grid(row=8,column=0)
    c_weight_entry=ttk.Entry(criminal,textvariable=crim_weight, font=("helvetica",13))
    if sg.editCrime_status()==True or addMoreCrimes==True:
        c_weight_entry.config(state='disabled')
    c_weight_entry.grid(row=8, column=1, ipadx=20, ipady=3, padx=5, pady=5)
    # Criminal occupation
    crim_occupation=StringVar()
    c_occupation=Label(criminal,text="Occupation ", font=("helvetica",12,"bold"))
    c_occupation.grid(row=9,column=0)
    c_occupation_entry=ttk.Entry(criminal,textvariable=crim_occupation, font=("helvetica",13))
    if sg.editCrime_status()==True or addMoreCrimes==True:
        c_occupation_entry.config(state='disabled')
    c_occupation_entry.grid(row=9, column=1, ipadx=20, ipady=3, padx=5, pady=5)
    # Crime label frame
    crime=LabelFrame(right,text="Crime Information", font=("helvetica",15,"bold"), fg="red")
    crime.place(x=556, y=0, width=555, height=550)
    # Crime form
    # Crime ID
    crime_id=StringVar()
    cr_id=Label(crime,text="Crime ID ", font=("helvetica",12,"bold"))
    cr_id.grid(row=0,column=0)
    cr_id_entry=ttk.Entry(crime,textvariable=crime_id, font=("helvetica",13))
    cr_id_entry.config(state='disabled')
    cr_id_entry.grid(row=0, column=1, ipadx=20, ipady=3, padx=5, pady=5)
    # Crime ID gets changed according to the crime type chosen
    def crimeIdChange(event):
        try:
            database=mysql.connector.connect(host="localhost", username="Admin", password="password", database="criminal_identification_db")
            cursor=database.cursor()
            cursor.execute("SELECT cr_id FROM crime where cr_type=%s",(crime_type.get(),))
            result=cursor.fetchall()
            if result != None:
                crime_id.set(result[0][0])
            database.commit()
            database.close()
        except Exception as es:
            messagebox.showerror("Error",f"An exception has occured {str(es)}")
    # Crime type
    crime_type=StringVar()
    cr_type=Label(crime,text="Crime Type ", font=("helvetica",12,"bold"))
    cr_type.grid(row=1,column=0)
    crType_combo=ttk.Combobox(crime,textvariable=crime_type, state="readonly", font=("helvetica",12))
    crType_combo.bind('<<ComboboxSelected>>', crimeIdChange)
    if sg.editCriminal_status()==True:
        crType_combo.config(state='disabled')
    values=("Select Crime", "Assault", "Homicide","Burglary","Illegal Drug Trade","Kidnapping","Embezzlement","Tax Evasion","Human Trafficking","Vandalism","Forgery","Bribery","Robbery")
    crType_combo["values"]=values
    crType_combo.current(0) # Default value
    crType_combo.grid(row=1, column=1, padx=5, pady=5)

    # crimes committed form
    # Criminal crime date
    crc_crimedate=StringVar()
    cc_crimedate=Label(crime,text="Crime Date ", font=("helvetica",12,"bold"))
    cc_crimedate.grid(row=2,column=0)
    if sg.editCriminal_status()==True:
        cc_crimedate_entry=DateEntry(crime,state=DISABLED,textvariable=crc_crimedate, font=("helvetica",13))
    else:
        cc_crimedate_entry=DateEntry(crime,textvariable=crc_crimedate, font=("helvetica",13))
    cc_crimedate_entry.grid(row=2, column=1, ipadx=47, ipady=3, padx=5, pady=5)
    # Criminal arrest date
    crc_arrestdate=StringVar()
    cc_arrestdate=Label(crime,text="Arrest Date ", font=("helvetica",12,"bold"))
    cc_arrestdate.grid(row=3,column=0)
    if sg.editCriminal_status()==True:
        cc_arrestdate_entry=DateEntry(crime,state=DISABLED,textvariable=crc_arrestdate, font=("helvetica",13))
    else:
        cc_arrestdate_entry=DateEntry(crime,textvariable=crc_arrestdate, font=("helvetica",13))
    cc_arrestdate_entry.grid(row=3, column=1, ipadx=47, ipady=3, padx=5, pady=5)

    # Add crimes that have been committed by the criminal
    crimeList=[]
    crimeCommittedList=[]
    # Label frame inside which the added crimes will be displayed
    added_crimes=LabelFrame(crime,text="Added Crimes (Multiple crimes can be added)", font=("helvetica",12,"bold"), fg="red")
    added_crimes.place(x=25, y=200, width=510, height=300)
    # Tree view for added crimes
    add_crimes=ttk.Treeview(added_crimes,style="add_crimes.Treeview", column=("Crime Name","Crime Date","Arrest Date"), show="headings")
    add_crimes.column("Crime Name", stretch=YES, anchor=CENTER, width=150, minwidth=150)    
    add_crimes.heading("Crime Name", text="Crime Name",anchor=CENTER)

    add_crimes.column("Crime Date", stretch=YES, anchor=CENTER, width=150, minwidth=150)
    add_crimes.heading("Crime Date", text="Crime Date",anchor=CENTER)

    add_crimes.column("Arrest Date", stretch=YES, anchor=CENTER, width=150, minwidth=150)
    add_crimes.heading("Arrest Date", text="Arrest Date",anchor=CENTER)
    #add_crimes.pack(side=LEFT, fill=BOTH, expand=1)
    add_crimes.pack(side=LEFT, fill=BOTH, expand=1)
    # Make changes to the fonts in add crimes section
    style = ttk.Style()
    style.configure("add_crimes.Treeview", font=("helvetica",10)) 
    style.configure("add_crimes.Treeview.Heading", font=("helvetica",13)) 
    # Vertical scrollbar for added crimes
    scrollbar = ttk.Scrollbar(add_crimes, orient=VERTICAL, command=add_crimes.yview)
    add_crimes.configure(yscroll=scrollbar.set)
    scrollbar.pack(side = RIGHT, fill=BOTH)

    def addCrime_function():
        if crime_type.get()=="" or crime_type.get()=="Select Crime" or crc_crimedate.get()=="" or crc_arrestdate.get()=="":
            messagebox.showerror("Error","All Fields Are Required")
        else:
            crimeList.append(crime_type.get())
            crimeCommittedList.append([crc_crimedate.get(),crc_arrestdate.get()])
            # Clear the add crime form once the crime is added to the list
            crime_id.set("")
            crime_type.set("")
            crc_arrestdate.set("")
            crc_crimedate.set("")
            for i in range(0,len(crimeList)):
                #Clear the treeview list items (it removes the previously displayed data for the first iteration so that old and newly added data can be displayed)
                if(i==0):
                    for item in add_crimes.get_children():
                        add_crimes.delete(item)
                # Insert data into the tree view
                add_crimes.insert("",END,values=(crimeList[i], crimeCommittedList[i][0] ,crimeCommittedList[i][1]))
            sg.Crime_added()
    
    # Add crime button
    if sg.editCriminal_status()==True or sg.editCrime_status()==True:
        addCrimeButton=Button(crime, state=DISABLED, text="Add Crime", cursor="hand2", command=addCrime_function)
    else:
        addCrimeButton=Button(crime, text="Add Crime", cursor="hand2", command=addCrime_function)

    addCrimeButton.grid(row=4,column=0)
    # Clear function that removes the entered data from all entry fields
    def clearAllDataEntryFields():
        crim_id.set("")
        crim_name.set("")
        crim_parentage.set("")
        crim_address.set("")
        crim_gender.set("")
        crim_dob.set("")
        crim_height.set("")
        crim_weight.set("")
        crim_occupation.set("")
        crime_id.set("")
        crime_type.set("")
        crc_arrestdate.set("")
        crc_crimedate.set("")

    # Submit function that acquires the information provided by the user and stores it into the database
    def submit_function():
        if  sg.samples_status()==False or sg.addCrime_status()==False or crim_name.get()=="" or crim_parentage.get()=="" or crim_address.get()=="" or crim_gender.get()=="" or crim_dob.get()=="" or crim_height.get()=="" or crim_weight.get()=="" or crim_occupation.get()=="" :
            messagebox.showerror("Error","All Fields Are Required")
        else:
            try:           
                database=mysql.connector.connect(host="localhost", username="Admin", password="password", database="criminal_identification_db")
                cursor=database.cursor()
                cursor.execute("insert into criminal(sample_id,c_name,c_parentage,c_address,c_gender,c_dob,c_height,c_weight,c_occupation) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (sg.readOldSerial(),crim_name.get(),crim_parentage.get(),crim_address.get(), crim_gender.get(), crim_dob.get(), crim_height.get(), crim_weight.get(), crim_occupation.get(),))
                database.commit()
                # Acquiring the criminal id for the recently added criminal data from the criminal table
                cursor.execute("select c_id from criminal where c_name=(%s)",(crim_name.get(),))
                c_id=cursor.fetchone()
                c_id=c_id[0]
                for i in range(0,len(crimeList)):
                    # Acquiring the crime id from crimes committed table
                    cursor.execute("select cr_id from crime where cr_type=(%s)",(crimeList[i],))
                    cr_id=cursor.fetchone()
                    cr_id=cr_id[0]
                    # Inserting criminal id, crime id, crime date and arrest date into crimes committed table
                    cursor.execute("insert into crimes_committed values(%s,%s,%s,%s)", (c_id, cr_id, crimeCommittedList[i][0], crimeCommittedList[i][1],))               
                    database.commit()
                database.close()
                # Clear all data
                clearAllDataEntryFields()
                messagebox.showinfo("Success","Record updated successfully")
            except Exception as es:
                messagebox.showerror("Error",f"An exception has occured {str(es)}")

            # Reads the previous biometrics serial number from the serial text file, adds 1 to it and stores the new serial number to the file  
            serialNumber=sg.readOldSerial()
            serialNumber=sg.incrementSerial(serialNumber)
            sg.writeNewSerial(serialNumber)
            # Sets the biometric flag to False so that submit button does not allow submission without capturing biometrics first
            sg.reset_biometrics_flag()
            # Sets the add crime flag to False so that submit button does not allow submission without adding the crimes first
            sg.reset_crime_flag()
         
    # Options frame
    options=Frame(right, bg="white")
    options.place(x=0, y=551, width=1110, height=90)
    # Options frame division
    if updateFlag==False:
        sg.editCriminal_reset()
        sg.editCrime_reset()
    # Submit button
    submit_frame=Frame(options, bg="white")
    submit_frame.place(x=0, y=0, width=277, height=89)
    if sg.editCriminal_status()==True or sg.editCrime_status()==True or addMoreCrimes==True:
        submit_button=Button(submit_frame, state=DISABLED, text="Submit", font=("helvetica",20,"bold"), command=submit_function)
    else:    
        submit_button=Button(submit_frame, text="Submit", cursor="hand2", font=("helvetica",20,"bold"), command=submit_function)   
    submit_button.place(x=65, y=15, width=150, height=60)

    if sg.editCriminal_status()==True or addMoreCrimes==True:
        try:
            database=mysql.connector.connect(host="localhost", username="Admin", password="password", database="criminal_identification_db")
            cursor=database.cursor()
            cursor.execute("SELECT c_id,c_name,c_parentage,c_address,c_gender,c_dob,c_height,c_weight,c_occupation from criminal WHERE c_id=%s",(idValue,))
            result=cursor.fetchone()
            crim_id.set(result[0])
            crim_name.set(result[1])
            crim_parentage.set(result[2])
            crim_address.set(result[3])
            crim_gender.set(result[4])
            crim_dob.set(result[5])
            crim_height.set(result[6])
            crim_weight.set(result[7])
            crim_occupation.set(result[8])
            database.commit()
            database.close()
        except Exception as es:
            messagebox.showerror("Error",f"An exception has occured {str(es)}")
    if sg.editCrime_status()==True:
        try:
            database=mysql.connector.connect(host="localhost", username="Admin", password="password", database="criminal_identification_db")
            cursor=database.cursor()
            cursor.execute("SELECT c_id,c_name,c_parentage,c_address,c_gender,c_dob,c_height,c_weight,c_occupation from criminal WHERE c_id=%s",(idValue,))
            result=cursor.fetchone()
            crim_id.set(result[0])
            crim_name.set(result[1])
            crim_parentage.set(result[2])
            crim_address.set(result[3])
            crim_gender.set(result[4])
            crim_dob.set(result[5])
            crim_height.set(result[6])
            crim_weight.set(result[7])
            crim_occupation.set(result[8])
            cursor.execute("SELECT cr_id from crime WHERE cr_type=%s",(crimeValue,))
            crimeid=cursor.fetchone()
            crimeid=crimeid[0]
            cursor.execute("SELECT cr_id, crime_date, arrest_date from crimes_committed WHERE c_id=%s and cr_id=%s ",(idValue, crimeid,))
            result=cursor.fetchone()
            crime_id.set(result[0])
            crime_type.set(crimeValue)
            crc_crimedate.set(result[1])
            crc_arrestdate.set(result[2])
            database.commit()
            database.close()
        except Exception as es:
            messagebox.showerror("Error",f"An exception has occured {str(es)}")
    criminalState=sg.editCriminal_status()
    crimeState=sg.editCrime_status()
    if crimeState==True:
        crimeIdentification=crime_id.get()
    addMoreState=addMoreCrimes
    def update_function():
        if criminalState==True:
            if crim_name.get()=="" or crim_parentage.get()=="" or crim_address.get()=="" or crim_gender.get()=="" or crim_dob.get()=="" or crim_height.get()=="" or crim_weight.get()=="" or crim_occupation.get()=="" :
                messagebox.showerror("Error","All Fields Are Required")
            else:
                try:           
                    database=mysql.connector.connect(host="localhost", username="Admin", password="password", database="criminal_identification_db")
                    cursor=database.cursor()
                    cursor.execute("UPDATE criminal SET c_name=%s,c_parentage=%s,c_address=%s,c_gender=%s,c_dob=%s,c_height=%s,c_weight=%s,c_occupation=%s WHERE c_id=%s", (crim_name.get(),crim_parentage.get(),crim_address.get(), crim_gender.get(), crim_dob.get(), crim_height.get(), crim_weight.get(), crim_occupation.get(),crim_id.get(),))
                    database.commit()                            
                    database.close()
                    # Clear all data
                    clearAllDataEntryFields()
                    messagebox.showinfo("Success","Changes updated successfully")
                except Exception as es:
                    messagebox.showerror("Error",f"An exception has occured {str(es)}")
        elif crimeState==True:
            if crime_type.get()=="" or crc_crimedate.get()=="" or crc_arrestdate.get()=="":
                messagebox.showerror("Error","All Fields Are Required")
            else:
                try:           
                    database=mysql.connector.connect(host="localhost", username="Admin", password="password", database="criminal_identification_db")
                    cursor=database.cursor()
                    cursor.execute("update crimes_committed set cr_id=%s, crime_date=%s, arrest_date=%s where c_id=%s and cr_id=%s",(int(crime_id.get()),crc_crimedate.get(),crc_arrestdate.get(),crim_id.get(),crimeIdentification,))
                    database.commit()                            
                    database.close()
                    # Clear all data
                    clearAllDataEntryFields()
                    messagebox.showinfo("Success","Changes updated successfully")
                except Exception as es:
                    messagebox.showerror("Error",f"An exception has occured {str(es)}")
        elif addMoreState==True:
            if sg.addCrime_status()==False:
                messagebox.showerror("Error","No crime added")
            else:
                try:
                    database=mysql.connector.connect(host="localhost", username="Admin", password="password", database="criminal_identification_db")
                    cursor=database.cursor()
                    for i in range(0,len(crimeList)):
                        # Acquiring the crime id from crimes committed table
                        cursor.execute("select cr_id from crime where cr_type=(%s)",(crimeList[i],))
                        cr_id=cursor.fetchone()
                        cr_id=cr_id[0]
                        # Inserting criminal id, crime id, crime date and arrest date into crimes committed table
                        cursor.execute("insert into crimes_committed values(%s,%s,%s,%s)", (crim_id.get(), cr_id, crimeCommittedList[i][0], crimeCommittedList[i][1],))               
                        database.commit()
                    database.close()
                    # Clear all data
                    clearAllDataEntryFields()
                    messagebox.showinfo("Success","Crime records added successfully")
                except Exception as es:
                    messagebox.showerror("Error",f"An exception has occured {str(es)}")
        global addMoreCrimes
        addMoreCrimes=False
        global updateFlag
        updateFlag=False
    # Update button
    update_frame=Frame(options, bg="white")
    update_frame.place(x=278, y=0, width=277, height=89)
    if sg.editCriminal_status()==False and sg.editCrime_status()==False and addMoreCrimes==False:
        update_button=Button(update_frame, state=DISABLED, text="Update", font=("helvetica",20,"bold"), command=update_function)
    else:
        update_button=Button(update_frame, text="Update", cursor="hand2", font=("helvetica",20,"bold"), command=update_function)
    update_button.place(x=65, y=15, width=150, height=60)

    def resetAllFields():
        clearAllDataEntryFields()

    # Reset button
    reset_frame=Frame(options, bg="white")
    reset_frame.place(x=556, y=0, width=277, height=89)
    if sg.editCriminal_status()==True or sg.editCrime_status()==True or addMoreCrimes==True:
        reset_button=Button(reset_frame, state=DISABLED, text="Reset", font=("helvetica",20,"bold"), command=resetAllFields)
    else:
        reset_button=Button(reset_frame, text="Reset", cursor="hand2", font=("helvetica",20,"bold"), command=resetAllFields)
    reset_button.place(x=65, y=15, width=150, height=60)
    # Cancel button
    Cancel_frame=Frame(options, bg="white")
    Cancel_frame.place(x=834, y=0, width=277, height=89)
    if sg.editCriminal_status()==True or sg.editCrime_status()==True or addMoreCrimes==True:
        Cancel_button=Button(Cancel_frame, state=DISABLED, text="Cancel", font=("helvetica",20,"bold"), command=registerModule)
    else:
        Cancel_button=Button(Cancel_frame, text="Cancel", cursor="hand2", font=("helvetica",20,"bold"), command=registerModule)
    Cancel_button.place(x=65, y=15, width=150, height=60)
    
    def resetAllFlags():
        global updateFlag
        updateFlag=False
        global addMoreCrimes
        addMoreCrimes=False
        sg.editCriminal_reset()
        sg.editCrime_reset()
    resetAllFlags()
    

