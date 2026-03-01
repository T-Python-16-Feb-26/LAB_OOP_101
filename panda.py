class Panda:
    def __init__(self,name:str,age:int,weight:float,color:str) -> None:
        self.name=name
        self.age=age
        self.weight=weight
        self.color=color

    def introduce(self) -> self:
        return f"Hello ,my name is {self.name}i am a {self.color}, and i am {self.age}year old"
    
    def eat_tree(self)->self:
        return f"{self.name}is eating tree"
    