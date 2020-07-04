# 6 + 4 = 10 # 6 and 4 are operands and + is an operator
'''
Arthimetic operators
Logical Operators
Comparison operators
Bitwise Operators
Assigment Operators
Membership operators
Identify Operators
'''
# ArithmeticOperators
# + - * ** / //

x = 1
y = 2
print("Addition is {} ".format(x + y))
print("Subraction is {} ".format(x - y))
print("Exponent is {} ".format(x ** y))
print("Division is {} ".format(x / y))
print("FloorDivision is {} ".format(x // y))

# Comparison Operators
# == != > < >= <=
#
string_1 = "madhu"
string_2 = "madhuafasf"
print(string_1 == string_2)
print(string_1 != string_2)
print("length of string1 is {} and string2 is {} ".format(len(string_1), len(string_2)))
x = 10
y = 20
print(x > y)
print(x >= y)
print(x <= y)

# Logical Operators
# and or not

b1 = False
b2 = True
print(b1 and b2)
print(b1 or b2)
print(not b1)

# Bitwise Operators
# & | ^ ~ << >>

# 168421
x = 10  # 1010
y = 4  # 0100

print(x & y)

# Assignment operators
# = += -= *= /= **= //=

a = 10
b = 5
a += b  # a= a+b
a -= b  # a= a-b
a *= b  # a=a*b
#

# Membership operators
# in not in
list_of_colors = ['red', 'blue', 'brown']
print('red' in list_of_colors)
print('yellow' not in list_of_colors)

# Identity Operators
# is is not
x = 10
y = 100
print(id(y))
print(id(x))

print(x is not y)

##########################################33
'''
Decision Making Statements and Loops
if , Nested if , if else, if elif else , while, for loop
# if condition

if condition:
   statement
   statement

# Nested if condition
if condition:
   statement
   if condition:
       statement

# if else condition
if condition:
   statement
   statement
else:
   statement
   statement

# if elif else condition
if condition:
   statement
elif condition:
   statement
else:
   statement
   statement

# Ternary operator
variable = statement if condition else statement

while condition:
    statement
    statement
else:
    statement
    ...

'''

x = 10
# indentation is very important in blocks
seva_pass = True
if seva_pass:
    print("You can enter bglore ")
else:
    print("You can't enter bglore ")
x = 10
y = 5
if x > y:
    print("x is greater than y")

# any non-zero or nonempty containers return True
if 7:
    print("777777")
L = [1, 2, 3, 4, 5]
if L:
    print("asdaaaaaaaaaa")

# any zero,none and empty container returns False

if 0:
    print("sdsdfsdfsa")
if None:
    print("adfdfafafafa")
else:
    print('from else')

if L:
    print("Hello")
x = 10
y = 6
z = 5
if x < y or x > z:
    print("X is greater than Y and Z")
else:
    print("X is less than Y and Z")
if x > y:
    print("X is greater than y")
    if x > z:
        print("X is greater than Z")
seva_pass = False
if seva_pass:
    print("you're allowed")
else:
    print("you're not allowed ")
#
seva_pass = True
corona_test = False

if seva_pass or not corona_test:
    print("you're allowed")
elif seva_pass and corona_test:
    print("you will be screened")
else:
    print("You're not allowed to enter bglore")
#
#
choice = int(input("Enter your valid choice "))
print("Your choice is {} ".format(choice))
if choice == 1:
    print("your choice is 1")
elif choice == 2:
    print("your choice is 2")
elif choice == 3:
    print("your choice is 3")
elif choice == 4:
    print("your choice is 4")
elif choice == 5:
    print("your choice is 5")
else:
    print("Invalid choice")

# variable = statement if condition else condition
x, y = 7, 50
print('x is greater') if x > y else print("X is less than Y")

max = x if x > y else y
print("Max value is {} ".format(max))

tuple_var = ('red', 'blue', 'yellow')
list_var = ['red', 'blue', 'yellow']
if 'yellow' in list_var:
    print("color is present")
else:
    print("Not present")
name = "MadhuSudhanaRaju"
print(name.lower())
if "RAJU" in name.lower():
    print("Exists")
else:
    print("Doesnt exists")

# while condition
# else
import time

x = 6
while x:
    print(x)
    time.sleep(2)
    x -= 1  # x=x-1

x = 10
while x:
    print(x)
    x = x - 1
    if x == 3:
        break
while x:
    x = x - 1
    if x % 2 != 0:
        continue
    print(x)
