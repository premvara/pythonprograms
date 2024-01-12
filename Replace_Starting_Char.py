string1 = "maths"
string2 = "science"
lengthofstring1 = len(string1)
lengthofstring2 = len(string2)
print(string1[0] + string2[1:] + string2[0] + string1[1:] + str(len(string1)) + str(len(string2)) + string1[len(string1) // 2] + string2[len(string2) // 2])

