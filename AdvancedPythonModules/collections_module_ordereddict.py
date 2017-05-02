from collections import OrderedDict

d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

print(d)

# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


for k, v in d.items():
    print(k, v)
# a 1
# b 2
# c 3
# d 4
# e 5

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

for k, v in d.items():
    print(k, v)



d1 = OrderedDict({
    "a":1,
    "b":2
})

d2 = OrderedDict({
    "b":2,
    "a":1
})

print(d1 == d2)
