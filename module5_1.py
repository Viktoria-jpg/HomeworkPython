class House:
    def __init__(self, name, numder_of_floor):
        self.name = name
        self.numder_of_floor = numder_of_floor
    def go_to(self, new_floor):
        if new_floor > self.numder_of_floor or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(new_floor):
                print(i+1)

h1 = House('ЖК Горский',10)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
