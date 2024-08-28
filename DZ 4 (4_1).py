list1 = [1,2,0,5,4,0,1,7,0,0,1]
new_list = []
for num in list1:
    if num != 0:
        new_list.append(num)
zeros_list = len(list1) - len(new_list)
new_list.extend([0] * zeros_list)
print(new_list)