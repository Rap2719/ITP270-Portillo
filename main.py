def middle_element(lst):
  if len(lst) % 2 == 0:
    return (lst[int(len(lst) / 2 )] + lst[int(len(lst) / 2 ) - 1]) / 2
  else:
    return lst[int(len(lst) / 2)]
print(middle_element([5, 2, -10, -4, 4, 5])) #This should print -7.0







  





