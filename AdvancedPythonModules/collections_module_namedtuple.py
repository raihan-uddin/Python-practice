from collections import  namedtuple

t = (1,2,3)
print(type(t))

print(t[1])


Dog = namedtuple('Dog', 'age breed name')
sam = Dog(age=2, breed='lab', name='sammy')
print(sam.age)
print(sam.breed)
print(sam.name)

print(sam[0])
print(sam[1])


Cat = namedtuple('Cat', 'fur claws name')
c = Cat(fur= 'Fuzzy', claws=False, name='kitty')
print(c)
print(type(c))