#PySpam, automated message spamming in python
"""This is a program designed to continually send messages via applescript on your mac after you enter a phone number, message, and amount of times you'd like to send the message.
You are currently working with PySpam 0.8.1.
Planned improvements:
add network connectivity checking
rewrite the main function more cleanly and with less looping
Improvements from PySpam 0.7 are:
added an init function that makes sure the applescript file is available, reduces the need for an additional file in the package as it will be created if nonexistent
added a function to return a properly formatted phone number for easier readability
"""
import os

#Define some global variables we'll be needing throughout the script
global amount
amount = ""
global number
number = ""
global message
message = ""

#making sure everything is ready to go before sending the messages
def init():
#checking for the applescript to send messages with
    try:
#creating the file
      f = open("sendMessage.applescript", "x")
#append the script into the file
      script = """on run {targetBuddyPhone, targetMessage}
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy targetBuddyPhone of targetService
        send targetMessage to targetBuddy
    end tell
end run"""
      f.write(script)
      f.close()
#ok, we're good
    except FileExistsError:
#user already has this script
      pass
#to be added: check for internet connectivity before continuing

def format(arg):
#to return formatted phone numbers
    arg = str(arg)
    n1 = arg[0:3]
    n2 = arg[3:6]
    n3 = arg[6:10]
    return f"{n1}-{n2}-{n3}"

def main():
 breaker = 1
 while breaker == 1:
  while True: #Loop until a break command  is encountered so we can factor in all possible input conditions and prompt for revised input if any of them fail to be met
   global number
   number = input("Enter a number to text\n")
   if (number.isdigit()): #making sure the number entered is an actual number and not text
    number = int(number) #type casting to integer for length comparison
    if len(str(number)) < 10: #if there are less than ten digits
     print("that doesn't seem like a 10 digit phone number. Try entering it again")
    else:
     break
   elif "-" in number: #if somebody used dashes 
    print("Oh that's okay, you don't have to use dashes.")
   else: #the entered string was not a number or equal to done
    print("Sorry, but there was an error.")
  global message
  message = input("Enter the message you'd like to spam\n")
  while True:
   global amount
   amount = input("Enter the amount of messages to spam\n")
   if (amount.isdigit()):
    amount = int(amount)
    break
   else:
    print("Please type a number")
  while True:
   print(f"""Ok. So, just to make sure, you would like to send
{message}
to {format(number)}
{amount} times?""")
   confirm = input("Type yes or no""")
   if confirm == "yes":
    print("all right, cool")
    breaker = 0
    break
   elif confirm == "no":
    print("Ok, sorry, something got messed up. Try typing the information you want again.")
    break
   else:
    print("please type yes or no")


init()

main()

while True:
 times_sent = 0
 print("Here we go")
 while times_sent < amount:
  command = f"osascript sendMessage.applescript {number} \"{message}\""
  os.system(command)
  times_sent += 1
  print(times_sent,"messages sent")
 print("Ok. Done.")
 break

a = ""
while a.upper() != "NO":
  a = input("Would you like to spam somebody else now?")
  if a.upper() == "YES":
   main()
  else:
   print("Please type yes or no")

