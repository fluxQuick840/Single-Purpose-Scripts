# Single Purpose Scripts
A collection of scripts that do one thing.
## What Are All These?
This repo contains a collection of small scripts and programs I've written over the years that were kind of only for one purpose. Download, use, modify, enjoy however you want. Use them as inspiration for your own code, as a starting point for a similar idea of yours, or heck, just grab one and turn it in as a homework assignment for a python course. 
Just kidding. Don't do that, but otherwise, go nuts. Keep reading for a description of each scrit.
**Please note that I apologize, but much of this code was written a long time ago and thus does not display proper technique, conform to proper formatting, or otherwise look pretty. But it works**
### PySpam Ver. 0.8.1
Taken directly from the comments at the top of the script:  
This is a program designed to continually send messages via applescript on your mac after you enter a phone number, message, and amount of times you'd like to send the message.
You are currently working with PySpam 0.8.1.
Planned improvements:
add network connectivity checking
rewrite the main function more cleanly and with less looping
Improvements from PySpam 0.7 are:
added an init function that makes sure the applescript file is available, reduces the need for an additional file in the package as it will be created if nonexistent
added a function to return a properly formatted phone number for easier readability  
This was just a small script I wrote while bored one day. As you read above, it requires a mac, so as to be able to leverage an applescript, but if you do have a mac, don't go too crazy with it.
### Wednesday
Remember: "It's Wednesday, my dudes. AAAAAAAAAAAAAAA?" Well so do I. I wrote this script based off the previous one to send that exact text to any number I put fed it, for 12 hours, on the hour, on any given Wednesday. Again, have fun, and ask before you send somebody 12 messages they don't want to receive.
### MergeUtil
As a blind person, it's very hard to work with video. Even simply merging an audio track with a video track. It's frustrating, to say the least, when I can't use a video production app because it's inaccessible. So I wrote this program. What I'll usually need to do is somehow modify the audio track of a video, yet leave the video alone. And I'd prefer to work with the audio in my DAW of choice. So, once I have that all done and exported, I run MergeUtil, tell it where the video and audio files I want merged are, and let it go. Enjoy!  
This script requires [MoviePy](https://pypi.org/project/moviepy/)
### Passgen
A simple password generator. Enter a length and your off. Does not use the secure generating algorithm, uses random to choose from a list of characters. For this reason you may or may not actually want to use this for actual passwords, it was more of an experimental fun project.
### Calc
Oh, speaking of experimental projects, here is the first ever full program I wrote. It's a calculator, as many people's first program is, but this one is unique because I didn't simply use the input function, some if statements, and the print function. I wrote my own functions, which I did not even understand how to do, and called them based on what the user entered. I even started writing a class, at least a year before I even knew what objects were. What a mess. But enjoy!
### File Generator
Simply generates empty files you may need for testing/other purposes. Run the script, select a directory, then type away all the filenames you want. Type done to quit. (No files named "done" can be created at this time)
### RPS
A way overcomplicated Rock, Paper, Scissors game that I wrote for a school assignment one time. Execute and beat the computer.
### blaaaaaaaaa
Sometimes, after a long day, it can be hard to remember what you're doing. It can be even harder to remember important details you need, so that you can even do whatever it is you're doing... like the name of the python script you're trying to write. If you close your command prompt and reopen it, the dreadful has occured; all your command history is gone! What will you do?  
Place this file, bla.py in the directory of any program you're working on. Name it whatever you want, but I've found that naming it bla helps because it's the only thing in my head after hours at my computer. So I can just type:  
python bla.py  
and I'll be presented with the name of the most recently modified python file, which is most likely the one I was last working on and need the name of so I can test.
### cutoff
I wrote this script to enforce a bedtime on myself. During the summertime when I was still in high school, I'd stay up way late on the phone or the computer doing who knows what online. And I could never pull myself away, so I made the computer do that for me.  
I wrote this script which would warn me one hour, thirty minutes, then five minutes, then one minute before my cutoff time, and when that happened, I would have it execute a command that disabled my network driver. Just in case I got smart and tried to turn it back on, I had the program try to access google every so offten. If it could, it ran the command again.  
Then at a specified time in the morning, the script would run a command to turn my wireless card back on, and I would have a good night's sleep. If you struggle with anything similar, this may help.
## Questions? Comments? 
[Contact Me](mailto:quantomrush34@icloud.com)
