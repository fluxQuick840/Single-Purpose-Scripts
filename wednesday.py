#It's Wednesday, my dudes. A simple script to send that exact message to whoever you would like on the hour for 12 hours.
#You will need a mac to run this program as messages are sent via applescript

#import required libs
import datetime 
from time import sleep
from sys import exit
import os

#first, check to make sure it's Wednesday
wkday = datetime.datetime.today().weekday() #returns an indexable list of days where Mon is 0
if wkday != 2: #if any other number besides 2
 print("It's not Wednesday, my dude. AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHH!!!!!!! \n Try running this script later when it is.")
 sleep(1)
 exit() #terminate the script

#now that we've made sure it's Wednesday, let's make sure our script will have time to run for the whole twelve hours it's supposed to.
global current #defining current as global since we'll need to access it later
current = datetime.datetime.now() #returns dictionary of date/time values
current_hr = current.hour
if current_hr > 12:
 print("Sorry, it's too late on Wednesday to run this script, it's after 12:00 already.")
 sleep(1)
 exit()

#required info
global message #setting variable as global so we can access it whenever we need it
message = "it's Wednesday, my dudes. AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHH!!!!!!!!!!"
numberlist = [] #creating an empty list which we'll be appending every input number into
#Asking for a phone number and checking its validity
while True: #Loop until a break command  is encountered so we can factor in all possible input conditions and prompt for revised input if any of them fail to be met
 number = input("Enter a number to text, or type 'done' to exit")
 if (number.isdigit()): #making sure the number entered is an actual number and not text
  number = int(number) #type casting to integer for length comparison
  if number < 10		: #if there are less than ten digits
   print("that doesn't seem like a 10 digit phone number. Try entering it again")
  else: #nothing is wrong so go ahead and save that number to our list of numbers to text
   numberlist.append(number)
   print("ok, saved",number)
 elif "-" in number: #if somebody used dashes 
  print("Oh that's okay, you don't have to use dashes.")
 elif number == "done":
  if len(numberlist) == 0: #if there is nothing in the list
   print("Sorry, but you don't appear to have entered any phone numbers.")
  else: #There was at least one phone number entered
   break
 else: #the entered string was not a number or equal to done
  print("Sorry, but there was an error.")
print("Ok, got it. Sending this meme to",len(numberlist),"different numbers")

#function to figure out how long it is until the start of the next hour, used to make sure this runs on the hour exactly no matter when executed.
def wait_time():
#getting the date and time from earlier
 global current
 current_min = current.minute
#find out how many minutes are remaining in the hour
 minute_difference = 60 - current_min
 print("there are",minute_difference,"minutes remaining in this hour. \n To ensure your messages are sent on the hour, this program will sleep for that long.")
#convert that to seconds because the sleep function does not sleep for input minutes
 sleep_secs = minute_difference * 60
 current_sec = current.second
 sleep_secs -= current_sec
 return sleep_secs

#function to send messages
def text(number):
#getting the command we're running into one string
 global message
 command = f"osascript sendMessage.applescript {number} \"{message}\""
#passing that string right into our command line function which executes it in the system shell
 os.system(command)

#putting the program to sleep until the next hour
wait = wait_time() #the result of our function from earlier
sleep(wait)

#defining a variable to keep count of the hours sent
times_sent = 0
while times_sent <= 12:
 for i in numberlist: #loop through the list of numbers and append i to each one in turn
  text(i) #execute the text function with i in the position of the number parameter it was defined with
 times_sent += 1
 sleep(3600) #3600 seconds in an hour
