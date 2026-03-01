# create class
class Panda:
    # constructor
    def __init__(self, name: str, age: int, weight: int, diet: str) -> None:
        self.name = name
        self.age = age
        self.weight = weight
        self.diet = diet

    def eat(self):
        if self.age < 0.5:
            return f"{self.name} is under 6 months old and depends on milk"
        else:
            return f"{self.name} is {self.age} years old, older than 6 months, and needs a balanced and sufficient diet"
    
    def sleep(self):
        return f"{self.name} needs to sleep 10 to 14 hours a day"