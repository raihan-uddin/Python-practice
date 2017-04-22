my_list = [1, 2, 3]
print(my_list)
print(type(my_list))

my_list = ['string', 23, 1.2, 'o']
print(my_list)
print(len(my_list))

my_list = ['one', 'two', 'three', 4, 5]
print(my_list[0])

print(type(my_list[0]))
print(type(my_list[3]))

print(my_list[1:])
print(my_list[:3])

my_list = my_list + ['permanet add']
print(my_list)

my_list *= 3
print(my_list)

l = [1, 2, 3]
# add somethin in list
l.append('append me')
print(l)

# remove last index from list
l.pop()
print(l)

x = l.pop(0)
print(x)
print(l)
print(l[1])

# print(l[99])
# IndexError: list index out of range

new_list = ['a','e','x','b','c']
# reversing a list
new_list.reverse()
print(new_list)

#shorting a list
new_list.sort()
print(new_list)

l_1 = [1,2,3]
l_2 = [4,5,6]
l_3 = [7,8,9]
# list in side of another list
matrix = [l_1,l_2,l_3]
print(type(matrix))
print(matrix)

print(matrix[0])
print(matrix[1][1])

fir_col = [row[0] for row in matrix]
print(fir_col)

print([row[2] for row in matrix])