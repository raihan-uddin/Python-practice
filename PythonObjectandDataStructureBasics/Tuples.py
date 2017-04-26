t = (1, 2, 3)
print(t)
print(type(t))
print(len(t))

t = ('one', 2, 5.5)
print(t)
print(t[0])

# grav the last one
print(t[-1])

# get the index
print(t.index('one'))
print(t.index(5.5))

t = (1, 1, 1, 2, 3, 4)
# count the items on tuples
print(t.count(1))

# Tuples are immutuble
#list
l = [1,2,3]
#tuple
t = (1, 2, 3)

l[0] = 's'
print(l)

# 'tuple' object does not support item assignment
# t[0] = 's'


