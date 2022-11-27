from tkinter import *
import commonStructure

def developerModule():
    # Right frame
    right=Frame(commonStructure.root, width=1116, height=646, bd=2, bg="white", relief=RIDGE)
    right.place(x=251,y=121)
    font_family="trebuchet ms"
    font_size="20"
    font_weight="bold"
    
    # Details of the project supervisor 
    supervisor=Frame(right, width=554, height=321, bd=2, bg="white", relief=RIDGE)
    supervisor.place(x=0,y=0)
    supervisorLable=Label(supervisor, bg="white", text="\nProject supervisor\n\nDr. Tasleem Arif\nHead of the department\nDepartment of IT\nBGSBU",font=(font_family,font_size,font_weight) )
    supervisorLable.place(x=100,y=0)

    # Details of the project co-supervisor
    coSupervisor=Frame(right, width=554, height=321, bd=2, bg="white", relief=RIDGE)
    coSupervisor.place(x=556,y=0)
    coSupervisorLable=Label(coSupervisor, bg="white", text="\nCo-Supervisor\n\nMr.Satish Kumar\nAssistant Professor\nDepartment of IT\nBGSBU",font=(font_family,font_size,font_weight) )
    coSupervisorLable.place(x=150,y=0)

    # Details of the project developer
    developer=Frame(right, width=1112, height=320, bd=2, bg="white", relief=RIDGE)
    developer.place(x=0,y=321)
    developerLable=Label(developer, bg="white", text="\nDeveloped by\n\nMir Suhail Ahmad\nDepartment of IT\nBGSBU\nmirsuhail029@gmail.com",font=(font_family,font_size,font_weight) )
    developerLable.place(x=390,y=0)
