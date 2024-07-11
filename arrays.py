empty_list = []
my_list = [1,2,3,4,5]

first_element = my_list[0]
last_element = my_list[-1]

my_list[0] = 10 # [10,2,3,4,5]

# add to end
my_list.append(6) # [10,2,3,4,5,6]

# insert at specific position:
my_list.insert(1,20) # [10,20,3,4,5,6]

# removing first instance of an element:
my_list.remove(20) # [10,3,4,5,6]

# remove by index:
my_list.pop(2) # [10,3,5,6]

# remove last element:
my_list.pop() # [10,3,5]


list1 = [1,2,3]
list2 = [4,5,6]

# concatenating elements:
concatenated_list = list1 + list2 # [1,2,3,4,5,6]

# repeating lists:
repeated_list = list1*3 # [1,2,3,1,2,3,1,2,3]

# checking membership:
is_present = 2 in list1 # true

# list slicing:
sub_list = list1[1:3] # [2,3]

# list comprehensions:
squares = [x**2 for x in range(5)]

# iterating through a list:
for element in list1:
    print(element)

# iterating with index
for index, element in list1:
    print(f"Index: {index}, Element: {element}")


# BUILT-IN functions:

# length:
length = len(list1) # 3

# max value in a list:
maxValue = max(list1) # 3

# min value in a list:
minValue = min(list1) # 1

# get sum of all elements combined:
total = sum(list1)

# sorting a list:
sorted_list = sorted(list1)

# sorting a list in place:
list1.sort()

# reversing a list:
reversed_list = list1[::-1]

# reversing a list in place:
list1.reverse() # [3,2,1]