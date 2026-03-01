from classes import Panda

panda1= Panda("Bao Bao","China",2,False)
panda2= Panda("Ling Ling","Japan",10,True)
panda3= Panda("Le Le","France",17,False)
panda4= Panda("Jia Jia","Australia",22,True)

print(panda1.name)
print(panda1.hungry())
print(panda1.sleep())

print(panda2.hungry())
print(panda2.sleep())

print(panda3.hungry())
print(panda3.sleep())

print(panda4.hungry())
print(panda4.sleep())