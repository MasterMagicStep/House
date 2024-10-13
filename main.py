class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors #floors было

    def Gt (self , new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for f in range(1, new_floor+1): #New было
                print(f)
        else:
                print("Нет такого этажа") #Floor is not defined было


h1 = House('Doctrine', 10)
h2 = House('Laclord', 11)
h1.Gt(5)
h2.Gt(12)
