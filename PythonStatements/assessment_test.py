st = 'print only the word that start with s in this sentence'
# for word in st.split():
#     # print(word)
#     if word[0] == 's':
#         print(word)

# for x in range(0, 10, 2):
#     print(x)
#
# # list comprehansion
# lst = [x for x in range(50) if x % 3 == 0]
# print(lst)
#
# st = 'Print every word in this sentence that has an even numbers of letters'
# for word in st.split():
#     if len(word) % 2 == 0:
#         print(word + "<-- has an even lenth")
#
# for num in range(1,101):
#     if num %5 == 0 and num % 3 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

st = 'Create a list of the first letters of every word in this string'
lst = [word[0] for word in st.split()]
print(lst)
