# Introduction to Data types in Python

'''
Numbers - int,float,complex
Sequences - string, list, tuple, set
Map - dictionary
'''

a, b, c = 'madhu', 3.147, 3 + 4j
print("a value is {} ".format(a))
print("b value is {} ".format(b))
print("c value is {} ".format(c))

a = b = c = "hello vijay"

print("a value is {} ".format(a))
print("b value is {} ".format(b))
print("c value is {} ".format(c))

a = 'madhu'
b = 3.147
c = 3 + 4j
print("a value is {} ".format(a))
print("b value is {} ".format(b))
print("c value is {} ".format(c))

a, b, c = "hel"
print("a value is {} ".format(a))
print("b value is {} ".format(b))
print("c value is {} ".format(c))

x = 10
print(x)

name = "RP"
print(name)

tuple_data = (1, 2, 4)
print(type(tuple_data))

int_a = 10
float_b = 10.60
compl_a = 4 + 5j
print(int_a, float_b, compl_a)
print(type(int_a), type(float_b), type(compl_a))

name = 'a'
name = "Hello"

print(name)
print(type(name))

# mutable -- its value can change
list_of_numbers = [1, 2, 3, 4, 5, "hello"]
print(list_of_numbers)
print(type(list_of_numbers))

# immutable - its value cant be changed

tuple_of_numbers = (1, 2, 3, 4, 5)
print(tuple_of_numbers)
print(type(tuple_of_numbers))

# sets are used to remove duplicate data in a sequence
set_of_numbers = {4, 5, 2, 5, 6, 2, 12, 4, 5}
print(set_of_numbers)

# dictionaries are key-value pair items.
phone_book_names = {'name': 'madhu',
                    'number': 98563030
                    }
print(phone_book_names['number'])


# User defined data types can be created using class in python

class Employee:
    pass

d = Employee()
print(type(d))  # <type 'instance'>
