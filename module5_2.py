class House:
    def __init__(self, name, numder_of_floor):
        self.name = name
        self.numder_of_floor = numder_of_floor

    def __len__(self):
        return self.numder_of_floor
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.numder_of_floor}"

h1 = House('ЖК Эльбрус',10)
h2 = House('ЖК Акация', 20)
#__len__
print(len(h1))
print(len(h2))
#__str__
print(h1)
print(h2)
