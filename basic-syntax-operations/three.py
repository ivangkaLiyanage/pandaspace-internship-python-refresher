# Write a function to calculate the factorial of a number.
# get user input
# calc factorial
# print output
import math

def factorial_func():
    val  = int(input('Enter a value to get factorial: '))
    factNum = math.factorial(val)
    print('Factorial of ' + str(val) + ' is ' + str(factNum))

factorial_func()