
class Panda: 
    def __init__(self, name: str, gender: str, age: int, health: str):
        self.name = name
        self.gender = gender
        self.age = age
        self.health = health
        
    def status(self):
        
        return f"Panda: {self.name}, Gender: {self.gender}, Age: {self.age}, Health: {self.health}" 

    def sleep(self):
        return f"{self.name} is now taking a nap in the bamboo forest!"
