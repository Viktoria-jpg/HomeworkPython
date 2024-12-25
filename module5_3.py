class House:
    def __init__(self, name, numder_of_floor):
        self.name = name
        self.numder_of_floor = numder_of_floor

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

h1 = House('ЖК Эльбрус',10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2) # eq
h1 = h1 + 10 # add

print(h1)
print(h1 == h2)
h1 += 10 # iadd
print(h1)
h2 = 10 + h2 # radd
print(h2)
print(h1 > h2) # gt
print(h1 >= h2) # ge
print(h1 < h2) # lt
print(h1 <= h2) # le
print(h1 != h2) # ne

