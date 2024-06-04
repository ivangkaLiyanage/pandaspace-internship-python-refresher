# Create a program that takes an integer input and determines whether it is even or odd.
#  get the user input
#  if ihe result is 0 then even
#  else it is odd

val = int(input('Enter a value: '))
if(val % 2 == 0):
    print(str(val) + ' is an even number')
else:
    print(str(val) + ' is an odd number')