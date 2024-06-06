#  Write a function to append text to an existing file.
# open the file
# append the text to the exisiting file.

def appendText(txt):
    file = open(txt, 'a')
    file.write('Do not run\nClean the room\nClean the laptop\n')
    file.close()

    readFile = open(txt, 'r')
    for line in readFile:
        print(line.strip())


appendText('three.txt')









