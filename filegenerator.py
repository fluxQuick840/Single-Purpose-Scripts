#File Generator, quickly generate empty files. 
from time import sleep
import tkinter as tk
from tkinter.filedialog import askdirectory

print("Select a folder to generate files into.")
sleep(1)
#open native folder selection dialog
root = tk.Tk()
root.withdraw()
path = askdirectory(title="Select Folder For Generated Files")
#continually prompt for file creation
while True:
    filename = input("Enter a filename or done to quit")
    if filename.upper() == "DONE":
        break #exit the loop
    elif filename == "":
        print("Please enter a filename")
        continue #jump back to the top of the loop
    try:
        f = open(path+"/"+filename, "x") #Creating the file with user specified filename
        f.close()
        print(f"{filename} generated successfully")
    except FileExistsError:
        print(f"{filename} already exists")
    except Exception as e: #handle all other exceptions
        print(f"Error creating {filename}. {e}")
print("Ok, exiting...")
sleep(1)
