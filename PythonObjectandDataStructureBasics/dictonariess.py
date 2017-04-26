my_dict = {"key1": "values", "key2": "value2"}
print(type(my_dict))
print(my_dict["key1"])

my_dict = {"k1": 123, "k2": 3.4, "k3": "string"}
print(my_dict["k3"])

print(type(my_dict["k1"]))
print(type(my_dict["k2"]))
print(type(my_dict["k3"]))

print(my_dict["k3"][:1])
print(my_dict["k3"][::-1])

print(my_dict["k3"].upper())

print(my_dict["k1"] - 120)

my_dict["k1"] += 120
print(my_dict["k1"])

print(my_dict)

my_dict["k1"] = my_dict["k1"]

d = {}
print(d)
d["animal"] = "dog"
d["answer"] = 42
print(d)

d = {"k1": {"nestkey": {"subnestkey": "value"}}}
print(d)
print(d["k1"])
print(d["k1"]["nestkey"])
print(d["k1"]["nestkey"]["subnestkey"])
print(d["k1"]["nestkey"]["subnestkey"].upper())

d = {}
d['k1'] = 1
d['k2'] = 2
d['k3'] = 3
print(d)

print(d.keys())
print(d.values())
print(d.items())