"""
APPEND
"""
a = [1,2,"new",3]
a.append(4)
print("Append", a)
b = [5,6,7]
a.append(b)
print("Append a list within a list", a)

"""
CLEAR
"""
a = [1,2,"new",3]
a.clear()
print("Clear Method", a)

"""
COPY
"""
a = [1,2,"new",3]
b = a.copy()
print("Copied List", b)

"""
COUNT
"""
a = [1,2,"new",1]
b = a.count(1)
print("Number of Occurences is", b)

"""
EXTEND
"""
a = [1,2,"new",3]
b = [5,6,7]
a.extend(b)
print("Extended List is", a)

"""
INDEX
"""
a = [1,2,"new",3]
b = a.index(1)
print("Index Position of 1 is", b)

"""
INSERT
"""
a = [1,2,"new",3]
a.insert(0, 9)
print("New List is", a)

"""
POP
"""
a = [1,2,"new",3]
a.pop(2)
print("After Pop", a)

"""
REMOVE
"""
a = [1,2,"new",3]
a.remove("new")
print("After Remove", a)

"""
REVERSE
"""
a = [1,2,"new",3]
a.reverse()
print("Reversed List is", a)

"""
SORT
"""
a = [1,2,3]
a.sort(reverse=True)
print("Sort in Descending Order", a)
a = [1,2,3]
a.sort()
print("Sort in Ascending Oder", a)



