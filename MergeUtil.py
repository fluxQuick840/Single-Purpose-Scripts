from moviepy.editor import *
import tkinter as tk
from tkinter import filedialog
from time import sleep
from os import getlogin
from sys import exit
import msvcrt

def main():
 root = tk.Tk()
 videopath = filedialog.askopenfilename(title="select your video track")
 audiopath = filedialog.askopenfilename(title="Select your audio track of filetype WAV, MP3, or OGG")
 root.withdraw()
 exportname = input("Enter Name Of File To Save To")
 extention = ".mp4"
 exportname = "/music/" + exportname + extention
 user = getlogin()
 fullpath = "c:/users/" + user + exportname
 print("Merging tracks...")
 videotrack = VideoFileClip(videopath)
 audiotrack = AudioFileClip(audiopath)
 merged = videotrack.set_audio(audiotrack)
 merged.write_videofile(fullpath, temp_audiofile="c:/users/public/temp.mp3")
 sleep(5)
 print("Merge complete. This file has been saved in your Music folder")
 sleep(2)

main()

print("Press Q to quit or M to merge more tracks")
while True:
  if msvcrt.kbhit():
   close = msvcrt.getch()
   if close == b'q':
    exit()
   elif close == b'm':
    main()
