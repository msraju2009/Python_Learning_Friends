l1 = [10, 20, 30, 40, 50]
l2 = [10, 30, 40, 20, 60, 50]
l3 = [10, 40, 20, 50, 30]
# list comparison in multiple ways
import collections

# collections return value and frequency
print((collections.Counter(l1)) == collections.Counter(l2))
print(collections.Counter(l3))  #
print((collections.Counter(l1)) == collections.Counter(l3))

# second way is sorting elements and compare
l1.sort()
l2.sort()
l3.sort()
print(l1, "\n", l2, "\n", l3)
print(l1 == l2)
print(l1 == l3)
# third way is to convert into sets and then compare
l1 = [10, 20, 30, 40, 50]
l2 = [10, 30, 40, 20, 60, 50, 50]
l3 = [10, 40, 20, 50, 30, 30, 30]
a = set(l1)
b = set(l2)
c = set(l3)
z = a.difference(b)  # get the difference element
print(z)
if a == b:
    print("L1 is equal to L2")
elif a == c:
    print("L1 is equal to L3")
else:
    print("None of the elements are equal")

l1 = [10, 20, 30, 40, 50]
l2 = [10, 30, 40, 20, 60, 50, 50]
l3 = [10, 40, 20, 50, 30, 30, 30]
# res = [x for x in l1+l2]
res = [x for x in l1 + l2 if x not in l1 or x not in l2]
print(res)
# a=[10,20,40,50]
# for item in a:
#     print(item)
a_dict = {'color': 'red', 'fruit': 'apple', 'pet': 'lion'}
print(a_dict['fruit'])
# iterate through dict keys
for item in a_dict:
    print(item)
# iterate through dict and return keys in a list
for item in a_dict.keys():
    print(item)
# iterate through dict and return values in a list
for value in a_dict.values():
    print(value)
# iterate and get key and its value from dict
for k in a_dict:
    print("Key is {} and its value is {} ".format(k, a_dict[k]))
for k, v in a_dict.items():
    print(k, v)

prices = {'apple': 20.40, 'orange': 10.50, 'banana': 90.04}
for k in list(prices.keys()):
    # prices[k] = v**2
    if k == 'orange':
        del prices[k]
print(prices)

courses = {'bash': {'classes': 10, 'hours': 2, 'fee': 500},
           'PHP': {'classes': 30, 'hours': 2, 'fee': 1500},
           'Angular': {'classes': 10, 'hours': 2, 'fee': 1000}}

# angular 10 2 1000
for each_course in courses:
    # print(cour)
    if each_course == "PHP":
        classes = courses[each_course]['classes']
        hours = courses[each_course]['hours']
        fee = courses[each_course]['fee']
        print("Course {} has classes {} and hours {} and fees {} ".format(each_course, classes, hours, fee))
import json

with open('mockaroo-user-data.json') as input_data:
    output_data = json.load(input_data)
employee_names = []
for element in output_data:
    first_name = element['first_name']
    last_name = element['last_name']
    ip_address = element['ip_address']
    gender = element['gender']  # get the employees whose gender is female
    if gender == "Female":
        employee_names.append(first_name + last_name)
print(employee_names)

with open('employees.json') as input_data:
    output_data = json.load(input_data)

results = output_data['data']
for each_element in results:
    emp_name = each_element['employee_name']
    emp_age = each_element['employee_age']
    profile_image = each_element['profile_image']
    if profile_image != "":  # get the employees whose profile image is there
        print("EmpName is {} and his age is {} ".format(emp_name, emp_age))

with open('comments.json') as input_data:
    output_data = json.load(input_data)
for each_element in output_data:
    body = each_element['body']
    name = each_element['name']
    email = each_element['email']
    if 'Fuck' in body:  # get the name and email of the person who spoke bad word
        print(name, email)
