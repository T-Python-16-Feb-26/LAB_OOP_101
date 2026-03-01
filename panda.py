class panda:
    def __init__(self, name:str, age:int, gender:str, weight:float):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
    
    def eatFood(self, food):
        print(f"{self.name} is eating {food}.")
        self.weight += 1
        print(f"{self.name}'s weight has increased! it is now: {self.weight}")
        
    def sleep(self, sleepTime:int):
        print(f"{self.name} is now sleeping for {sleepTime} hours")
    
