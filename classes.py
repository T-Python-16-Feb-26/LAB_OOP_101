class Panda:

    def __init__(self, name:str,country:str, age:int, is_hungry:bool):
        self.name=name
        self.country=country
        self.age=age
        self.is_hungry=is_hungry

    def sleep (self):
        message= f"The {self.name} is sleeping now"
        return message
    
    def hungry(self):
        if self.is_hungry:
            message_hungry=f"{self.name} is hungry !!"
        else:
            message_hungry=f"{self.name} is not hungry :)"
        return message_hungry

    
    
