class Rectangle :
    def __init__(self,long,wid) :
        self.length = long
        self.width = wid
    def RectangleArea(self):
        return((self.length)*(self.width))
rectangle1 = Rectangle(4,8)
print(rectangle1.RectangleArea())