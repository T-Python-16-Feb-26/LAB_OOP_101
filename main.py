from Lab import Panda
panda1 = Panda("Po", 5, 100.5, "black and white")
panda2 = Panda("Do", 9, 80.0, "brown")
panda3 = Panda("Bo", 3, 60.0, "white")
panda4 = Panda("Mo", 7, 90.0, "black")

print(panda1.info())
print(panda2.info())
print(panda3.info())
print(panda4.info())

print(panda1.eat("Berries"))
print(panda2.eat("Bamboo"))
print(panda3.eat("Nuts"))
print(panda4.eat("Fish"))

print(panda1.sleep(8))
print(panda2.sleep(10))
print(panda3.sleep(6))
print(panda4.sleep(7))