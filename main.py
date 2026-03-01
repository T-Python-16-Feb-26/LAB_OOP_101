from panda import Panda

panda1 = Panda("Oreo", 15,"black and white", 98.0)
panda2 = Panda("Mochi", 10,"Brown and White", 80.0)
panda3 = Panda("Bao Bao", 6, "Black and White", 92.5)
panda4 = Panda("Lulu", 12, "Brown and White", 95.0)

print(panda1.information())
print(panda1.sleep())

print(panda2.information())
print(panda2.sleep())

print(panda3.information())
print(panda3.sleep())

print(panda4.information())
print(panda4.sleep())

print(panda1.name)
print(panda3.color)
print(panda2.name)
print(panda4.age)