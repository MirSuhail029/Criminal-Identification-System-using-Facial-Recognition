def readOldSerial():
    file=open(r"C:\Users\Admin\Desktop\Criminal identification system with facial recognition\resources\serial.txt","r")
    serial=file.read()
    file.close()
    return(serial)
            
def writeNewSerial(serial):
    file=open(r"C:\Users\Admin\Desktop\Criminal identification system with facial recognition\resources\serial.txt","w")
    file.write(serial)
    file.close()

def incrementSerial(serial):
    serial=int(serial)
    serial+=1
    serial=str(serial)
    return serial


biometrics_flag=False
def samples_status():
    return biometrics_flag
def samples_captured():
    global biometrics_flag
    biometrics_flag=True 
def reset_biometrics_flag():
    global biometrics_flag
    biometrics_flag=False

addCrime_flag=False
def addCrime_status():
    return addCrime_flag
def Crime_added():
    global addCrime_flag
    addCrime_flag=True
def reset_crime_flag():
    global addCrime_flag
    addCrime_flag=False

exit_flag=True
def exit_status():
    return exit_flag
def login():
    global exit_flag
    exit_flag=False


editCriminal_flag=False
def editCriminal_status():
    return editCriminal_flag
def editCriminal_set():
    global editCriminal_flag
    editCriminal_flag=True
def editCriminal_reset():
    global editCriminal_flag
    editCriminal_flag=False

editCrime_flag=False
def editCrime_status():
    return editCrime_flag
def editCrime_set():
    global editCrime_flag
    editCrime_flag=True
def editCrime_reset():
    global editCrime_flag
    editCrime_flag=False