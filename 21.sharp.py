from abc import ABC

class sharpe(ABC):
    def area(self):
        return 0
    
class Square(sharpe):
    def __init__(self):
        self.length=length
            
    def area(self):
        return self.length+self.length
    
square = Square(4)
square_area=square.area()
print(square_area)
    