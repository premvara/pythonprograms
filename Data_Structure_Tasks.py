a = []
b = [5,6,7,8]
new_list = a + b
new_list.append(8)
new_list.append(9)
new_list.append(1)
new_list.append(5)
new_list.append(6)
new_list.append(7)
new_list.append(8)
new_list.append(1)
print(new_list)

to_be_counted = 8
print(new_list.count(to_be_counted))
print("Sum of List with Min and Max", sum(new_list) + min(new_list) + max(new_list))
print("Median is", new_list[len(new_list) // 2 - 1], new_list[len(new_list) // 2],)

print("Remove Duplicates is", set(new_list))





