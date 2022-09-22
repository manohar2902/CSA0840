list1 = [1,2,4]
list2= [1,3,4]

sorted_list =[]
while list1 and list2:
    if list1[0] <  list2[0]:
        sorted_list.append(list1.pop(0))
    else:
        sorted_list.append(list2.pop(0))
sorted_list += list1
sorted_list += list2
print(sorted_list)