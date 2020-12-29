class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"

class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"
    
class C(B,A):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name)

c= C()
c.showprops()
print(C.__mro__) # Method Resolution Order
                # is the order in which Python 
                # looks for a method in a hierarchy of classes