"""
TASK 6
"""
string1 = "computer"
string2 = "mathematics"
#string1_list = list(string1)
#string2_list = list(string2)
#print(str(string1_list[0])+str(len(list(string1)) - 2)+str(string1_list[len(string1_list)-1]))
#print(str(string2_list[0])+str(len(list(string2)) - 2)+str(string2_list[len(string2_list)-1]))

#print("hello world")
#print(input("What is your name : "))

print(string1[0]+str(len(string1[1:-1]))+string1[-1])
print(string2[0]+str(len(string2[1:-1]))+string2[-1])