# Create a program that takes a string input and prints the number of characters.
# take user input
# get length of the user input 
# count charcs and ommit white space
# print charcs

usrSenten = input('Enter a sentence to get the number of characters: ')
chars = len(usrSenten) - usrSenten.count(' ')
print(chars)