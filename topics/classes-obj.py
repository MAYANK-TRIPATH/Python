# Pyhton is object oriented lang.
# Mostly Things in python are in objects. withs its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# class MyClass:   # this is class
#     x =10       # with property x


# p1 = MyClass()       # object named p1
# print(p1.x)      


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

p1 = Person("Mayank", 20)

print(p1.name)
print(p1.age)