a = (20000 - (10 ** 2) / 12 * 34) - 19627.75
print(a)
# True division
print(2 // 3)

print(4 * (6 + 5))
print(4 * 6 + 5)
print(4 + 6 * 5)

a = 3 + 1.5 + 4
print(type(a))

print(100 ** 0.5)
print(10 ** 2)

s = "hello"
print(s[1])
print(s[::-1])
print(s[-1])
print(s[4])

# list
l = [0] * 3
print(l)

l = [0, 0, 0]
print(l)

l = [1, 2, [3, 4, 'hello']]
print(l)
l[2][2] = "goodbye"
print(l)

l = [3, 2, 4, 5, 5, 6]

print(sorted(l))

ll = [1, 2, 3, 2, 5, 6, 7, 2, 9]
ll.sort()
print(ll)

# Dictonaries

d = {"simple_key": "hello"}
print(d)
# print(d["simple_key"])

d = {"k1": {"k2": "hello"}}
# print(d["k1"]["k2"])

e = {"k1": [{"nest_key": ["this is deep", ["hello"]]}]}
# print(e)
print(e["k1"])

print(e["k1"][0]["nest_key"][1][0])

d = {'k1': [1, 2, {'k2': ['this is tricky', {'toughie': [1, 2, ['hello']]}]}]}
print(d)

print(d['k1'][2]['k2'][1]['toughie'][2][0])

# Tuples
t = (1, 2, 3)

# sets
l = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2, 1, 3]
print(set(l))

# Booleans
print(2 > 3)

print(3 <= -2)

print(3.00 == 3)

print(3 == 2.0)

print(4 ** 0.5 != 2)

l_one = [1,2,[3,4]]
l_two =[1,2,{'k1':4}]
print(l_one[2][0] >= l_two[2]['k1'])
