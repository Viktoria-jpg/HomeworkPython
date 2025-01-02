def count_numbers_and_strings(data):
    num_count = 0
    str_count = 0

    def recursive_count(item):
        nonlocal num_count, str_count

        if isinstance(item, (int, float)):
            num_count += 1
        elif isinstance(item, str):
            str_count += 1
        elif isinstance(item, (list, tuple, set)):
            for sub_item in item:
                recursive_count(sub_item)
        elif isinstance(item, dict):
            for key, value in item.items():
                recursive_count(key)
                recursive_count(value)

    recursive_count(data)
    return num_count, str_count

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

numbers_count, strings_count = count_numbers_and_strings(data_structure)
print(f"Количество чисел: {numbers_count}")
print(f"Количество строк: {strings_count}")





