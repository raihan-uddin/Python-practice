print(bin(1024))
print(hex(1024))

print(round(5.23222, 2))

s = "hello how are you Raihan, are you felling okay?"
print(s.islower())

s = 'twywywtwywbwhsjhwuwshshwuwwwjdsjdisds'
print(s.count('w'))

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
print(set1.difference(set2))

print(set1.union(set2))


print({x:x ** 3 for x in range(5)})
l = [1,2,3,4]
l.reverse()
print(l)

l = [3,4,2,5,1]
l.sort()
print(l)
