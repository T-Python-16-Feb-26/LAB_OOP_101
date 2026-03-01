from panda import Panda

panda1 = Panda("Po", 5, 100, "black & white")
panda2 = Panda("Ling", 3, 80, "black & white")
panda3 = Panda("Ming", 7, 120, "black & white")
panda4 = Panda("Bao", 2, 70, "black & white")

pandas = [panda1, panda2, panda3, panda4]

for panda in pandas:
    print(f"Panda Name: {panda.name}")
    panda.eat()
    panda.sleep()
    print("-" * 30)