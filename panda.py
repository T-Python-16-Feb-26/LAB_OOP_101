class Panda:
    def __init__(self, name, type, sex, age):
        self.name = name
        self.type = type
        self.sex = sex
        self.age = age
    
    def eat(self):
        return f"{self.name} is eating bamboo."
    def sleep(self):
        return f"{self.name} is sleeping."