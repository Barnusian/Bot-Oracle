import os
import random

#main function
def select_line(filename):
    #check if file exists
    if os.path.isfile(filename):
        #open file into variable
        with open(filename) as f:
            #select random line from document as list
            lines = list(f)
            return(random.choice(lines).replace("\n",""))
    else:
        #in case of no such file
        return('No file found!')
print(select_line("Text/barts-words.txt"))