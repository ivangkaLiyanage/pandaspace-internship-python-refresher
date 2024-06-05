#  Create a module that contains a function to generate a random password.
# use built in random generator 
# make a password of 8 characters
# print the password

# https://pynative.com/python-generate-random-string/
import random
import string

def randPassword(length):
    password = string.ascii_letters + string.digits + string.punctuation
    result = ''.join(random.choice(password) for i in range(length))
    return result
print('Random password: ' + randPassword(8))

# def randPassword2(length):
#     # password = string.ascii_letters + string.digits + string.punctuation
#     # result = ''.join(random.choice(password) for i in range(8))
    
#     choice = [string.ascii_letters, string.digits, string.punctuation]
#     results = ''
#     for i in range(length):
#         results.join(random.choice(choice))
    
#     return results

# print('Random password: ' + randPassword2(8))