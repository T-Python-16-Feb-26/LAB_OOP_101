
class panda:

    def __init__(self, name:str, age:int, mate:str, feed_time:str):

        self.name = name
        self.age = age
        self.mate = mate
        self.feed_time = feed_time


    def panda_info(self):
        print("name: ", self.name)
        print("age: ", self.age)
        print("mate: ", self.mate)
        print("feed time: ", self.feed_time)

    def has_mate(self):
        if self.mate == "none":
            print(f"{self.name} has no mate")
        else:
            print(f"{self.mate} is the mate of {self.name}")
        

