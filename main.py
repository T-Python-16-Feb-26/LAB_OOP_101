# main.py

from panda import Panda

# Create 4 Panda objects
panda1 = Panda("Teddy", 5, 100, "Black & White")
panda2 = Panda("Bear", 3, 80, "Black & White")
panda3 = Panda("Snowy", 4, 90, "Black & White")
panda4 = Panda("Fluffy", 2, 70, "Black & White")

# Print 1 attribute value (name)
print(panda1.name)
print(panda2.name)
print(panda3.name)
print(panda4.name)

print("\n Panda Activities \n")

# Call the 2 methods on each instance
panda1.eat()
panda1.sleep()

panda2.eat()
panda2.sleep()

panda3.eat()
panda3.sleep()

panda4.eat()
panda4.sleep()
