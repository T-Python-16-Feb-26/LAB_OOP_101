# panda.py

class Panda:
    def __init__(self, name, age, weight, color):
        # 4 Attributes
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color

    # Method 1
    def eat(self):
        print(f"{self.name} is eating bamboo.")

    # Method 2
    def sleep(self):
        print(f"{self.name} is sleeping peacefully.")