from panda import Panda



panda1 = Panda("Po", 5, 100, "meat")
panda2 = Panda("Ling", 3, 80, "fish")
panda3 = Panda("Ming", 7, 120, "banana")
panda4 = Panda("Hua", 4, 90, "snake")


# put them in a list
pandas = [panda1, panda2, panda3, panda4]





for panda in pandas:
   
    panda.eat()
    panda.sleep()
    print()