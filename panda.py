class Panda:
    def __init__(self, name: str, age: int, color: str, weight: float) -> None:
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight

    def information(self):
        information = f"The animal {self.name}, they are {self.age} years old, their color is {self.color}, its weight is {self.weight}"
        return information

    def sleep(self):
        sleep_message = f"{self.name} is sleeping"
        return sleep_message