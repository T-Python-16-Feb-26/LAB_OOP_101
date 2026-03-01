from Panda import Panda

panda1=Panda("Mammal","black and white",20,1864,"China", True)
panda2=Panda("Mammal", "black and brown",25,1200,"Sichuan Province", False)
panda3 = Panda("Giant Panda","black and white",20,1864,"China",False)
panda4 = Panda("Qinling Panda","brown and white",25,300,"Qinling Mountains",True)

print(panda1.display_info())
print()
print(panda2.display_info())
print()
print(panda3.display_info())
print()
print(panda4.display_info())

print()
print(panda1.extinction_status())
print(panda2.extinction_status())
print(panda3.extinction_status())
print(panda4.extinction_status())
print()
print(panda1.count)
print(panda2.color)
print(panda3.age)
print(panda4.count)


