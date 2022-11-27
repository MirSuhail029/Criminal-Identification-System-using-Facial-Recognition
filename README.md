# Welcome to Criminal Identification System using Facial Recognition (CISFR)
A machine learning project developed in python using Tkinter, OpenCV, Haar Cascade algorithm and LBPH algorithm.
Your system must have a webcam for successful execution of this application.
Before you can use this system, you'll need to download and install:
1. MySQL Community Server. https://dev.mysql.com/downloads/mysql/
2. Python. https://www.python.org/downloads/
3. Visual Studio Code for editing the code and running the application. https://code.visualstudio.com/

Install Python Libraries/Packages/Modules/dependencies (using command prompt)
1. Numpy. Using command -> pip install numpy
2. OpenCV (contrib). Using command -> pip install opencv-contrib-python
3. Pillow. Using command -> pip install pillow
4. Tkcalendar. Using command -> pip install tkcalendar
5. Tkinter Using command -> pip install tk (only if required because Tkinter is installed by default with Python)

Also, you will need to open the program in VSCode and change the paths in various modules in accordance to your system and folder location 
eg:
r"C:\Users\Admin\Desktop\Criminal identification system with facial recognition\facial recognition samples"
						to
r"C:\Users\your pc\some folder\Criminal identification system with facial recognition\facial recognition samples"
You also need to change the username and password in accordance to what you choose to set the username and password to unless you set it to the default values below:
eg:
database=mysql.connector.connect(host="localhost", username="Admin", password="password", database="criminal_identification_db")
						to
database=mysql.connector.connect(host="localhost", username="your username", password="your password", database="criminal_identification_db")


At last you need to create the database and populate some tables using MySql using the SQL commands:

CREATE DATABASE criminal_identification_db;

USE criminal_identification_db;

CREATE TABLE admin(
	username varchar(50) PRIMARY KEY,
    	password varchar(8) NOT NULL
    	);

CREATE TABLE criminal(
	c_id int PRIMARY KEY AUTO_INCREMENT,
    	sample_id varchar(10) NOT NULL,
    	c_name varchar(45) NOT NULL,
    	c_parentage varchar(45) NOT NULL,
    	c_occupation varchar(45) NOT NULL,
    	c_address varchar(45) NOT NULL,
    	c_gender varchar(45) NOT NULL,
    	c_dob varchar(45) NOT NULL,
    	c_height varchar(45) NOT NULL,
    	c_weight varchar(45) NOT NULL
    	);
ALTER TABLE criminal AUTO_INCREMENT = 8715980;
    
CREATE TABLE crime(
	cr_id int PRIMARY KEY AUTO_INCREMENT,
    	cr_type varchar(45) NOT NULL
    	);
ALTER TABLE crime AUTO_INCREMENT = 121;
    
INSERT INTO crime(cr_type) VALUES
	("Assault"),
        ("Homicide"),
        ("Burglary"),
        ("Illegal Drug Trade"),
        ("Kidnapping"),
        ("Embezzlement"),
        ("Tax Evasion"),
        ("Human Trafficking"),
        ("Vandalism"),
        ("Forgery"),
        ("Bribery"),
        ("Robbery")
        ;
    
CREATE TABLE crimes_committed(
	c_id int,
    	cr_id int,
    	crime_date varchar(10) NOT NULL,
    	arrest_date varchar(10) NOT NULL,
    	PRIMARY KEY (c_id,cr_id),
    	FOREIGN KEY (c_id) REFERENCES criminal(c_id) ON DELETE CASCADE, 
    	FOREIGN KEY (cr_id) REFERENCES crime(cr_id) ON DELETE CASCADE
    	);

Now you are all set to run the application. 
Thank you

email: mirsuhail029@gmail.com
github: https://github.com/MirSuhail029
This Application was designed and developed by: 
Mir Suhail Ahmad. BGSBU
under the supervision of Dr Tasleem Arif, Head Of the Department, Department of Information Technology and 
co supervision of Mr Satish Kumar, Assistant Professor, Department of Information Technology. 
