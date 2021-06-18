#Cutoff, to disconnect you from the internet so you'll go to bed
#Third Party Dependencies:
#win10toast
#playsound
#can all be installed via "pip install"
from win10toast import ToastNotifier
import urllib.request 
from playsound import playsound
import os
import datetime
import time

def time_trigger():
#Calculating the current time
    now = datetime.datetime.now()
    sec_list = [3600, 60, 1]
    global now_secs
    now_secs = sum([a*b for a,b in zip(sec_list, [now.hour, now.minute, now.second])])
    wait_time = 84600 - now_secs #the difference between now and 84600 seconds past midnight (or 11:30)
    if wait_time < 0:
        wait_time += 86400 #add a day's worth of time to a negative integer to make the time difference still work
    print("Waiting",wait_time,"seconds until 11:30") #if you'd like to adjust this to your own preferred bedtime, swap out my 84600 value for its number of seconds past midnight
    time.sleep(wait_time)
    playsound("C:/Windows/Media/Alarm10.wav", block=False) #your one hour warning
    time.sleep(1800)
    playsound("C:/Windows/Media/Alarm10.wav", block=False) #your 30 minute warning
    time.sleep(1500) 
    playsound("C:/Windows/Media/Alarm10.wav", block=False) #your 5 minute warning
    time.sleep(240)
    playsound("C:/Windows/Media/Alarm10.wav") #your one minute warning
    time.sleep(60)
    net_stuff()


def net_stuff():
#turn off the wifi
    os.system('cmd /c "net stop WlanSvc"')
    wifi = "off"
    while True:
        try: 
#to open a connection to google.com
            urllib.request.urlopen("https://www.google.com")
            wifi = "on" 
        except: #connection couldn't be opened
            pass #do nothing because that's the result we wanted
        if wifi == "on":
            toaster = ToastNotifier()
            toaster.show_toast("Wi-Fi disabled","Wi-Fi was disabled after cutoff.py detected it was on", duration=4)
#turn it back off
            os.system('cmd /c "net stop WlanSvc"')
access the seconds variable from the time_trigger function
        global now_secs
        if now_secs > 28800: #it's 7 o'c
            os.system('cmd /c "net start WlanSvc"') #ok, you can have your wifi back again. You should have gotten 8 hours of sleep by now
            break #out of the loop that keeps checking to make sure wifi is off
        time.sleep(45) #until we check to see if the wifi is on or not again

while True:
    time_trigger() #so this repeats every night
