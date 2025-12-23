class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        result = f'{self.name} is talking'
        return result

person1 = Person("Ramya")
print(person1.talk())
