d = {"k": 1, "k2": 2}

print({x: x ** 2 for x in range(10)})
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

var = {k: v ** 2 for k, v in zip(['a', 'b', 'c'], range(10))}
print(var)
# {'a': 0, 'b': 1}

for k in d.items():
    print(k)

for k in d.keys():
    print(k)

for k in d.values():
    print(k)

print(d.values())
print(d.keys())
print(d)

