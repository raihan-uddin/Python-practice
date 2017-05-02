l = [1, 2, 3]

print(l.count(10))
print(l.count(1))

l.append(4)
print(l)

x = [1, 2, 3]
x.append([4, 5])
print(x)

x = [1, 2, 3]
x.extend([4, 5])
print(x)

print(l)

print(l.index(2))
# error
# print(l.index(10))

l.insert(2, "inserted")
print(l)

ele = l.pop()
print(l)

l.pop(0)
print(l)

l.remove('inserted')
print(l)

l = [1, 2, 3, 4, 3]
l.remove(3)
print(l)

l.reverse()
print(l)

l.sort()
print(l)
