# Write a function that takes a list of integers and returns their average, handling any potential errors.
# create a function 
# pass a list of integers as argument
# inside try return it's average
# except for handling error

# print("Method one: ")
# def avgFunc(intList):
#     try:
#         total = 0
#         for num in intList:
#             total += num
#         avg = total/len(intList)
#         return avg
#     except:
#         "Error, check again"

# print(avgFunc([21,23,25]))


# print("Method two: ")
# def avgFunc2(intList):
#     try:
#         avg = sum(intList)/len(intList)
#         return avg
#     except:
#         "Error, check again"

# print(avgFunc2([21,23,25]))

def avgFunc3(intList):
    try:
        total = 0
        for num in intList:
            total += num
        avg = total/len(intList)
        return avg
    except Exception as e:
        return (f"Error: {str(e)}")
        exit(3) # Specify an exit code to indicate an error occurred

print(avgFunc3([21,23,25]))
print(avgFunc3('21,23,25'))
print(avgFunc3(3))
print(avgFunc3((3,1,2,3)))
print(avgFunc3({
    "x":1,
    "y":2
}))


