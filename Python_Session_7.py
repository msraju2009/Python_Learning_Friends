# Comprehension is a compact way of creating a python data structure from iterators
# List comprehension is a way to build a new list by applying an expression to each item in an iterable

# common way
name = "MadhuSudhanaRaju"
new_list = []
for item in name:
    new_list.append(item)
print(new_list)

# pythonic way
new_list = [item for item in name]
print("using comprehension is {} ".format(new_list))

# common way to add items to a list
L = []
L.append(1)
L.append(4)
L.append(9)
L.append(16)
L.append(25)
print(L)
# another approach to add items to a list
L = []
for item in range(1, 6):
    L.append(item ** 2)
print(L)
# using list comprehension
l = [1, 2, 3, 4, 5]
pyth_way = [item ** 2 for item in range(1, 6)]
print(pyth_way)
# range(start,end(n-1 item),step)
# print each letter in a string three times and print in a list
s = 'MAD'
new_list = []
for item in s:
    new_list.append(item * 3)
print(new_list)
# using list comprehension
str_list = [item * 3 for item in s]
print(str_list)
#

whole_numbers = [-2, -4, -5, 0, 7, 9]
oput = [2, 4, 5, 0, 7, 9]
# convert negative numbers to absolute numbers
L = [abs(x) for x in whole_numbers]
print(L)
# get only numerics
n_str = "Hello 123456 Madhu"
new_ll = [x for x in n_str if x.isdigit()]
print(new_ll)
# using list comprehension convert list items to lower
caps_items = ["A", "M", "C", "D"]
small_items = [item.lower() for item in caps_items]
print(small_items)
# using list comprehension convert list items to upper
small_letters = ['a', 'b', 'c']
caps = [item.upper() for item in small_letters]
print(caps)

# [(1,1),(2,4),(3,9)] # using list comprehension , return output in tuple format
squares_list = [(x, x ** 2) for x in range(1, 4)]
print(squares_list)
# using list comprehension print only first index of each element
words = ["Hello", "Iam", "Madhu", "Python"]
op = ['H', 'I', 'M', 'P']
output = [item[0].lower() for item in words]
print(output)
# using list comprehension print numbers which are greater than 0
whole_numbers = [-2, -4, -5, 0, 7, 9]
L = []
for number in whole_numbers:
    if number >= 0:
        L.append(number)
print(L)
n = [number for number in whole_numbers if number >= 0]
print(n)
# using list comprehension remove non-aqua animal
aqua_animals = ("fish", "whale", "dolphin", "Human")
non_aqua = [item for item in aqua_animals if item != "Human"]
print(non_aqua)

# 1 to 100 which are divisible by 3 and 5

numbers_div = [number for number in range(1, 100) if number % 3 == 0 and number % 5 == 0]
print(numbers_div)
#
# # 1 to 20 even,odd
obj = [(i, "Even") if i % 2 == 0 else (i, "Odd") for i in range(1, 21)]
print(obj)

normal_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []
for outer_list in normal_list:
    for inner_list in outer_list:
        new_list.append(inner_list)
print(new_list)
# example of nested list comprehension
flat_list_compre = [inner_list_item ** 2 for outer_list in normal_list for inner_list_item in outer_list]
print(flat_list_compre)
