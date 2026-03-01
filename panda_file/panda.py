class Panda:
    def __init__(self , name:str,age:int,weight:float,food:str):

        self.name=name
        self.age=age
        self.weight=weight
        self.food=food
        
    def eat(self):
        print(f"the {self.name} is eating {self.food}")

    def sleep(self):
        
        print(f"The {self.name} will sleep at night")