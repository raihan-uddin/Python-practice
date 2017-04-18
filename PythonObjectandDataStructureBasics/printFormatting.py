print("this is a string")

s = 'String'
print("place my variable here: %s " % (s))
# place my variable here: String

x = 13.33
print("place my variable here: %s " % x)
# place my variable here: 13.33

# formating float number
f = 13.12345
print("Floating point number : %1.2f" % f)
# Floating point number : 13.12

print("Floating point number : %1.3f" % f)
# Floating point number : 13.123

print("Floating point number : %1.10f" % f)
# Floating point number : 13.1234500000

# White Space before float num
print("Floating point number : %10.2f" % f)
#Floating point number :      13.12

# this %s using str() function
print("convert to string %s" % 123)

# this %r using repr() function
print("convert to string %r" % 123)

print("First: %s, Second: %s, Third %s" %("hi", "two", 3))
# First: hi, Second: two, Third 3

print("First: {x} Second: {x}".format(x = "inserted"))
# First: inserted Second: inserted

print("First: {x} Second: {y} Third: {x}".format(x = "inserted", y = "two!"))
# First: inserted Second: two! Third: inserted

print('Insert another string with curly brackets: {}'.format('The inserted string'))
# Insert another string with curly brackets: The inserted string