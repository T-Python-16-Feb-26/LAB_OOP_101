class Panda:
    # Constructor
    def __init__(self, name, age, color, weight):
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight

    # Method 1
    def eat(self):
        print(f"{self.name} is eating bamboo 🌿")

    # Method 2
    def sleep(self):
        print(f"{self.name} is sleeping 😴")