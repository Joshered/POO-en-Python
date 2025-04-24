from abc import ABC

class Sharpe(ABC):
    def area(self):
        return 0
    
class Square(Sharpe):
    def __init__(self,length):
        self.length=length
            
    def area(self):
        return self.length*self.length
    
class Triangle(Sharpe):
    def __init__(self,base,hauteur):
        self.base=base
        self.hauteur=hauteur
            
    def area(self):
        return (self.base*self.hauteur)/2
    
square = Square(4)
square_area=square.area()
print(square_area)

triangle=Triangle(5,7)
print(triangle.area())
    