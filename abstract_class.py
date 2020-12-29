from abc import ABC, abstractmethod

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod     #indication of abstract method
    def calcArea(self):
        pass

class Square1(GraphicShape):
    def __init__(self,side):
        self.side = side

    def calcArea(self):
        return (self.side * self.side)

class Circle(GraphicShape):
    def __init__(self,radius):
        self.radius = radius

    def calcArea(self):
        return 3.14*(self.radius**2)



class Rectangle(GraphicShape):
    def __init__(self,len,bth):
        self.len = len
        self.bth = bth
    
    def calcArea(self):
        return (self.len * self.bth)
#g= GraphicShape()

c= Circle(10)
print(c.calcArea())
s =Square1(2)
print(s.calcArea)
r = Rectangle(2,4)
print(r.calcArea)