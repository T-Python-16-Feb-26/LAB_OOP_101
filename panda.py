class Panda:
    def __init__(self, name, age, weight, color):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color

    def eat(self):
        print(self.name, "is eating bamboo")

    def sleep(self):
        print(self.name, "is sleeping")

    def description(self):
        print("Your panda's information: ")
        info = f"panda's name is : {self.name}, age is : {self.age}, weight is : {self.weight}, color: {self.color}" 
        print(info)