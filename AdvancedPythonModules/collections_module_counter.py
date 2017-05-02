# Counter
from collections import Counter

l = [1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 3, 4, 5, 74, 3, 2, 4, 1, 2, 1, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7]
print(Counter(l))
# Counter({1: 11, 4: 6, 2: 4, 5: 4, 6: 4, 7: 3, 3: 2, 74: 1})



s = 'sdfalks;jdfasdjfosaidjfsakdjfo;iwefnksnflskdjflskdjfsalkd;fjsdkflsajfdsadfsd;fasrfwetwtfsf'
print(Counter(s))
# Counter({'f': 17, 's': 15, 'd': 12, 'a': 8, 'j': 8, 'k': 7, 'l': 5, ';': 4, 'w': 3, 'o': 2, 'i': 2, 'e': 2, 'n': 2, 't': 2, 'r': 1})


s = "How many times does each word show up in this sentence word word show up up"

words = s.split()
print(Counter(words))
# Counter({'word': 3, 'up': 3, 'show': 2, 'How': 1, 'many': 1, 'times': 1, 'does': 1, 'each': 1, 'in': 1, 'this': 1, 'sentence': 1})

c = Counter(words)
print(c.most_common(3))
# [('word', 3), ('up', 3), ('show', 2)]


"""
Common patterns when using the Counter() object
sum(c.values())                         # total of all counts
c.clear()                               # Reset all counts
list(c)                                 # list unique elements
set(c)                                  # convert to a set
dict(c)                                 # convet to a regular dictonary
c.items()                               # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))            # convert from a list of (elem, cnt) pairs
 c.most_common()[:-n-1:-1]              # n least common elements
 c += Counter()                         # remove zero and negative conts
"""
print(sum(c.values()))
# 16
# c.clear()
# print(c)
print(list(c))
# ['How', 'many', 'times', 'does', 'each', 'word', 'show', 'up', 'in', 'this', 'sentence']

print(set(c))
# {'word', 'up', 'this', 'How', 'each', 'does', 'many', 'show', 'times', 'in', 'sentence'}

print(dict(c))
# {'How': 1, 'many': 1, 'times': 1, 'does': 1, 'each': 1, 'word': 3, 'show': 2, 'up': 3, 'in': 1, 'this': 1, 'sentence': 1}

print(c.items())
# dict_items([('How', 1), ('many', 1), ('times', 1), ('does', 1), ('each', 1), ('word', 3), ('show', 2), ('up', 3), ('in', 1), ('this', 1), ('sentence', 1)])
