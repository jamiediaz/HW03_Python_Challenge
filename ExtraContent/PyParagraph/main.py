import re
import os
import csv


parag = os.path.join("raw_data","paragraph_2.txt")
with open(parag, newline =None) as textfile:
    csvreader = csv.reader(textfile, delimiter=" ")

    words = []
# file = open("raw_data/paragraph_2.txt","r")
    for column in csvreader:
        words = column
        
        print (words)
#print (len(words))


#file.close()
