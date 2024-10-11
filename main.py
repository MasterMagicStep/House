class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def Gt (self , New):
        if 0 < New <= self.floors:
            for f in range(1, New+1):
                print(f)
        else:
                print("Floor is not defined")


h1 = House('Doctrine', 10)
h2 = House('Laclord', 11)
h1.Gt(5)
h2.Gt(12)
