# Tuples are immutable objects meaning -- we cant add,delete or change items after tuple is defined

tuple_obj = ('red', 'blue', 'green')
print(tuple_obj[0])

empty_tuple = ()
print(type(empty_tuple))

# singleton tuple
named_tuple = ("Hello",)
print(type(named_tuple))

T = (4,)
print(type(T))

L = [1, 2, 3]
print(tuple(L))

name = "madhu"
print(tuple(name))

nested_tuple = ('red', 'blue', 'green', (12, 3, 14))
print(nested_tuple[3][1])

pack = ('red', 'blue', 'green', 'yellow')
print(pack[0:])
print(pack[-2:])
print(pack[-1])
pack[0] = 'magenta'
print(pack)
colors_tuple = ('red', 'blue', 'green', 'yellow', [0, 30, 20])
colors_tuple[-1][1] = 50
print(colors_tuple)
even_numbers = (1, 2, 3, 35)
print(colors_tuple + even_numbers)
print(even_numbers * 2)
del colors_tuple
print(colors_tuple)
print(type(pack))
print(2 in even_numbers)

numbers = (42, 10, 5, 3, 1, 70)
tmp = list(numbers)
tmp.sort()
print(tmp)

print(tuple(sorted(numbers)))

a, b, c, d = pack
print("d value is {} ".format(d))
a, b = pack
print(a, b)
a, b, c, d, f = pack
print(a, b, c, d, f)

email_address = "msraju2009@gmail.com"
user_name, mail_company = email_address.split('@')
print(user_name)
print(mail_company)

# sets are used to remove duplicate elements in an iterable object

set_object = {3, 2, 1, 5, 6, 1, 2, 7, 9, 2, 3, 2}
print(set_object)

A = [3, 2, 1, 5, 6, 1, 2, 7, 9, 2, 3, 2]
print(set(A))

A = set('madhu')
print(A)

A.add('raju')
print(A)
colors_set = {'red', 'blue', 'green', 'yellow'}
colors_set.update([1, 2, 3])
colors_set.update()
print(colors_set)
colors_set.remove('akdfaksdfnskf')
print(colors_set)
colors_set.discard('akdfaksdfnskf')
print(colors_set)

colors_set.pop()
print(colors_set)
colors_set.clear()
print(colors_set)

A = {'red', 'green', 'blue'}
B = {'orange', 'yellow', 'red'}
print(A | B)
print(A.union(B))

print(A & B)
print(A.intersection(B))

print(A - B)
print(A.difference(B))

print(A ^ B)
print(A.symmetric_difference(B))
