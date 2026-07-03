class Book:
    def __init__(self, title,author):
        self.title = title
        self.author = author
    def __repr__(self):
        return repr((self.title,self.author))


book = Book('SQLtoPython','Ayushman Singh')
print(book)