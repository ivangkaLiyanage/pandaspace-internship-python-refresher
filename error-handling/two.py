# Write a function that takes a list of integers and returns their average, handling any potential errors.
# create a function 
# pass a list of integers as argument
# inside try return it's average
# except for handling error

print("Method one: ")
def avgFunc(intList):
    try:
        total = 0
        for num in intList:
            total += num
        avg = total/len(intList)
        return avg
    except:
        "Error, check again"

print(avgFunc([21,23,25]))


print("Method two: ")
def avgFunc2(intList):
    try:
        avg = sum(intList)/len(intList)
        return avg
    except:
        "Error, check again"

print(avgFunc2([21,23,25]))