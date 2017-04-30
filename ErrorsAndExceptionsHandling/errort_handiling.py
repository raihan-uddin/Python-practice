try:
    2 + 's'
except TypeError:
    print("There was a type error")
finally:
    print("Final this was printed!")

try:
    f = open('tesfile.txt', 'w')
    f.write("Test Write this")
except:
    print("Error in writing to the file!")
else:
    print("File write was a success")

try:
    f = open('tesfile.txt', 'r')
    f.write("Test Write this")
except IOError:
    print("Error in writing to the file!")
else:
    print("File write was a success")

try:
    f = open('tesfile.txt', 'r')
    f.write("Test File Write this")
except:
    print("There was an error!")
finally:
    print("Always Execute finally code block")

"""
def askint():
    try:
        val = int(input("Please enter an integer : "))
    except:
        print("Looks like you did not enter an integer!")
        val = int(input("Try Again- Please enter an integer: "))
    finally:
        print("finally block executed!")

    print(val)
"""


def askint():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you didn't enter an integer!")
            continue
        else:
            print("Correct, That is an integer!")
            break
        finally:
            print("FInally Block Executed!")
    print(val)


askint()
