
class Panda:
    def __init__(self, name:str, age:int, weight:float, color:str):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
    
    def info(self):
        introduction = f"Name is {self.name}, age is {self.age}-year-old , panda weighing is {self.weight} kg and color is {self.color}."
        return introduction
    def eat(self, food:str):
        eat = f"{self.name} is eating {food}."
        return eat
    
    def sleep(self, hours:int):
        sleep = f"{self.name} is sleeping for {hours} hours."
        return sleep
    