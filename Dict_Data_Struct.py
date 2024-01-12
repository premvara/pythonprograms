# Dict Data Structure
a = {1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
First_element = (a[3])
# Extract "bobtn" from above dictionary
Assement_1 = First_element[0]
print(Assement_1[0:9:2])
# Extract "bobtn" from above dictionary
Assement_2 = First_element[2]
print(Assement_2[0:7:5])
# print all keys in dictionary and convert it into tuples
print(type(tuple(a.keys())))
Second_Element = (a[2])
sum_ouput = sum(Second_Element)
print("Average is", int(sum_ouput / 2))
