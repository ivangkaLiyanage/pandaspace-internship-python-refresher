# Write a recursive function to calculate the nth Fibonacci number.
# first create the recursive function
# when the user passes a number check if it is in the sequence
# calculate the user input fibonacci number

# first method
# def getFibonacci(num):
#     if(num < 0):
#         return ('Invalid input')
#     elif(num == 0):
#         return 0
#     elif((num == 1) or (num == 2)):
#         return 1
#     else:
#         return getFibonacci(num-1) + getFibonacci(num-2)


# print(getFibonacci(5))

# second method
def fibonacci(n, memoDict={}):
    if n < 0:
        return 'Invalid input'
    elif n == 0:
        return 0
    elif ((n == 1) or (n == 2)):
        return 1
    elif n in memoDict:
        return memoDict[n]
    else:
        memoDict[n] = fibonacci(n-1, memoDict) + fibonacci(n-2, memoDict)
        return memoDict[n]

print(fibonacci(5)) 
