import string


def vol(red):
    return (4.0 / 3) * (3.14) * (red ** 3)


print(vol(5))


def ran_check(num, low, high):
    # check if num is between low and high (including low and high)
    if num in range(low, high):
        print("%s is in the range" % str(num))
    else:
        print("the number is outsed the range.")


ran_check(10, 5, 20)


def ran_bool(num, low, high):
    return num in range(low, high)


print(ran_bool(3, 1, 10))

lmd = lambda num, low, high: num in range(low, high)
print(lmd(20, 10, 60))


def up_low(s):
    d = {"upper": 0, "lower": 0}
    for c in s:
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case String : ", d["upper"])
    print("No. of Lower case String : ", d["lower"])


s = 'Hello Mr. Raihan Uddin, How are you this fine Friday'
up_low(s)


def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x


print(unique_list([1, 1, 1, 2, 2, 3, 4, 5, 6, 9, 8, 7, 1, 5, 2, 3, 1, 4, 5]))


def multiply(numbers):
    total = numbers[0]
    for x in numbers:
        total *= x
    return total


print(multiply([1, 2, 3, 4]))


def palindrome(s):
    return s == s[::-1]


print(palindrome('haelleah'))


def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())


print(ispangram("The quick brown fox jumps over the lazy dog"))
