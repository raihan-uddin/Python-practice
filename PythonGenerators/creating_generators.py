# Generator function for the cube of numbers (power fo 3)
def gencube(n):
    # out = []
    for num in range(n):
        yield num ** 3
        # out.append(num ** 3)
        # return out


for x in gencube(10):
    print(x)


def genfibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        t = a
        a = b
        b += t


for num in genfibon(10):
    print(num)


def fibon(n):
    a = 1
    b = 1

    output = []
    for i in range(n):
        output.append(a)
        a, b = b, a + b
    return output


fibon(20)


def simple_gen():
    for x in range(3):
        yield x


g = simple_gen()
print(next(g))
print(next(g))
print(next(g))

s = 'hello'
for let in s:
    print(let)

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
