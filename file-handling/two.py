# Create a program to count the number of words in a text file.
# create a text file
# add some sentences
# loop through the text file
# omit the white spaces
# count the words

file = open('myTxtFile.txt', 'a')
file.write("Hello my name is Kooky\nI like cats\nI also like BTS")

readFile = open('myTxtFile.txt', 'r')
for words in readFile:
    
wordsCount = 