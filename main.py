from panda import Panda

panda1 = Panda("Po", 5, 100, "Black & White")
panda2 = Panda("Luna", 3, 110, "Black & White")
panda3 = Panda("Lili", 7, 120, "White")
panda4 = Panda("Snow", 4, 90, "White")


print(panda1.name)
print(panda2.name)
print(panda3.name)
print(panda4.name)


panda1.eat()
panda2.sleep()
panda3.description()