a = [1,2,3,4]
sum = 0
for i in a:
    sum = sum + i
print("The mean is", sum/len(a))
Midpoint = len(a) // 2
if len(a) % 2 == 0:
    print("Median is", a[Midpoint - 1], a[Midpoint])
else:
    print("Median is", a[Midpoint])
