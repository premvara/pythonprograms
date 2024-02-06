print("Program to remove duplicate elements and to sort them")
a = [7,2,3,1,1]
b = []
for i in a:
    if i in b:
        print("Element Exists")
    else:
        b.append(i)
print("The list without duplicate elements is ", b)
first_element = b[0]
for i in range(0, len(b)):
    for j in range(1+i, len(b)):
        if b[i] > b[j]:
            b[i], b[j] = b[j], b[i]
print(b)



