#Password generator
import pyperclip #to copy passwords to the clipboard
import random #for randomly choosing characters
import string #instead of defining a list of characters

password = "" #to be appended to later
#define string of all characters and convert it to a list
pass_chars = list(string.ascii_letters + string.digits + string.punctuation)
while True:
    try:
        length = int(input("how many characters would you like your password to be?"))
    except:
        print("That... is not a number. Type one of those.")
        continue #Jump back to the top of the loop and try again
    if length > 128:
        print("It is highly unlikely you'll need a password more than 128 characters long.\nEnter a smaller number")
        continue
    elif length < 8:
        print("Come on man, your password needs to be secure.\nType in a bigger number")
        continue
    break
for x in range(0,length): #Loop for the user specified length
    random.shuffle(pass_chars) #Shuffle the list in place
    x = random.choice(pass_chars) #Pick a character
    password += x #Append it to password
#Try to find out if any of the chars in password are numbers or not
num = False
for i in password:
    if i.isdigit():
        num = True
if num == False:
    password = password[:-1] #remove the last character
    password += random.choice(string.digits) #replace it with a number
print("Your password is:\n",password)
pyperclip.copy(password)
print("It has been copied to your clipboard.\nPaste it somewhere safe as this program does not save generated password results")
