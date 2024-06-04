# Write a function to find the maximum value in a list.
# create a list with values
# loop through the list
# check if previous val is bigger than the current value
# print the maximum number

num_list = [1, 8, 6, 12, 4, 3, 7]
    
max_val = 0
for num in num_list:
    if(num > max_val):
        max_val = num
print('Maximum value is: ' + str(max_val))
