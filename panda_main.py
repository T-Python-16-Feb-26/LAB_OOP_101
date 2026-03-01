from panda_class import panda

def main():
    panda1 = panda("Pnut", 5, "Snax", "12AM")
    panda2 = panda("Snax", 5, "Pnut", "1AM")
    panda3 = panda("Pan", 3, "none", "5AM")
    panda4 = panda("Da", 4, "none", "1AM-9AM")


    print(panda1.name)
    panda1.panda_info()
    panda1.has_mate()

    print(panda2.name)
    panda2.panda_info()
    panda2.has_mate()

    print(panda3.name)
    panda3.panda_info()
    panda3.has_mate()

    print(panda4.name)
    panda4.panda_info()
    panda4.has_mate()
    
main()