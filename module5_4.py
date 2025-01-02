class House:
    houses_history = []

    def __new__(cls, name, numder_of_floor):
        cls.houses_history.append(name)
        return super().__new__(cls)

    def __init__(self, name, numder_of_floor):
        self.name = name
        self.numder_of_floor = numder_of_floor

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.numder_of_floor}"

    def __eq__(self, other):
            return self.numder_of_floor == other

    def __lt__(self, other):
        if self.numder_of_floor < other:
            return True
        else:
            return False


    def __le__(self, other):
        if self.numder_of_floor <= other:
            return True
        else:
            return False


    def __gt__(self, other):
        if self.numder_of_floor > other:
            return True
        else:
            return False


    def __ge__(self, other):
        if self.numder_of_floor >= other:
            return True
        else:
            return False


    def __ne__(self, other):
        if self.numder_of_floor != other:
            return True
        else:
            return False


    def __add__(self, value):
        if isinstance(value, int):
          self.numder_of_floor = self.numder_of_floor + value
          return self
        else:
            return False


    def __radd__(self, value):
        self.numder_of_floor = self.numder_of_floor + value
        return self

    def __iadd__(self, value):
        self.numder_of_floor = self.numder_of_floor + value
        return self

h1 = House('ЖК Эльбрус', 10)

print(House.houses_history)

h2 = House('ЖК Акация', 20)

print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)

print(House.houses_history)



# Удаление объектов

del h2

del h3



print(House.houses_history)



