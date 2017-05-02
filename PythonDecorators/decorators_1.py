"""def func():
    return 1


print(func())"""

s = 'This is a globl variable'


def func():
    print(locals())


func()


print(globals().keys())
# dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 's', 'func'])
# print(globals()['s'])

def hello(name='Raihan'):
    return 'Hello ' + name


print(hello())

greet = hello
print(greet)
print(greet())
del hello
# print(hello())
print(greet())