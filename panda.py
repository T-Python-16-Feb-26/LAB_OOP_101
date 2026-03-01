#oop 101

class Panda:
    def __init__(self, name, age, weight, color):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color

    #Methods
    def eat(self):
        print(f"{self.name} is eating bamboo")

    def sleep(self):
        print(f"{self.name} is sleeping")