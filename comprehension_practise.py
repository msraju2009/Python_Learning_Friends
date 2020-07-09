# import collections
#
# l1 = [10, 20, 30, 40, 50]
# l2 = [10, 20, 30, 50, 40, 70]
# l3 = [10, 20, 50, 40, 30]
# # Counter() function counts the frequency of the items in a list
# # and stores the data as a dictionary in the format <value>:<frequency>
# print(collections.Counter(l1)) # Counter({10: 1, 20: 1, 30: 1, 40: 1, 50: 1})
# print(collections.Counter(l2)) # Counter({10: 1, 20: 1, 30: 1, 50: 1, 40: 1, 70: 1})
# print(collections.Counter(l1) == collections.Counter(l2)) # False
# # True , even if order is not same also matches
# print(collections.Counter(l1) == collections.Counter(l3))
# print(set(l1)) #{40, 10, 50, 20, 30}
# print(set(l3)) # {40, 10, 50, 20, 30}
# l1.sort()
# l3.sort()
# print(l1 == l3) #True
#
# l1 = [10, 20, 30, 40, 50]
# l3 = [50, 10, 30, 20, 40]
# a=set(l1)
# b=set(l3)
# print(a,b)
# print(a==b)
#
#
# l1 = [-10, -20, 30, 40, 50]
# l3 = [50, 75, 30, 20, 40, 69]
# res = [x for x in l1+l3 if x not in l1 or x not in l3]
# print(res)
# new_list= []
# for item in l1:
#     pos = abs(item)
#     new_list.append(pos)
# print(new_list)

# x = set(['x1','rr','x3','y4'])
# y = set(['x1','rr','rr','y4'])
#
# print ("List first: " + str(x))
# print ("List second: " + str(y))
#
# # take difference of two lists
# z = x.difference(y)
#
# print("Difference of first and second String: " + str(z))
#
# number_list = [x for x in range(100) if x%3 == 0 if x%5 == 0]
# print(number_list)

my_list = ['91 9925479326', '18002561245', 'All the best', 'good']
print([i for i in my_list if not i.startswith(('91', '18'))])  # ['All the best', 'good']
