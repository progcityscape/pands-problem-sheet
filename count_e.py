# Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.
# The program should take the filename from an argument on the command line. 

# author John Kelleher

# assuming that python will not distinguish between 'E' and 'e' (this was proved incorrect)
# will be using emma by jane austen as the source text

# https://docs.python.org/3/library/fileinput.html to input file using command line
# https://pythonexamples.org/python-count-number-of-characters-in-text-file/ to read the total number of characters in a text file
# https://stackoverflow.com/questions/27401474/pydev-3-8-or-3-9-requires-utf-8-encoding-to-be-manually-set-in-python-3-code-un to set the encoding correctly to prevent errors
# https://www.informit.com/articles/article.aspx?p=2979063&seqNum=11#:~:text=To%20access%20command-line%20arguments,first%20import%20the%20sys%20package.&text=You%20can%20then%20refer%20to,to%20a%20list%20named%20argv.&text=In%20either%20case%2C%20argv%20refers,arguments%2C%20all%20stored%20as%20strings.

# bring in the filename as a variable
# https://www.informit.com/articles/article.aspx?p=2979063&seqNum=11#:~:text=To%20access%20command%2Dline%20arguments,first%20import%20the%20sys%20package.&text=You%20can%20then%20refer%20to,to%20a%20list%20named%20argv.&text=In%20either%20case%2C%20argv%20refers,arguments%2C%20all%20stored%20as%20strings.

import sys

FILENAME = (sys.argv[1])

'''
import fileinput
for line in fileinput.input(encoding="utf-8"):
print (line)
'''    
        
'''
# set filename variable
FILENAME = "emma_jane_austen.txt"
'''
# extra code to count the overall number of characters
# open file in read mode

with open(FILENAME, mode='rt', encoding='utf-8') as f:

# read the content of file
# strip any spaces
    data = f.read().replace(" ", "")
        
# get the length of the data
    number_of_characters = len(data)
    
    print(f'Number of characters in {FILENAME}: {number_of_characters}')

# count the number of occurences in a python string https://datagy.io/python-count-number-of-occurrences-in-a-string/#:~:text=a%20String%20with%20.-,count(),string%20associated%20with%20the%20method.
# creates a dictionary
    from collections import Counter
    collection = Counter (data)

# read the number of E's from the dictionary
# https://www.w3schools.com/python/python_dictionaries_access.asp

number_of_e = collection ["e"]
number_of_E = collection ["E"]
total_e = number_of_e + number_of_E
print (f'The character "e\E" appears {total_e} times')

