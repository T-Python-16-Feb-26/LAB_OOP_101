
from panda import Panda


panda1 = Panda("Rimi", "Female", 7, "Sick")
panda2 = Panda("Samuil", "Male", 4, "Healthy")
panda3 = Panda("Mimi", "Female", 1, "Healthy")
panda4 = Panda("Bao", "Male", 10, "Excellent")


pandas_list = [panda1, panda2, panda3, panda4]

for p in pandas_list:
    print("-" * 20)
    
    print(f"Checking on: {p.name}")

    print(p.status())
    print(p.sleep())