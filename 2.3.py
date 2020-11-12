list1 = ['I', '3657', 'am', '350', 'a', '341', 'student', '12']
list1 = [item for item in list1 if not item.isnumeric()]
print(list1)