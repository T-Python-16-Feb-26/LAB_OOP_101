class Panda:
    def __init__(self, name, age, location, mood="okay"):
        self.name = name
        self.age = age
        self.location = location
        self.mood = mood
    def eat(self):
        print(f"{self.name} is {self.mood} and eating bamboo.")
    def sleep(self):
        print(f"{self.name} is sleeping. and will wake up in a better mood.")
        self.mood = "relaxed"
    def play(self):
        print(f"{self.name} in {self.mood} mood, and is playing and having fun.")
        self.mood = "excited"
    def __str__(self):
        return f"Panda Info:-\n\nName: {self.name}\nAge: {self.age}\nLocation: {self.location}\nMood: {self.mood}\n"