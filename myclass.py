class Panda:
    def __init__(self,name,gender, weight, age, food):
        self.name = name
        self.gender = gender
        self.weight = weight
        self.age = age
        self.food = food
        
    
    def panda_info(self):
        panda_info = f"Panda Information\n-----------\nname: {self.name}\ngender: {self.gender}\nweight: {self.weight}\nage:{self.age}\nfav food: {self.food}"
        return panda_info
    
    def panda_status(self):
        if self.age >= 4:
            #adult
            if self.weight > 125:
                return  "overweight"
            elif self.weight < 85:
                return "underweight"
            else:
                return "Average"
        else:
            return "panda is too young"
    

        