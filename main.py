from Panda import Panda

panda1 = Panda("Rex", 5, "Happy", 12)    
panda2 = Panda("Rocky", 12, "Energetic", 25) 
panda3 = Panda("Luna", 2, "Sleepy", 5)     
panda4 = Panda("Zack", 20, "Calm", 10)

print(panda1.mood)


panda1.move()
panda1.update_speed(15)

panda2.move()
panda2.update_speed(45)

panda3.move()
panda3.update_speed(0)

panda4.move()
panda4.update_speed(25)


