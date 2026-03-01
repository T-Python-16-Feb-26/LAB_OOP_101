from panda import Panda

panda1 = Panda("Ling", "Giant Panda", "male", 5)
panda2 = Panda("Mei", "Red Panda", "female", 3)
panda3 = Panda("Bao", "Giant Panda", "male", 2)
panda4 = Panda("Xiao", "Red Panda", "female", 4)

pandas = [panda1, panda2, panda3, panda4]

for panda in pandas:
    print(f" Name: {panda.name}, Type: {panda.type}, Sex: {panda.sex}, Age: {panda.age}")
    print(panda.eat())
    print(panda.sleep())
    print("-" * 30)

