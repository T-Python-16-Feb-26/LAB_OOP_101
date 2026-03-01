from panda import Panda

panda1=Panda("leo",4,"black",78)
panda2=Panda("kioo",9,"bwhite",98)
panda3=Panda("sho",4,"blue",48)
panda4=Panda("ali",4,"green",79)

print(panda1.name)
print(panda2.name)
print(panda3.name)
print(panda4.name)

for panda in [panda1,panda2,panda3,panda4]:
    print(panda.introduce())
    print(panda.eat_tree())