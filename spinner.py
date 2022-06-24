#spinner.py: proof of concept for an electronic spinner wheel
import winsound
from time import sleep
from random import shuffle
#again, this is only an example and does not really work well
#but it demonstrates the idea

"""to simulate a real wheel being spun, we will use slowly increasing time delays to make it seem as though the wheel is slowing down as it runs out of energy.
Each time the wheel passes an item, it will beep.
We will simulate this by looping through a list of items and beeping the computer speaker each time our list index increases.
The wheel will stop on an item when it runs out of energy.
We will simulate this by setting a max time value for the amount of time between each item's beep
Each physical wheel spin is different because each spin has different force behind it
To simulate this ,we will randomize the order of the items such that we don't always get the same result if we use the same amount of time"""

items = ["a sexy new smart TV","a gorgeous new iPad pro","3 months of free Apple music","a lifetime netflix subscription","a dell optiplex workstation","an iPhone 13 Pro Max","a brand new M2 Macbook air","a Lenovo Thinkpad Carbon"]
shuffle(items)
i = 0
time = 0.0000001
while time <= 0.3:
    i += 1
    if i == len(items):
        i = 0
    winsound.Beep(500,60)
    sleep(time)
    time += 0.005
winsound.Beep(500,1500)
print(f"Congratulations! You just won {items[i]}!!!")
