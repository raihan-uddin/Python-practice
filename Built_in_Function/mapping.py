def fahrenheit(T):
    return (float(9.0) / 5) * T + 32


print(fahrenheit(0))

temp = [0, 22.5, 40, 100]

print(map(fahrenheit, temp))  # ?????????????? <map object at 0x00000214D009E080>

c = map(lambda T: (9.0 / 5) * T + 32, temp)
print(c)  # <map object at 0x00000214D009E080>

print(lambda x, y: x + y)
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
print(map(lambda x, y: x + y, a, b))

print(map(lambda  num: num *- 1,a))
