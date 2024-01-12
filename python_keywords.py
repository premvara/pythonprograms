"""
AND Keyword
"""
a = 10
b = 30
print("To validate the AND Keyword in Python")
print(a == 10 and b == 20)

"""
IN Keyword
"""
a = (1, 2 ,3)
print(type(a))
print("To validate the IN Keyword in Python")
if 7 in a:
    print("Valid")
else:
    print("Invalid")

"""
IS Keyword
"""
a = 3
b = 3
c = (6, 7, 8)
d = (1, 2, 3)
print(type(d))
print("To validate the IS Keyword in Python")
if a is b:
    print("Valid")
else:
    print("Invalid")
print("Are both the lists same - ", c is d)

"""
NOT KEYWORD
"""
a = 10
b = 20
c = a < b
print("NOT KEYWORD", not c)
New = bool("Large")
print("=====", New)
print("Not Keyword validation is", not New)

"""
OR KEYWORD
"""
print("OR Keyword Validation is", 1 > 3 or 1 < 0)

"""
DEL Keyword
"""
a = 10
print("====", a)
del a
#print("DEL Keyword is", a)