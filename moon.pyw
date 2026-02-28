from datetime import date, datetime, timezone
from pathlib import Path
import ctypes #setting background
import os #for getting the current directory and deleting files
import configparser #for reading settings file
import cv2

### Grabbing Config ###
pyFilePath = os.path.abspath(__file__)
configDir = os.path.dirname(pyFilePath)
baseConfigPath = os.path.join(configDir, "config.ini")
localConfigPath = os.path.join(configDir, "config.local.ini")
if(os.path.exists(baseConfigPath)):
    print(f"base config at: {baseConfigPath}")
else:
    raise FileNotFoundError(f"Missing required config file: {baseConfigPath}")

config = configparser.ConfigParser()

readPaths = [baseConfigPath]
if os.path.exists(localConfigPath):
    readPaths.append(localConfigPath)
    print(f"local override config at: {localConfigPath}")

config.read(readPaths)

videoFilePath = config['file_paths']['videoFilePath']
print(f"videoFilePath: {videoFilePath}")
imageSaveDir = config['file_paths']['imageSaveDir']
print(f"imageSaveDir: {imageSaveDir}")
imageName = config['file_paths']['imageName']
print(f"imageName: {imageName}")
imageSavePath = imageSaveDir+"/"+imageName
directBgReplace = config['settings']['directBgReplace']
print(f"directBgReplace: {directBgReplace}")
###

def Grab_Frame(frame_index):
    """
    Saves a specific frame from a video file by its 0-based index.
    """
    cap = cv2.VideoCapture(videoFilePath)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Check if the requested frame index is valid
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"total_frames {total_frames}")
    if 0 <= frame_index < total_frames:
        # Set the frame position
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        
        # Read the frame
        ret, frame = cap.read()

        if ret:
            return frame
        else:
            print(f"Error: Could not read frame {frame_index}.")

    else:
        print(f"Error: Frame index {frame_index} is out of range (0-{total_frames-1}).")

    # Release the video capture object
    cap.release()
    cv2.destroyAllWindows() #

def save_frame(frame):
    # Save the frame as an image file
    write_status = cv2.imwrite(imageSavePath, frame)
    if write_status:
        print(f"Frame saved as {imageName} in {imageSaveDir}")
    else:
        print("Error: Image not saved. Check path and permissions.")

#define dates/times
now = datetime.now(timezone.utc)
beginningOfYear = date(now.year, 1, 1)
difference = now.date()-beginningOfYear

#calculate which hour of the year it is
picNum = difference.days * 24 + now.hour# + 1

#print out status
print("UTC time: "+str(now)[:-10])
print("Hour: "+str(picNum))

frame = Grab_Frame(picNum)

#set background
if(directBgReplace == "True"):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, imageSavePath , 0)
else:
    save_frame(frame)
