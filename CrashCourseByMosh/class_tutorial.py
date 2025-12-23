#class is the blue print/template of an obj
# objects are the instances of the blue print.
#A class has variable, method, constructor etc.
#A class can be used once it is instantiated , which is called object

# class Point:
#     def draw(self):
#         print("draw method called")
#
# point1 = Point()
# point1.draw()
#
# point2= Point()
# point2.a=10
# point2.b=20
# print(point2.a,point2.b)

# point3 = Point()
# print(point3.a) #this will show AttributeError , each obj should have its own attribute.

#we can use the constructor ===> constructor is a function that  gets called during object creation.

class Demo:
    def __init__(self, x, y): #we added two param after the self
        self.x = x  # self refer to the current obj ,the obj of x is pointing to the parameter x
        self.y = y

    def print(self):
        print(self.x, self.y)

demo = Demo(10,20)
demo.print()

