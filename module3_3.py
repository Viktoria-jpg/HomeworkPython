
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = (7, 'Кот', False)
values_dict = {'a' : 2, 'b' : 'Чёрный кот', 'c' : True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ("Белый кот", 74)
print_params(*values_list_2, 42)

