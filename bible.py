#Downloads the New International Version Of The Bible From MIT 
import requests
from os import mkdir, chdir

#map book shortcodes to book names and amount of chapters
books = {
"GEN" : ["Genesis", 50],
"EXO" : ["Exodus", 40],
"LEV" : ["Leviticus", 27],
"NUM" : ["Numbers", 36],
"DEU" : ["Deuteronomy", 34],
"JOS" : ["Joshua", 24],
"JDG" : ["Judges", 21],
"RUT" : ["Ruth", 4],
"1SA" : ["1 Samuel", 31],
"2SA" : ["2 Samuel", 24],
"1KI" : ["1 Kings", 22],
"2KI" : ["2 Kings", 25],
"1CH" : ["1 Chronicles", 29],
"2CH" : ["2 Chronicles", 36],
"EZR" : ["Ezra", 10],
"NEH" : ["Nehemiah", 13],
"EST" : ["esther", 10],
"JOB" : ["Job", 42],
"PSA" : ["Psalms", 150],
"PRO" : ["Proverbs", 31],
"ECC" : ["Ecclesiastes", 12],
"SNG" : ["Song of Solomon", 8],
"ISA" : ["Isaiah", 66],
"JER" : ["Jeremiah", 52],
"LAM" : ["Lamentations", 5],
"EZK" : ["Ezekiel", 48],
"DAN" : ["Daniel", 12],
"HOS" : ["Hosea", 14],
"Joel" : ["Joel", 3],
"AMO" : ["Amos", 9],
"OBA" : ["Obadiah", 1],
"JON" : ["Jonah", 4],
"MIC" : ["Micah", 7],
"NAM" : ["Nahum", 3],
"HAB" : ["Habakkuk", 3],
"ZEP" : ["Zephaniah", 3],
"HAG" : ["Haggai", 2],
"ZEC" : ["Zechariah", 14],
"MAL" : ["Malachi", 4],
"MAT" : ["Matthew", 28],
"MRK" : ["Mark", 16],
"LUK" : ["Luke", 24],
"JHN" : ["John", 21],
"ACT" : ["Acts", 28],
"ROM" : ["Romans", 16],
"1CO" : ["1 Corinthians", 16],
"2CO" : ["2 Corinthians", 13],
"GAL" : ["Galatians", 6],
"EPH" : ["Ephesians", 6],
"PHP" : ["Philippians", 4],
"COL" : ["Colossians", 4],
"1TH" : ["1 Thessalonians", 5],
"2TH" : ["2 Thessalonians", 3],
"1TI" : ["1 Timothy", 6],
"2TI" : ["2 Timothy", 4],
"TIT" : ["Titus", 3],
"PHM" : ["Philemon", 1],
"HEB" : ["Hebrews", 13],
"JAS" : ["James", 5],
"1PE" : ["1 Peter", 5],
"2PE" : ["2 Peter", 3],
"1JN" : ["1 John", 5],
"2JN" : ["2 John", 1],
"3JN" : ["3 John", 3],
"JUD" : ["Jude", 1],
"REV" : ["Revelation", 22]}

#make bible directory to store book subdirectories

mkdir("bible")
chdir("bible")

counter = 1
for i in books:
    print("Downloading " + books[i][0])
#create a folder for the book we're in and change to it
    folder = f"{counter} - {books[i][0]}"
    mkdir(folder)
    chdir(folder)
    chapter = 1
#loop to request successive chapters from the webserver until we reach the number stored in the dictionary
    while chapter <= books[i][1]:
        url = f"http://web.mit.edu/jywang/www/cef/Bible/NIV/NIV_Bible/{i}+{chapter}.html"
        response = requests.get(url)
#open a file and write the content into it
        f = open(f"Chapter {chapter}.html", "w", encoding="utf-8")
        f.write(response.text)
        f.close()
        print("Wrote Chapter " + chapter)
        chapter += 1
    chdir("..") #return to the root directory
    counter += 1

