class Panda:
    def __init__(self,name,age, mood, speed):
     self.name=name
     self.age=age
     self.mood=mood
     self.speed=speed

    def move(self):
        print(f"Panda {self.name} ({self.age} years old) is moving at speed {self.speed}. Mood: {self.mood}")        
    def update_speed(self, new_speed):
        self.speed = new_speed
        print(f"panda {self.name} speed updated to {self.speed}")


