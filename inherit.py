class rectangle:

   def __init__(self,length,breadth):
      self.length = length
      self.breadth = breadth

   def area(self):
      res = self.length * self.breadth
      print("The area of a rectangle is", res)

length=int(input("Enter the length:"))
breadth=int(input("Enter the breadth:"))

r=rectangle(length,breadth)
r.area()