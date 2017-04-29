# l = [1, 2, 3]
# print(l)
# print(len(l))

class Book(object):
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title:%s, author:%s , pages:%s " %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    # def __del__(self):
    #     print("A book is destroyed")


b = Book('Python', 'Raihan', 100)
print(len(b))
print(b)

# del b
print(b.title)
