Li1 = [2,3,4,5,[45,56,67,78,[111,222,333,[5555,3333,[10000,50000,"python","computer"],1111,7777,8888],444,555,666,777],89,23,34]]
print("To get 5 is", Li1[3])
print(Li1[4])
Inner_List = Li1[4]
print("To get 56 is", Inner_List[1])
Inner_List_1 = Inner_List[4]
print(Inner_List_1)
# To get 222
print("To get 222 is", Inner_List_1[1])
Inner_List_2 = (Inner_List_1[3])
Inner_List_3 = Inner_List_2[2]
# To get 50000
print("To get 50000 is", Inner_List_3[1])
Inner_List_4 = Inner_List_2[2]
string1 = Inner_List_4[2]
string2 = Inner_List_4[3]
print("The string put is obtained is", string1[0]+string2[4:6])
list_1 = Li1[4]
list_2 = list_1[4]
list_3 = list_2[3]
print(list_2)
print(list_3[0])
print(list_3[4])
print(list_2[6])
print(Inner_List[5])
print(string1[4:6])
print(Inner_List_1[2])
final_list = list_2[3]
print(final_list[1])

##########
# Task 2
a = [1,2,3,4,[100,101,102,"Computer_science"],200,203]
Inner_List = a[4]
Inner_List_Element = (Inner_List[3])
print(Inner_List_Element[0:8])
print(Inner_List_Element[9::])

##########
# Task 3
a = [1,2,3,4,[101,102,103,[201,202,[999]], 666, 777]]
Inner_List = a[4]
print(Inner_List[4])
Inner_List_1 = Inner_List[3]
print(Inner_List_1[0])
print(Inner_List[1])
print(Inner_List_1[2])
print(Inner_List[5])

######
# Task 4
Li1 = [2,3,"python","hello",4,5,0]
string1_1 = Li1[2]
string1_2 = Li1[3]
print(string1_1[2:6])
print(string1_2[2:4])

#######
# Task 5
Li1 = [1,2,3,4,5,[11,22,33,44,55,[111,222,333,444],6666,7777],7777]
print(Li1[5][0])
print(Li1[5][6])
print(Li1[5][-2])
print(Li1[5][7])
print(Li1[6])
print(Li1[5][5][1])
print(Li1[-2][-1])
print(Li1[-2][2:4])

#########
# Task 6
a = {1: [1,2,3,"python"], 2:{10:"hello",20:"welcome",40: "science"}, 99: {3,4,5,6}, 40:{1:"zoology", 2:"Botany"}}
print(a.get(1)[3][0:2])
new = a.get(2)
print(new.get(10)[1::])
print(new.get(40)[3:5])
new_1 = a.get(40)
print(new_1.get(1)[0:3])
print(new_1.get(2)[0:3])
print(a)

#######
# Task 7
# Covert below two lists in to a dictionary
a = [1,2,3,4,5]

#####
# Task 8
# Convert below set in to a list
a = {5,4,3,6,2,7,1}
print(type(a))
c = list(a)
print(c)

####
# Task 9
# Remove duplicates from below list
a = [5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]
b = set(a)
print(type(b))

#####
# Task 10
# Convert below one to tuple
a = [5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]
b = tuple(a)
print(type(b))

