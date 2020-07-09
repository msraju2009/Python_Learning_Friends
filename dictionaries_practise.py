# D= {
#     (2,2):25,
#     True : 'a',
#     'name' : 'Bob',
#     }
# #D[2,3] = "E"
# print(D)
# del D['name']
# print((D.values()))
import json

# with open('country_by_religion.json') as input_data:
#     country_by_religion_data = json.load(input_data)
# print(country_by_religion_data,"\n",type(country_by_religion_data))
# hindu_countries = []
# christ_countries =[]
# # iterate through each item in list of dictionaries
# for countries in country_by_religion_data:
#     # get each country dictionary
#     for key in countries:
#         if countries['religion'] == "Hinduism":
#             hindu_countries.append(countries['country'])
#         elif countries['religion'] == "Christianity":
#             christ_countries.append(countries['country'])
# get all hindu countries
# get all christian countries
# get total number of hindu countries
# print(hindu_countries,"\n",len(hindu_countries))
# print(christ_countries,"\n",len(christ_countries))

country_dict = [{
    "country": "Seychelles",
    "religion": "Christianity"
},
    {
        "country": "Sierra Leone",
        "religion": "Islam"
    }]
# new_item = []
# for dict_item in country_dict:
#     for key in dict_item:
#         if key == "religion":
#             print(dict_item[key])
#             new_item.append(dict_item['country'])
# print(new_item)
# if key == "religion":
#     print(dict_item['religion'])
# for key,value in di.items():
#     print(di['religion'])

with open('country_by_population.json') as pop_input_data:
    pop_output_data = json.load(pop_input_data)
# def get_max_value():
#     pop = []
#     zero_pop_countries = []
#     for countries in pop_output_data:
#         for couny in countries:
#             #print(countries['population'])
#             if countries['population'] is not None:
#                 pop.append(countries['population'])
#             elif countries['population'] == 0 :
#                 print(countries['country'])
#                 zero_pop_countries.append(countries['country'])
#     return max(pop),zero_pop_countries,sorted(pop,reverse=True)

# max_pop,zero_country,population = get_max_value()
# print(max_pop,"\n",zero_country,"\n",population)


# get countries whose population is 0
# get countries whose population is None
# get countries population in sorted order
# print(max(pop))

# with open('youtube_result.json') as ip:
#     op = json.load(ip)
# for items in op['items']:
#     id = items['id'] # get the id dictionary info
#     for k in id: # iterate through dictionary ,check if k==videoID
#         if k == "videoId":
#             print(id[k]) # get the value of videoID

# with open('json_test_data_example.json') as ip:
#     op = json.load(ip)
#
# male = []
# female=[]
# for element in op: # iterate through the items in json test data
#     gender = element['gender'] # get the values of gender key
#     if gender == "Male": # if gender key value is Male, store in a male list
#         male.append(element['first_name'])
#     elif gender == "Female":
#         female.append(element['first_name'])
# print(male,female)

# with open('products.json') as ip:
#     op = json.load(ip)
# remove_dollar = []
# for element in op:
#     unit_cost = element['unit_cost'][1:]
#
# for items in pop_output_data:
#     maximum = max(items, key=items.get('population'))
#     print(maximum, items[maximum])
#

dict_item = [{
    "_id": {
        "$oid": "5968dd23fc13ae04d9000002"
    },
    "product_name": "Mountain Juniperus ashei",
    "supplier": "Keebler-Hilpert",
    "quantity": 292,
    "unit_cost": "$8.74"
}, {
    "_id": {
        "$oid": "5968dd23fc13ae04d9000003"
    },
    "product_name": "Dextromathorphan HBr",
    "supplier": "Schmitt-Weissnat",
    "quantity": 211,
    "unit_cost": "$20.53"
}]

# for i in dict_item:
#     for ele in i:
#         supplier = i["supplier"]
#         product_name = i["product_name"]
#     print(supplier,"--->",product_name)
#

with open('users.json') as ip:
    op = json.load(ip)

# for ele in op:
#     for d_item in ele:
#         name = ele['name']
#         phone = ele['phone']
#     print("Name is {} and phone is {} ".format(name,phone))

with open('posts.json') as ip:
    op = json.load(ip)
# for ele in op:
#     for d_item in ele:
#         title = ele['title']
#     if title == "laborum non sunt aut ut assumenda perspiciatis voluptas":
#         print("userID is {} , body is {} ".format(ele['userId'],ele['body']))
#
# with open('comments.json') as ip:
#     op = json.load(ip)
# for ele in op:
#     for d_item in ele:
#         body = ele["body"]
#     if "fuck" in body.lower():
#         print("postID is {} and hist name is {} ".format(ele['postId'],ele['name']))

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}
# dict of dictionaries
# for emp in D:
#     name = D[emp]['name']
#     job = D[emp]['job']
#     print(name,job)
# dictionary of dictionaries
courses = {'bash': {'classes': 10, 'hours': 2, 'fee': 500},
           'PHP': {'classes': 30, 'hours': 2, 'fee': 1500},
           'Angular': {'classes': 10, 'hours': 2, 'fee': 1000}}
# for each_course in courses:
#     classes = courses[each_course]['classes']
#     hours = courses[each_course]['hours']
#     fees = courses[each_course]['fee']
#     print("For {} classes are {}, hours are {} , the fees is {} ".format(each_course, classes,hours,fees))

products = {'t121': {'name': '42" Sony TV', 'brand': 'Sony', 'price': 600},
            'c702': {'name': 'Camera 8989', 'brand': 'Cannon', 'price': 400},
            'm432': {'name': 'Samsung Galaxy j10', 'brand': 'Samsung', 'price': 200}}
Liverpool = {
    'Keepers': {'Loris Karius': 1, 'Simon Mignolet': 2, 'Alex Manninger': 3},
    'Defenders': {'Nathaniel Clyne': 3, 'Dejan Lovren': 4, 'Joel Matip': 5, 'Alberto Moreno': 6, 'Ragnar Klavan': 7,
                  'Joe Gomez': 8,
                  'Mamadou Sakho': 9}
}
# for k, v in Liverpool.items():
#     for k1, v1 in v.items():
#         print(k1)
# for k,v in Liverpool.items():
#     print(v.keys())

with open('employees.json') as ip:
    op = json.load(ip)

for ele in op:
    data = op['data']
    for k in data:
        employee_name = k['employee_name']
        employee_age = k['employee_age']
        profile_image = k['profile_image']
        if profile_image is not None:  # get employees who doesnt not have profile image
            print("Employee {} doesnt have image ".format(employee_name))
