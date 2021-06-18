import time
import msvcrt
#Requires Install
import pyperclip

print("Welcome to ThatCalculator! ")

#conversion class
class convert:
 def distance():
  global answer
  current_d = input("what is the current distance measurement you have? You can press: \n C, for centimeters \n I, for Inches \n F, for feet \n E, for Meters \n K, for kilometers \n Or M, for miles")
  x = input("How many:")
  x = int(x)
  convert_d = input("what distance unit would you like to convert to? You can press: \n C, for centimeters \n I, for Inches \n F, for feet \n E, for Meters \n K, for kilometers \n Or M, for miles")
  if current_d == "c":
   cm={
    "i" : 0.393701,
    "f" : 0.0328084,
    "e" : 0.01,
   "k" : 0.00001,
    "m" : 0.0000160934
    }
   for g in cm:
    if g == convert_d:
     h = cm.get(g)
     answer = x * h
     print(answer)

  elif current_d == "i":
   inch={
    "c" : 2.54,
    "f" : 12,
    "e" : 39.3701,
    "k" : 39370.1,
    "m" : 63360
    }
   for g in inch:
    if g == convert_d:
     h = inch.get(g)
     answer = x / h
     print(answer)

  elif current_d == "f":
   foot={
    "c" : 0.0328084 ,
    "i" : 0.0833333 ,
    "e" : 3.28084,
    "k" : 3280.84 ,
    "m" : 5280
    }
   for g in foot:
    if g == convert_d:
     h = foot.get(g)
     answer = x / h
     print(answer)

  elif current_d == "e":
   met={
    "c" : 0.01,
    "i" : 0.0254,
    "f" : 0.3048,
    "k" : 1000,
    "m" : 0.621371 
    }
   for g in met:
    if g == convert_d:
     h = met.get(g)
     answer = x / h
     print(answer)

  elif current_d == "m":
   mile={
    "c" : 160934,
    "i" : 63360,
    "f" : 5280,
    "e" : 1609,
    "k" : 1.609
    }
   for g in mile:
    if g == convert_d:
     h = mile.get(g)
     answer = x * h
     print(answer)

  elif current_d == "k":
   km={
    "c" : 100000,
    "i" : 39370,
    "f" : 3281,
    "e" : 1000,
    "m" : 0.621371 
    }
   for g in km:
    if g == convert_d:
     h = km.get(g)
     answer = x * h
     print(answer)


 def time():
  global answer
  current_d = input("what is the current value of time you have? You can press: \n s, for seconds \n m, for minutes \n h, for hours \n d, for days \n w, for weeks \n or y, for years")
  x = input("How Many:")
  convert_d = input("what value of time do you wish to convert to? You can press: \n s, for seconds \n m, for minutes \n h, for hours \n d, for days \n w, for weeks \n or y, for years")
  if current_d == "s":
   sec={
    "m" : 60,
    "h" : 3600,
    "d" : 86400,
   "w" : 604800,
    "y" : 31536000
    }
   for g in sec:
    if g == convert_d:
     h = sec.get(g)
     answer = x / h
     answer = int(answer)
     print(answer)

  elif current_d == "m":
   min={
    "s" : 0.0166667 ,
    "h" : 60,
    "d" : 1340,
    "w" : 9380,
    "y" : 525600
    }
   for g in min:
    if g == convert_d:
     h = min.get(g)
     answer = x / h
     answer = int(answer)
     print(answer)

  elif current_d == "f":
   hour={
    "s" :0.000277778,
    "m" : 0.0166667,
    "d" : 24,
    "w" : 168,
    "y" : 8760
    }
   for g in hour:
    if g == convert_d:
     h = hour.get(g)
     answer = x / h
     print(answer)

  elif current_d == "e":
   met={
    "c" : 0.01,
    "i" : 0.0254,
    "f" : 0.3048,
    "k" : 1000,
    "m" : 0.621371 
    }
   for g in met:
    if g == convert_d:
     h = met.get(g)
     answer = x / h
     print(answer)

  elif current_d == "m":
   mile={
    "c" : 160934,
    "i" : 63360,
    "f" : 5280,
    "e" : 1609,
    "k" : 1.609
    }
   for g in mile:
    if g == convert_d:
     h = mile.get(g)
     answer = x * h
     print(answer)

  elif current_d == "k":
   km={
    "c" : 100000,
    "i" : 39370,
    "f" : 3281,
    "e" : 1000,
    "m" : 0.621371 
    }
   for g in km:
    if g == convert_d:
     h = km.get(g)
     answer = x * h
     print(answer)





class calculater:
 def add():
   global answer
   answer = x + z
   print(answer)

 def subtract():
   global answer
   answer = x - z
   print(answer)

 def multiply():
   global answer
   answer = x * z
   print(answer)

 def divide():
   global answer
   answer = x / z
   print(answer)


def main():
 print("Would you like to: \n 1. Perform basic arethmetic, \n or, \n 2: Convert between units? \n (Press the corresponding number)")
 while True:
  if msvcrt.kbhit():
   choice = msvcrt.getch()
   if choice == b'1':
    print("OK!")
    calculate()
    break
   elif choice == b'2':
    print("OK!")
    converter()
    break

 pyperclip.copy(answer)
 time.sleep(1)
 print("Alert!: This answer has been copied to your clipboard.")
 time.sleep(2)
 print("would you like to calculate anything else? Y/N")
 while True:
  if msvcrt.kbhit():
   again = msvcrt.getch()
   if again == b'y':
    main()
   elif again == b'n':
    print("all right! See you later then!")
    time.sleep(1.3)
    exit()
   else:
    print("you must  press Y, for yes, or N, for no")


#write a function to do all of the calculating
def calculate():
#Call our first three functions which ask the user of our calculator for numbers to calculate and how they want them to be calculated
  finp()
  sinp()
  op()

def finp():
#because we are calling this function later in the program, we have to define x as a global variable so Python will know what it is when we refer to it
  global x
#We have to make sure the number the user enters is actually a number and not a letter. So, we'll be using Python's built-in try function to attempt to TypeCast whatever is put in during program execution to a type float. It is important that we cast to type float so that users can calculate decimals.
  try:
   x = float(input("enter your first number"))
#If that fails, then
  except ValueError: 
   print("Sorry, That Is Not A Number")
#Call the function again until they put a number in
   finp()

#Now defining sinp, or second input
def sinp():
#Just as before, we're declaring Z as a global variable so Python knows what we're talking about when we call it later
  global z
  z = input("Enter your second number")
  if len(z) == 0:
   handle_convert_choice()
  elif len(z) >= 1:
   try:
    z = float(z)
   except ValueError:
    print("Sorry, that's not a number")
    sinp()

#Now, we're going to write a function that will ask the user which operation they'd like to perform.
def op():
#You know the drill, define this variable as a global one
  global y
  print("Select your operation: You can enter: \n A, for adition \n S, for subtraction. \n M, for Multiplication. \n Or D, for division.")
  while True:  
   if msvcrt.kbhit():
    y = msvcrt.getch()
    if y == b'a':
     calculater.add()
     break
    elif y == b's':
     calculater.subtract()
     break
    elif y == b'd':
     calculater.divide()
     break
    elif y == b'm':
     calculater.multiply()
     break
    else:
     print("Sorry, that is not an available operation")


def converter():
#Ask the user what kind of converting they want to do and assign it to the variable ct, or convert type
  global answer
  print("What type of conversion would you like to do? You can press: \n D, for Distance \n T, for time \n V, for volume \n M, for mass \n Or P, for tempature")
#Here we write conditionals for each input and call functions from the class we defined earlier depending
#Enclosing this code in a loop for the purposes of the autoadvance feature. We are calling kbhit from the msvcrt which returns true if the user pressed a key. We then assign the getch function from the same lib to a variable, and write if statements for if that variable equals a cerain key press
  while True:
   if msvcrt.kbhit():
    ct = msvcrt.getch()
    if ct == b'd':
     convert.distance()
     break
    elif ct == b't':
     convert.time()
     break
    elif ct == b'v':
     convert.volume()
     break
    elif ct == b'm':
     convert.mass()
     break
    elif ct == b'p':
     convert.temperature()
     break
#If the user didn't type any of those keys
    else:
     print("Sorry, that is not an available conversion type")



main()