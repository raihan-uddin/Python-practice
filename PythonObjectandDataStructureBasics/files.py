import os

#  print current directory
print(os.getcwd())

# changing the directory
# os.chdir(os.path.dirname(__file__))
# print(os.getcwd())


# f = open('test.txt')
# print(f.read())

# if i print it again it will print nothing. because the cursor is end of the file
# print(f.read())

# to set the cursor begening of the file use seek()
# f.seek(0)
# print(f.read())
#
# f.seek(0)
# print(f.readline())

# Open a file
fo = open("test.txt", "w")
print("name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("opening mode :", fo.mode)

#write on a existing file
fo.write("python is a great language. \nYeah!! \n its great")

#  Read from a file
fo = open("test.txt", "r+")
str = fo.read(10)
# fullString = fo.readline()
print("Read String is: ", str)
# print(fullString)
# File

# Read full text from file
fo.seek(0)
for line in open('test.txt'):
    print(line)

# check current position
position = fo.tell()
print("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0)
str = fo.read(10)
print("Again read String is : ", str)

# Rename  a file from test-2.txt to test3.txt
# os.renames("test-2.txt", "test-3.txt")

# Delete file test-3.txt
# os.remove("test-3.txt")
# Close opened file
fo.close()
print("Closed or not : ", fo.closed)

# Create a new directory
# os.mkdir("test")

# changing a directory to test
# os.chdir("test/")

# This would give location of the current directory
print(os.getcwd())

# This would  test directory.
# os.rmdir("test")

# ?????
# magic command %%writefile test.py

