class box():
    def __init__(self,length,breadth,height):
        self.length=length
        self.breadth=breadth
        self.height=height
    def area(self):
        return self.length*self.breadth*self.height
    def peri(self):
        return self.length*self.height
l=int(input("length: "))
b=int(input("breadth: "))
h=int(input("height: "))
a=box(l,b,h)
print("Area of the box: ",a.area())
print("Perimeter of the box: ",a.peri())
print()
