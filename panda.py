
class Panda:
    def __init__(self ,name:str,age:str,weight:str , height:str):
        self.name = name
        self.age = age 
        self.weight = weight
        self.height = height 

    def name_and_age(self):
        print(f'this panda name :{self.name}age is {self.age}')


    def weight_and_height(self):
        print(f'weight is {self.weight}and height is {self.height}')
    def __str__(self):
        return "yo"
              
              
