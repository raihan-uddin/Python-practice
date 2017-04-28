import math, sys


# def square(num):
#     result = num ** 2
#     return result
#
#
# print(square(2))
#
#
# def square(num):
#     return num ** 2
#
#
# print(square(5))
#
#
# # lambda expression
# def square(num): return num ** 2
#
#
# print(square(6))
#
# print(lambda num: num ** 2)
#
# square = lambda num: num ** 2
#
# print(square(10))
#
# # chek if a number is even
# even = lambda num: num % 2 == 0
# print(even(10))
#
#
# # Regular code
# # def even(num):
# #     return num % 2 == 0
# #
# # print(even(12))
#
# # Grab the first character of a string
# first = lambda s: s[0]
# print(first("hello"))
#
# reverse = lambda  s:s[::-1]
# print(reverse("raihan"))
#
# # Regular code
# # def adder(x,y):
# #     return x + y;
# #
# # print(adder(10,22))
#
# # lambda code
# adder = lambda x,y: x + y
# print(adder(10,12))

def square_root(x): return math.sqrt(x)


print(square_root(5))

square_root = lambda x: math.sqrt(x)
print(square_root(2))

sum = lambda x, y: x + y
print(sum(5, 6))

out = lambda *x: sys.stdout.write(" ".join(map(str, x)))
print(out(2))


