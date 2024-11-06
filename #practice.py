#practice
#The pow function raises a value to that power
x = pow(2,35)
print(x) # Output: 34359738368

#The vars function returns the dictionary attribute of an object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person = Person("Zargathrax", 1500)
print(vars(person))

#The super function is calls methods from parent or sibling classes.
class Animal:
    def  __init__(self,):
        print("Animal's __init__")
    def  speak(self):
        print("ROAR")
class  Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog's __init__")
    def speak(self):
        super().speak()
        print("Woof")
Dog_instance = Dog()
Dog_instance.speak()


