# Write a script to read a file and print its content line by line.
# create a text file
# open the text file
# read the text file line by line
# print the text file line by line

file = open('newFile.txt', 'w')
file.write("Hello my name is Kooky\nI like cats\nI also like BTS\n")
file.close()

readFile = open('newFile.txt','r')
print('Option 1: ')
print(readFile.read())
readFile.close()

print('\nOption 2: ')
readFile = open('newFile.txt','r')
for line in readFile:
    # strip eliminates the new line
    print(line.strip())   

print('\nOption 3: ')
with open("newFile.txt") as readFile2:
  for item in readFile2:
    print(item.strip())
