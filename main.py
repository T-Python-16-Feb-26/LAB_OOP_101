from panda import Panda

p1 = Panda("Bamboo", 3, "black-white", "bamboo")
p2 = Panda("Luna", 5, "black-white", "apple")
p3 = Panda("Momo", 2, "brown", "carrot")
p4 = Panda("Kiki", 4, "black-white", "sweet potato")

pandas = [p1, p2, p3, p4]

for panda in pandas:
    print(panda.name)   
    panda.eat()         
    panda.sleep()       
    print("-----")