# adding elements to dictionary/assigning values to a dictionary in a traditional way
D = {}
# D[0] = 1
# D[1] = 2
# D[2]= 3
# print(D)
# modifying dictioanry value
# D[2]='madhu'
# print(D)

# Create a dictionary with squares of a number from 1-5
# for x in range(1,6):
#     D[x] = x**2
# print(D)

# using dictionary comprehension, syntax is {key:value for var in iterable}
# d= {x:x**2 for x in range(1,6)}
# print(d)
# iterate through list and create a dict with lower values as key and upper values as value
# st = ['MadHu','SaI','KalYAn']
# D = {x.lower():x.upper() for x in st}
# print(D)
# Converting a list into set for set operation difference
# A =[1,2,4,5]
# B = [1,2,3]
# print(set(A)-set(B))

D = {0: '1', 1: '2', 3: '5', 4: '8'}
# {3:'5',4:'8'}
selected_keys = [3, 4]
removed_key = [3, 4]
# get only selected keys from a dictionary
D = {k: D[k] for k in selected_keys}

# get remaining keys after removing removed_keys
D = {k: D[k] for k in D.keys() - removed_key}
print(D)

colors = {0: 'red', 1: 'blue', 2: 'green'}
# output should be like this {red:0, blue:1, green:2}
# invert mapping/ reverse lookup
rev = {v: k for k, v in colors.items()}
print(rev)

# use enumerate to get index and value from a list to dictionary
D = ['madhu', 'kalyan', 'rp', 'deepak']
di = {k: v for k, v in enumerate(D)}
print(di)

# way of creating a dictionary with some default values to all keys in a dict
D = dict.fromkeys(D, 'bglore')
print(D)

# way of creating a dictionary with some default values to all keys in a dict
D = {k: 'bglore' for k in D}
print(D)

# use zip to combine two lists into a dictionary
first_name = ['madhu', 'raju']
last_name = ['C', 'chejerla']
D = {k: v for (k, v) in zip(first_name, last_name)}
print(D)

# other way using dict constructor
D = dict(zip(first_name, last_name))
print(D)

# dict comprehension using if statement {key:value for var in iterable if condition}

D = {}
for i in range(1, 11):
    if i % 2 == 0:
        D[i] = i ** 2
print(D)
# using dict comprehension
D = {k: k ** 2 for k in range(1, 11) if k < 5}
print(D)


# sample function definition
def hello():
    print("Hello Madhu")


# sample function call
hello()


# sample function with return statement
def addition():
    a, b = 3, 5
    return a + b


# print the function addition output
print(addition())


# function without any statements, using pass keyword
def get_none():
    pass


# functions in python always return None
print(get_none())


# function with two arguments
def get_name(first_name, last_name):
    return first_name + "--->" + last_name


# passing arguments to a function
print(get_name(first_name='Raju', last_name='Madhu'))


# different types of functions in python
# positional arguments
# keyword arguments
# default arguments
# variable length positional arguments (*args)
# variable length positional keyword arguments (**kwargs)

# keyword arguments
def func(name, job):
    print("my name is {} and my job is {} ".format(name, job))


# calling function with keyword arguments
func(job='developer', name='Raju')


# default function
def company(name, location='Bglore'):
    print("My company name is {} and its location is {} ".format(name, location))


# calling default function without argument, this will assign default value to argument
company('Google')
# calling default function with argument
company('Google', location='hyd')


# variable length positional arguments (*args)
def print_args(*args):
    print(args)


print_args('madhu', 'raju', 1, 2, 3, 4, 5, 6, 7, 2, 2)


# variable length positional keyword arguments (**kwargs)
def key_word_function(**kwargs):
    print(kwargs)


key_word_function(name='madhu', job='developer', age=32)
