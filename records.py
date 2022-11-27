from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import serialGenerator as sg
import os
from register import updateFunction
import commonStructure

def recordsModule():
    # Right frame
    right=Frame(commonStructure.root, width=1116, height=646, bd=2, bg="white", relief=RIDGE)
    right.place(x=251,y=121)

    # Search bar frame
    searchbar_frame= LabelFrame(right, text="Search", fg="red", bg="lightgreen")
    searchbar_frame.place(x=0, y=0, width=1112, height=642)
    choice=StringVar()
    options= ["Select search filter ","Criminal ID", "Criminal Name"]
    searchby_entry_selection=ttk.OptionMenu(searchbar_frame, choice, *options)
    searchby_entry_selection.place(x=20, y=20)
    searchby_entry=ttk.Entry(searchbar_frame)
    searchby_entry.place(x=150, y=20)
    # Search results
    def search_results():
        if choice.get()=="Criminal ID":
            if searchby_entry.get()=="":
                messagebox.showerror("Error!", "Enter criminal ID")
            if searchby_entry.get()!="":
                #Clear the treeview list items
                for item in criminal_info.get_children():
                    criminal_info.delete(item)
                try:
                    database=mysql.connector.connect(host="localhost", username="Admin", password="password", database="criminal_identification_db")
                    cursor=database.cursor()
                    if crimes_variable.get()=="1":
                        cursor.execute("SELECT c.c_id,c.c_name,c.c_parentage,c.c_address,c.c_gender,c.c_dob,c.c_height,c.c_weight,c.c_occupation,cr.cr_type,crc.crime_date,crc.arrest_date from criminal as c join crimes_committed as crc on c.c_id=crc.c_id join crime as cr on cr.cr_id=crc.cr_id WHERE c.c_id=%s",(searchby_entry.get(),))
                    else:
                        cursor.execute("SELECT c_id,c_name,c_parentage,c_address,c_gender,c_dob,c_height,c_weight,c_occupation from criminal WHERE c_id=%s",(searchby_entry.get(),))
                    result=cursor.fetchall()
                    if len(result) != 0:
                        for x in result:
                            criminal_info.insert("",END,values=x)
                    else:
                        messagebox.showinfo("Info","ID not found")
                    database.commit()
                    database.close()
                except Exception as es:
                    messagebox.showerror("Error",f"An exception has occured {str(es)}")

        elif choice.get()=="Criminal Name":
            if searchby_entry.get()=="":
                messagebox.showerror("Error!", "Enter criminal name")
            if searchby_entry.get()!="":
                #Clear the treeview list items
                for item in criminal_info.get_children():
                    criminal_info.delete(item)
                try:
                    database=mysql.connector.connect(host="localhost", username="Admin", password="password", database="criminal_identification_db")
                    cursor=database.cursor(searchby_entry.get())
                    if crimes_variable.get()=="1":
                        cursor.execute("SELECT c.c_id,c.c_name,c.c_parentage,c.c_address,c.c_gender,c.c_dob,c.c_height,c.c_weight,c.c_occupation,cr.cr_type,crc.crime_date,crc.arrest_date from criminal as c join crimes_committed as crc on c.c_id=crc.c_id join crime as cr on cr.cr_id=crc.cr_id WHERE c.c_name LIKE (%s)",("%"+searchby_entry.get()+"%",))
                    else:
                        cursor.execute("SELECT c_id,c_name,c_parentage,c_address,c_gender,c_dob,c_height,c_weight,c_occupation from criminal WHERE c_name LIKE (%s)",("%"+searchby_entry.get()+"%",))
                    result=cursor.fetchall()
                    if len(result) != 0:
                        for x in result:
                            criminal_info.insert("",END,values=x)
                    else:
                        messagebox.showinfo("Info","Name not found")
                    database.commit()
                    database.close()
                except Exception as es:
                    messagebox.showerror("Error",f"An exception has occured {str(es)}")
        else:
            messagebox.showerror("Error!", "Make proper selections")

    # Search button
    search_button=ttk.Button(searchbar_frame, text="Search", command=search_results)
    search_button.place(x=300, y=20)

    # Deletion
    def delete():
        response=messagebox.askokcancel(title="Warning!", message="Are you sure you want to delete this data?", icon="warning")
        if response==True:
            try:
                # Deletion of data from the treeview widget and retreival of criminal id from the selected row
                # if no row is seleted before clicking the delete button it will trigger an exception
                selected_data=criminal_info.selection()
                id=criminal_info.item(selected_data)['values'][0]
                criminal_info.delete(selected_data)
                # Deletion of face biometrics
                try:
                    database=mysql.connector.connect(host="localhost", username="Admin", password="password", database="criminal_identification_db")
                    cursor=database.cursor()
                    cursor.execute("SELECT sample_id from criminal WHERE c_id=%s",(id,))
                    sampleID=cursor.fetchone()
                    database.close()
                    count=1
                    while count<=100:
                        os.remove(f"C:\\Users\\Admin\\Desktop\\Criminal identification system with facial recognition\\facial recognition samples\\{sampleID[0]}.{count}.jpg")
                        count+=1
                    messagebox.showinfo("Success","Biometrics deleted successfully")
                except Exception as es:
                        messagebox.showerror("Error",f"An exception has occured {str(es)}")
                # Deletion of data from the database
                try:
                    database=mysql.connector.connect(host="localhost", username="Admin", password="password", database="criminal_identification_db")
                    cursor=database.cursor()
                    cursor.execute("DELETE from criminal WHERE c_id=%s",(id,))
                    database.commit()
                    database.close()
                    messagebox.showinfo("Success","Record Deleted successfully")
                except Exception as es:
                        messagebox.showerror("Error",f"An exception has occured {str(es)}")
            except Exception as es:
                    messagebox.showerror("Error","No Item Selected")
    # Delete button
    delete_button=ttk.Button(searchbar_frame, text="Delete", command=delete)
    delete_button.place(x=400, y=20)

    # Deletion of crimes committed
    def deleteCrime():
        response=messagebox.askokcancel(title="Warning!", message="Are you sure you want to delete this data?", icon="warning")
        if response==True and crimes_variable.get()=="1":
            try:
                # Deletion of data from the treeview widget and retreival of criminal id from the selected row
                # if no row is seleted before clicking the delete button it will trigger an exception
                selected_data=criminal_info.selection()
                id=criminal_info.item(selected_data)['values'][0]
                crime=criminal_info.item(selected_data)['values'][9]
                criminal_info.delete(selected_data)
                # Deletion of data from the database
                try:
                    database=mysql.connector.connect(host="localhost", username="Admin", password="password", database="criminal_identification_db")
                    cursor=database.cursor()
                    cursor.execute("SELECT cr_id from crime WHERE cr_type=%s",(crime,))
                    crimeid=cursor.fetchone()
                    crimeid=crimeid[0]
                    cursor.execute("DELETE from crimes_committed WHERE c_id=%s and cr_id=%s ",(id, crimeid,))
                    database.commit()
                    database.close()
                    messagebox.showinfo("Success","Record Deleted successfully")
                except Exception as es:
                        messagebox.showerror("Error",f"An exception has occured {str(es)}")
            except Exception as es:
                    messagebox.showerror("Error","No Item Selected")
        elif response==True and crimes_variable.get()=="":
            messagebox.showerror("Error","No Crime Selected")
    # Delete crime button
    deleteCrime_button=ttk.Button(searchbar_frame, text="Delete Crime", command=deleteCrime)
    deleteCrime_button.place(x=500, y=20)

    def editCriminal():
        try:
            # if no row is seleted before clicking the edit criminal button it will trigger an exception
            selected_data=criminal_info.selection()
            id=criminal_info.item(selected_data)['values'][0]
            # Editing the criminal data using register module update function
            updateFunction("criminal", id, "0")
        except Exception as es:
            messagebox.showerror("Error","No Item Selected")
    # Edit criminal details button
    editCriminal_button=ttk.Button(searchbar_frame, text="Edit Criminal", command=editCriminal)
    editCriminal_button.place(x=300, y=60)
    def editCrime():
        if crimes_variable.get()=="1":
            try:
                # if no row is seleted before clicking the edit criminal button it will trigger an exception
                selected_data=criminal_info.selection()
                id=criminal_info.item(selected_data)['values'][0]
                crime=criminal_info.item(selected_data)['values'][9]
                # Editing the criminal data using register module update function
                updateFunction("crime", id, crime)
            except Exception as es:
                messagebox.showerror("Error",es)
        elif crimes_variable.get()=="":
            messagebox.showerror("Error","No Crime Selected")
           
    # Edit crime details button
    editCrime_button=ttk.Button(searchbar_frame, text="Edit Crime", command=editCrime)
    editCrime_button.place(x=400, y=60)

    # Add more crimes function
    def addMoreCrimes():
        try:
            # if no row is seleted before clicking the add more crimes button it will trigger an exception
            selected_data=criminal_info.selection()
            id=criminal_info.item(selected_data)['values'][0]
            # Adding new crime details for a criminal using update function
            updateFunction("add", id, "0")
        except Exception as es:
            messagebox.showerror("Error","No Item Selected")
    # Add more crimes for criminals that already exist in the records
    addMoreCrimes_button=ttk.Button(searchbar_frame, text="Add More Crimes", command=addMoreCrimes)
    addMoreCrimes_button.place(x=500, y=60)

    # Show crimes function
    def showCrimes():
        if crimes_variable.get()=="1":
            for item in criminal_info.get_children():
                    criminal_info.delete(item)
            try:
                database=mysql.connector.connect(host="localhost", username="Admin", password="password", database="criminal_identification_db")
                cursor=database.cursor()
                if choice.get()=="Criminal ID" and searchby_entry.get()!="":
                    cursor.execute("SELECT c.c_id,c.c_name,c.c_parentage,c.c_address,c.c_gender,c.c_dob,c.c_height,c.c_weight,c.c_occupation,cr.cr_type,crc.crime_date,crc.arrest_date from criminal as c join crimes_committed as crc on c.c_id=crc.c_id join crime as cr on cr.cr_id=crc.cr_id WHERE c.c_id=%s",(searchby_entry.get(),))
                elif choice.get()=="Criminal Name" and searchby_entry.get()!="":
                    cursor.execute("SELECT c.c_id,c.c_name,c.c_parentage,c.c_address,c.c_gender,c.c_dob,c.c_height,c.c_weight,c.c_occupation,cr.cr_type,crc.crime_date,crc.arrest_date from criminal as c join crimes_committed as crc on c.c_id=crc.c_id join crime as cr on cr.cr_id=crc.cr_id WHERE c.c_name LIKE (%s)",("%"+searchby_entry.get()+"%",))
                else:
                    cursor.execute("SELECT c.c_id,c.c_name,c.c_parentage,c.c_address,c.c_gender,c.c_dob,c.c_height,c.c_weight,c.c_occupation,cr.cr_type,crc.crime_date,crc.arrest_date from criminal as c join crimes_committed as crc on c.c_id=crc.c_id join crime as cr on cr.cr_id=crc.cr_id")
                result=cursor.fetchall()
                if result != None:
                    for x in result:
                        criminal_info.insert("",END,values=x)
                else:
                    messagebox.showinfo("Info","No Records Found")
                database.commit()
                database.close()
            except Exception as es:
                messagebox.showerror("Error",f"An exception has occured {str(es)}")
        elif crimes_variable.get()=="0":
            recordsModule()
    # Crimes Checkbox
    crimes_variable= StringVar()
    crimes_checkbox= ttk.Checkbutton(searchbar_frame, text='Show Crimes', variable=crimes_variable, onvalue=1, offvalue=0, command=showCrimes)
    crimes_checkbox.place(x=600, y=20)
    
    # Results frame
    results_frame=Frame(right, width=1090, height=600)
    results_frame.place(x=10, y=127, width=1095, height=450)
    # Make changes to the fonts in add crimes section
    style = ttk.Style()
    style.configure("add_crimes.Treeview", font=("helvetica",10)) 
    style.configure("add_crimes.Treeview.Heading", font=("helvetica",13))

    criminal_info=ttk.Treeview(results_frame, style="criminal_info.Treeview",column=("id","name","parentage","address","gender","dob","height","weight","occupation","crime","crime_date","arrest_date"), show="headings")
    
    # Column properties
    # Column heading properties
    criminal_info.column("id", stretch=NO, anchor=CENTER, width=80, minwidth=80)    
    criminal_info.heading("id", text="Criminal ID",anchor=CENTER)

    criminal_info.column("name", stretch=NO, anchor=CENTER, width=100, minwidth=100)
    criminal_info.heading("name", text="Name",anchor=CENTER)

    criminal_info.column("parentage", stretch=NO, anchor=CENTER, width=100, minwidth=100)
    criminal_info.heading("parentage", text="Parentage",anchor=CENTER)

    criminal_info.column("address", stretch=NO, anchor=CENTER, width=100, minwidth=100)
    criminal_info.heading("address", text="Address",anchor=CENTER)

    criminal_info.column("gender", stretch=NO, anchor=CENTER, width=60, minwidth=60)
    criminal_info.heading("gender", text="Gender",anchor=CENTER)

    criminal_info.column("dob", stretch=NO, anchor=CENTER, width=100, minwidth=100)
    criminal_info.heading("dob", text="DOB",anchor=CENTER)

    criminal_info.column("height", stretch=NO, anchor=CENTER, width=60, minwidth=60)
    criminal_info.heading("height", text="Height",anchor=CENTER)

    criminal_info.column("weight", stretch=NO, anchor=CENTER, width=60, minwidth=60)
    criminal_info.heading("weight", text="Weight",anchor=CENTER)

    criminal_info.column("occupation", stretch=NO, anchor=CENTER, width=100, minwidth=100)
    criminal_info.heading("occupation", text="Occupation",anchor=CENTER)

    criminal_info.column("crime", stretch=NO, anchor=CENTER, width=100, minwidth=100)
    criminal_info.heading("crime", text="Crime",anchor=CENTER)

    criminal_info.column("crime_date", stretch=NO, anchor=CENTER, width=100, minwidth=100)
    criminal_info.heading("crime_date", text="Crime Date",anchor=CENTER)

    criminal_info.column("arrest_date", stretch=NO, anchor=CENTER, width=100, minwidth=100)
    criminal_info.heading("arrest_date", text="Arrest Date",anchor=CENTER)

    criminal_info.pack(side=LEFT, fill=BOTH, expand=1)

    # Vertical scrollbar for added crimes
    scrollbar = ttk.Scrollbar(criminal_info, orient=VERTICAL, command=criminal_info.yview)
    criminal_info.configure(yscroll=scrollbar.set)
    scrollbar.pack(side = RIGHT, fill=BOTH)
    
    # Display database records
    def select():
        try:
            database=mysql.connector.connect(host="localhost", username="Admin", password="password", database="criminal_identification_db")
            cursor=database.cursor()
            cursor.execute("SELECT c_id,c_name,c_parentage,c_address,c_gender,c_dob,c_height,c_weight,c_occupation from criminal")
            result=cursor.fetchall()
            if len(result) != 0:
                for x in result:
                    criminal_info.insert("",END,values=x)

            database.commit()
            database.close()
        except Exception as es:
            messagebox.showerror("Error",f"An exception has occured {str(es)}")

    select()




    