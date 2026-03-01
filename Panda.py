class Panda:
    def __init__ (self,type:str,color:str,age:str,count:float,location:str,endangered:bool):
        self.type=type
        self.color=color
        self.age=age
        self.count=count
        self.location=location
        self.endangered=endangered

    def extinction_status(self):
        if self.endangered== True:
            return f"This panda {self.type} : endangered"
        else:
            return f"This panda {self.type} : not endangered"
    

    def display_info(self):
        info=f"The animal is the PANDA, of the type {self.type}, and it has a {self.color} color. Its lifespan is {self.age}, and there are {self.count} in {self.location}. In terms of the threat of extinction, it is {self.endangered}"
        return info