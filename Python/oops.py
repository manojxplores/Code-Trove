# python is an object oriented programming language
# class is like a object constructor 

class myclass:
    x = 5

p1 = myclass()
print(p1.x)

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("john", 36)
print(p1.name)
print(p1.age)

