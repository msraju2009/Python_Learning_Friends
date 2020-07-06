# A dictionary holds key-value pairs.
# Declare it in curly braces, with pairs separated by commas. Separate keys and values by a colon(:).
# Dictionaries are mutable like lists, it can grow and shrink based on demand
# Dicationries are accessed by keys like we access list elements using index
person = {
    'city': 'bglore',
    'age': 30
}
print(type(person))
#
list_items = [1, 2, 3, 5, [4, 3, 1]]
print(list_items[-1])
#
print(person['city'])
#
user = {
    'name': 'Bob',
    'age': 25,
    'job': 'Dev',
    'city': 'Bglore',
    'email': 'msraju2009@gmail.com'
}
print(len(user))

# keys must be unique

person = {
    'city': 'bglore',
    'age': 30,
    'city': 'hyd'
}
print(person)  # only city hyd will be there, last value will be replaced

# # keys must be immutable , keys should not be mutable
D = {
    (1, 2): 25,
    True: 'a',
    'name': 'b',
}
print(D[True])
# as list can grow or shrink, we cant use mutable object in dictionary as key
# values can be of same value
B = {'city': 'bglore',
     'age': 30,
     'percentage': 30
     }
print(B)
# list of tuple items
L = [('name', 'madhu'), ('age', 30), ('job', 'Developer')]
convert_list_dict = dict(L)
print(convert_list_dict)
# tuple of list items
tuple_of_items = (['name', 'madhu'], ['age', 30], ['job', 'Developer'])
convert_tuple_dict = dict(tuple_of_items)
print(convert_tuple_dict)
#
# create a dictionary using dict constructor
dict_obj = dict(city='bglore', age=30, percentage=30)

# nested dictionary
college = {'student_1': {'age': 30, 'branch': 'IT', 'grade': 'C'},
           'student_2': {'age': 20, 'branch': 'CSE', 'grade': 'B'},
           'location': 'bglore'
           }

# convert list into dictionary
names_list = ['madhu', 'kalyan', 'deepu', 'sai', 'vijay', 'RP', 'karthik']
city_list = ['bglore', 'kadapa', 'andhra', 'atp', 'rajamundy', 'prakasham']

print(dict(zip(names_list, city_list)))

# Create a dictionary with default values from a list , use .fromkeys method
default_value = 'python_programmers'
dict_obj = dict.fromkeys(names_list, default_value)
print(dict_obj)
A = {'city': 'bglore',
     'age': 30,
     'percentage': 30
     }
print(B['asdfajksdfnak'])  # this raises valueError if key is not found
print(B['city'])
print(B.get('adsfvasdfasdf'))  # get will return None if key is not found
B['city'] = 'hyd'
print(B)
B = {'email': 'msraju2009@gmail.com',
     'age': 35,
     'Name': 'Madhu'
     }
A.update(B)  # merge two dictionaries using update function
print(A)
# remove an item by key
removed_element = B.pop('age')  # use pop if we want to get the value that needs to be removed
print(B)
del B['age']  # del will not return any value
print(removed_element)
B.clear()
print(B)

person_object = {'madhu': 'bglore', 'kalyan': 'kadapa', 'deepu': 'andhra', 'sai': 'atp', 'vijay': 'rajamundy',
                 'RP': 'prakasham'}
print(len(person_object))

print(list(person_object.keys()))  # returns list of keys
print(list(person_object.values()))  # returns list of values
print(person_object['madhu'])
print(list(person_object.items()))  # returns list of key,value pairs in tuple format

even_nums = [2, 34, 6, 8, 10]
print(20 in even_nums)
print(even_nums[0])
name = "MadhuSUdhanaRaju"
# iterating through dictionary using for loop
for ele in person_object:
    print(ele)
# iterating through dictionary and print key,value using for loop
for key in person_object:
    print(key, person_object[key])

# iterating through dictionary using for loop and get the keys,values using .items() function
# for key,value in person_object.items():
#      print("Key is {} and its value is {} ".format(key,value))

person_object = {'madhu': 'bglore', 'kalyan': 'kadapa', 'deepu': 'andhra', 'sai': 'atp', 'vijay': 'rajamundy',
                 'RP': 'prakasham'}

print('madhu' in person_object)
print('tpt' in person_object.values())

# list comparison
# tuple comparison
# dictionary comparison
# lists of dictionaries
# tuple of dictionries
# dictionaries of dictionaries

# to be be given assignments
