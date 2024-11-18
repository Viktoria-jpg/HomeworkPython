import random

def fell_number ():
    numbers = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    first_number = random.choice(numbers)
    return first_number

on_stone = int(fell_number())
print('Число на первом каменном поле: ', on_stone)

result = []
for i in range(1,20):
    for j in range(1,20):
        if on_stone % (i+j) == 0:
            result.append(i)
            result.append((j))


print("Возможные карианты для второго поля: ", *result)


