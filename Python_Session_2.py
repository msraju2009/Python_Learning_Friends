str_name = "MadhuSudhanaRaju"
# It converts the first character of a string to uppercase
print(str_name.capitalize())  # Madhusudhanaraju
# It is used to count the number of times a specific value appears in the string
print(str_name.count('a'))  # 4
# value, start, end
print(str_name.count('a', 0, 6))  # 1
# It checks if the string is ending with specified value then it returns True
print(str_name.endswith("ju"))  # True
# It is used to find the presence of a specified value in a string
print(str_name.find('S'))  # 5
# It checks if all the characters are alphabet (a-z) then returns True
print(str_name.isalpha())  # True
# It checks if all the characters are alphanumeric then returns True
str_name = "MadhuSudhanaRaju$"
print(str_name.isalnum())  # false
# It checks if all the characters are digits then returns True
print(str_name.isdigit())  # False
# It checks if all the characters are in lowercase then returns True
print(str_name.islower())  # False
# It checks if all the characters are whitespaces then returns True
print(str_name.isspace())  # False
# It is used to replace specified word or phrase into another word or phrase in the string
print(str_name.replace("M", "R"))  # RadhuSudhanaRaju$
str_name = "Madhu Sudhana Raju"
print(str_name.split())  # ['Madhu', 'Sudhana', 'Raju']
str_name = "Madhu-Sudhana-Raju"
print(str_name.split('-'))  # ['Madhu', 'Sudhana', 'Raju']
# It is used to split the string and make a list of it. Splits at the line breaks.
str_name = '''Madhu
           Sudhana
           Raju'''
print(str_name.splitlines())  # ['Madhu', '           Sudhana', '           Raju']
str_name = "Madhu_Sudhana_Raju--"
print("hello")
print(str_name.strip('-'))  # Madhu_Sudhana_Raju
# It is used to swap uppercase string to lowercase or vice versa
str_name = "Madhu_Sudhana_Raju"
print(str_name.swapcase())  # mADHU_sUDHANA_rAJU
str_name = "Madhu sudhana raju"
#	It converts initial letter of each word to uppercase
print(str_name.title())  # Madhu Sudhana Raju
print(str_name.lower())  # madhu sudhana raju
print(str_name.upper())  # MADHU SUDHANA RAJU
# 01234
# Hello
# -5-4-3-2-1

# Type conversions for int, float and complex

PI = 3.147
print(type(PI))
print(int(PI))
money = 1000
print(float(money))
print(complex(6))
print(bin(64))
print(oct(8))
print(hex(255))

name = "madhuSudhanaRaju"
print(name)

print(dir(name))

print(name.capitalize())

print(name.count('a'))

print(name.count('a', 0, 10))
# import os
# file_name = os.path.abspath(os.path.dirname(__file__))
# print(file_name)
file_names = ['Raju.json', 'r.txt', 'c.py', 'hello.js']
for file in file_names:
    if file.startswith("R") or file.startswith('r'):
        print(file)
#
#
name = "MADHU"
print(name.find('Raju'))
print(name.isupper())
print(name.islower())
print(name.lower())
num = "93490340"
print(num.isdigit())

print(name.replace('D', 'X'))
village = "Kadapa-Andhra-Prakasham"
print(village.split('-'))
#
#
characters = '''
        asdifjasdf
        asdfjajfas
        asdjfsadfasfafwegerg
'''

for item in characters.splitlines():
    print(item.strip())

name = "Madhu-Sudhana-Raju---"
print(name.strip('-'))

a = "hello"
b = "Gello"
print(id(a))
print(id(b))
#
print(a == b)
#
# print("hello"!='Hello')
# fruit = 'bananana'
print(a is not b)

# for ch_a in a:
#     if ch_a not in b:
#         print(ch_a)

str_item = "Hello"
#   01234
# -5-4-3-2-1
# string slicing start:stop(n-1):step

print(str_item[1:])
print(str_item[:3])
print(str_item[1:200])
print(str_item[-1])
print(str_item[:-3])
print(str_item[-3:])
a = 10
b = 30
# a value is 10 and b value is 30
print("a value is {} and b value is {} ".format(a, b))

print("a value is {0} and b value is {1} ".format(b))
