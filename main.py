from panda import panda

if __name__ == "__main__":
    panda1 = panda("Panda1", 5, "Male", 100.0)
    panda2 = panda("Panda2", 3, "Female", 80.0)
    panda3 = panda("Panda3", 7, "Male", 120.0)
    panda4 = panda("Panda4", 2, "Female", 60.0)
    
    print(panda1.name)
    print(panda2.age)
    
    panda.eatFood(panda1, "bamboo")
    panda.sleep(panda1,  12)