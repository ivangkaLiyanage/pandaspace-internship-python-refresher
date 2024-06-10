# Implement a program that handles division by zero using try-except blocks.
# write try and except
# print 

def zeroFunc(x):
    try:
        ans = x/0
        return ans
    except:
        return 'Error, try again'
    
def zeroFunc2(x):
    try:
        ans = x/0
        return ans
    except ZeroDivisionError:
        return "Oops!  That was no valid number.  Try again..."

print(zeroFunc(5))
print(zeroFunc2(5))

