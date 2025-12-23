#inheritance is the mechanism for reusing code.
#
# class Dog:
#     def walk(self):
#         print("walk")
#
#
# class Cat:
#     def walk(self):
#         print("walk")


#we have walk() method used by both cat and Dog. In codine , we have to follow DRY(Dont Repeat Yourself). To avoid repeating code , we can use inheritance.

class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal): #this will inherit the methods from dog
    pass # we can write pass if we dont have anything to write inside the method. it will pass the method block

class Cat(Mammal):
    def sleeping(self):
        print("sleeping")

dog = Dog()
dog.walk()

cat = Cat()
cat.walk()
cat.sleeping()