from datetime import datetime #referencing UTC time
from datetime import date #defining first day of the year
import ctypes #setting background
import os #for getting the current directory and deleting files

#define dates/times
now = datetime.utcnow()
then = date(now.year, 1, 1)
difference = now.date()-then

#calculate which hour of the year it is
picNum = difference.days * 24 + now.hour + 1
picNumStr = (4-len(str(picNum)))*"0"+str(picNum)

#get current path
currentDirectory = os.path.dirname(os.path.abspath(__file__))
path = currentDirectory +"/"+str(now.year)+"/"+picNumStr+".jpg"

#print out status
print("Hour: "+str(picNumStr))
print("UTC time: "+str(now)[:-10])
print("Path: "+path)

#set background
ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)

#Delete all previous pictures
for picNum in range(picNum):
    picNumStr = (4-len(str(picNum)))*"0"+str(picNum)
    try:
        os.remove(currentDirectory +"/"+str(now.year)+"/"+picNumStr+".jpg")
        print("removing: "+picNumStr+".jpg")
    except:
        None
