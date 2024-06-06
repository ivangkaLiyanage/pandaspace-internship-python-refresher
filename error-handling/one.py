# Implement a program that handles division by zero using try-except blocks.
# write try and except
# print 

def zeroFunc(x):
    try:
        ans = x/0
        return ans
    except:
        return 'Error, try again'

print(zeroFunc(5))


