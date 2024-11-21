my_list = [42,69,322,13,0,99,-5,9,8,7,-6,5]
point = 0

while point < len(my_list):
    if my_list[point] > 0:
      print(my_list[point])
      point = point + 1
      continue
    else:
      break
