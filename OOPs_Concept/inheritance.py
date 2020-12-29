class Publication:
    def __init__(self,title,price):
        self.title = title
        self.price = price

class Periodical(Publication):
    def __init__(self,title,price,publisher,period):
        super().__init__(title,price)
        self.publisher=publisher
        self.period=period

class Book(Publication):
    def __init__(self,title,author,pages,price):
        super().__init__(title,price) #inherting these attributes
        self.author=author
        self.pages=pages


class Magazine(Periodical):
    def __init__(self,title,publisher,price,period):
        super().__init__(title,price,publisher,period)

class Newspaper(Periodical):
    def __init__(self,title,publisher,price,period):
        super().__init__(title,price,publisher,period)


b1 = Book("Brave" , "Adarsh" , 311,29.0)
n1 = Newspaper("NYT", "NYT Company" , 6.0 , "Daily")
m1 = Magazine("Scince" , "Nature" , 5.99 , "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price,m1.price,n1.price)