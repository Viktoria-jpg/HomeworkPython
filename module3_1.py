calls = 0
def count_calls():
    global calls
    calls = calls + 1
    return calls
def string_info(a):
    count_calls()
    b = (len(a), a.upper(), a.lower())
    return (b)
def is_contains(string, List_to_search):
    count_calls()
    string = str(string).lower()
    List_to_search = list(List_to_search)
    for i in range(len(List_to_search)):
        if str(List_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return (result)
print(string_info('Cat'))
print(string_info('Cap of tea'))
print(string_info('Students'))
print(is_contains('Cat',['CaTaclysm','CaT','Catalog']))
print(is_contains('Tea',['team','tear']))
print(calls)