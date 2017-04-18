# To use print function from Python 3 in Python2
#from  __future__ import print_function

# String word
print("hello world")
print('this is a string')

# this code will get error
# print('I'm a string')

print("i'm a string")
print('"this is a quote"')

print('Here is a new line \n and here is the second line')
print('Here is a new tab \t and here is the second line')

print(len("Hello World"))

s = "Hello World"
print(s)

#indexing
#in python index starting on 0
print(s[0])
print(s[1])

#Slicing a string
print(s[1:])
#ello World
print(s[:5])
#Hello
print(s[1:4])
#ell
print(s[-1])
#d
print(s[:-1])
#Hello Worl

#Grab Everything Step size 1
print(s[::1])
#Hello World

#Grab Everything Step size 2
print(s[::2])
#HloWrd

#Grab Everything reverse Step size 1
print(s[::-1])
#dlroW olleH

print(s)
#String Properties
#String Properties Knows as "immutabillity"
#Once a string is created the elements within it can't change or replace
#s[0]  = 'x'
#TypeError:'str' object does not support item assignment

#but you can concatenate / adding new string together
s = s + " concatenate me!"
print(s)

letter = 'za'
print(letter * 10)
#zazazazazazazazazaza

s = "Hello python"
print(s.upper())
#HELLO PYTHON

print(s.capitalize())
#Hello python

print(s.lower())
#hello python

print(s.split())
#['Hello', 'python']

print(s.split('o'))
#['Hell', ' pyth', 'n']