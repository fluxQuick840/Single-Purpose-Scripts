#gay.py, when the only word you can think of at the command prompt is gay
import os
#this script will find the last modified python script and tell you what it is, so you can remember and execute it
#after a long day of programming, things like that slip your mind, and the only word you can think of is gay
#so, you can now just type: python gay.py and be reminded of the file you're looking for.

path = "c:/users/mason/documents"
time_dict = {}
for i in os.listdir(path):
    if i.endswith(".py"):
        date = os.path.getmtime(i)
        time_dict[i] = date
last_modified = max(time_dict, key=time_dict.get)
filename = last_modified.rsplit("/", 1)
print(f"You're looking for {filename}")