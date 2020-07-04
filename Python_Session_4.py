list_items = ['Monday', 'madhu', 2, 4.5, True, 5 + 6j]
# array_numbers = [1,2,3,4,5,6]
l = []

L = list('abcdcsfs2342')
print(L)
print(type(L))
l = list((1, 2, 3, 56))
print(l)
import time

flattened_list = [[0, 1, 2], [3, 4, 5]]

colors = ['red', 'blue', 'green', 'yellow']
# start:end(n-1):step
print(colors[0:])
print(colors[-1:])
print(colors[0:2])
print(colors[2:-1])
for items in colors:
    time.sleep(2)
    print("item is {} ".format(items))

# immutable - whos value can be changed
list_colors = ['red', 'blue', 'green', 'yellow']
print(list_colors[0])
list_colors[0] = 'magenta'
print(list_colors)
# mutable - whos value cant be changed
tuple_colors = ('red', 'blue', 'green', 'yellow')
tuple_colors[0] = 'magenta'
print(tuple_colors)
s = 'Madhu'
s[0] = 'R'
print(s)
# HOW TO ASSIGN
# HOW TO ITERATE
# HOW TO ADD/MODIFY/UPDATE VALUES
new_list = [1, 2, 3, 4, True]
list_colors = ['red', 'blue', 'green', 'yellow']
list_colors.append("magenta")
list_colors.append("black")
list_colors.append(new_list)
print(list_colors)
list_colors.extend(new_list)
list_colors.insert(0, 'Orange')
print(list_colors)
mod_list = list_colors + new_list
print(mod_list)

print(list_colors * 2)
list_colors = ['red', 'blue', 'green', 'yellow']
print(len(list_colors))
x = list_colors.pop(1)
print(x)
print(len(list_colors))

list_colors.remove('red')
print(list_colors)
del list_colors[10:50]
print(list_colors.clear())
print(len(list_colors))
list_colors = ['red', 'blue', 'green', 'yellow']
new_list = []
#
for index, value in enumerate(list_colors):
    if value == "blue":
        new_value = list_colors[index]
        new_list.insert(0, new_value)
    new_list.append(value)
new_list.remove('blue')
print(new_list)
# index returns the value where the key is present 
print(list_colors.index('blue'))

print('bsaslue' not in list_colors)
print('blue' not in list_colors)
