try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print("An error occured!")



x = 5
y = 0
try:
    z = x /y
    print(z)
except ZeroDivisionError:
    print("Can't devide by zero")
finally:
    print("All done")

def ask():
    while True:
        try:
            val = int(input("Input an integer: "))
        except:
            print("An error occured! Please try again")
        else:
            break
    print("Thank you, you number sqared is: ", val ** 2)

ask()
