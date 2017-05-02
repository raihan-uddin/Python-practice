from collections import defaultdict

d = {"k1": 1}
print(d["k1"])

# d['k2']
# KeyError: 'one'

d = defaultdict(object)
print(d['one'])
# <object object at 0x00000174A073A0A0>

for item in d:
    print(item)
# one



d = defaultdict(lambda : 0)
print(d['one'])
print(d['two'])
print(d)
# defaultdict(<function <lambda> at 0x00000217022C3E18>, {'one': 0, 'two': 0})