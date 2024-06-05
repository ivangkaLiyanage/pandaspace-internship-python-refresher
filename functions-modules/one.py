# Write a function that takes a list of numbers and returns a list of the squares of those numbers.
# create a function that accepts a parameter of list
# square the list by looping through it
# return the result

def squareNums(*numList):
    sqrNum = []
    for num in numList:
        val = num**2
        sqrNum.append(val)
    return sqrNum


# num_list = [2, 4, 5, 6, 8]
# print(squareNums(num_list))
print(squareNums(2, 4, 5, 6, 8))
