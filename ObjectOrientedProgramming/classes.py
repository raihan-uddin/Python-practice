class Sample(object):
    pass


x = Sample()
print(type(x))


class Dog(object):
    # Class object Attribute
    species = 'mamal'

    def __init__(self, breed, name, fur = True):
        self.breed = breed
        self.name = name
        self.fur = fur


sam = Dog(breed="lab", name='sas')
print(sam)

print(sam.breed)
print(sam.name)
print(sam.species)
print(sam.fur)


dmm = Dog(breed="lab", name='sas', fur=False)
print(dmm.fur)
