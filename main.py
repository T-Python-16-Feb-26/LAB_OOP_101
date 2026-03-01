from panda import Panda
def main():
    pandas = []
    p1 = Panda("P1", 5, "Forest")
    p2 = Panda("P2", 3, "Zoo", "sad")
    p3 = Panda("P3", 7, "Nature", "happy")
    p4 = Panda("P3", 2, "Wild", "playful")
    pandas.append(p1)
    pandas.append(p2)
    pandas.append(p3)
    pandas.append(p4)
    for panda in pandas:
        print(f"++++++++ Meet {panda.name} ++++++++")
        panda.eat()
        panda.play()
        panda.sleep()
        print(panda)
    
if __name__ == "__main__":
    main()