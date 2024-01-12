a = "helloworld"
lengthof = len(a)
print(lengthof)
Quotient = lengthof // 2
print("Quotient is", Quotient)
Remainder = lengthof % 2
print("Remainder is", Remainder)
if Remainder == 1:
    Quotient = Quotient
    print("Middle of String is", a[Quotient])
else:
    print("Middle of String is", a[Quotient - 1], a[Quotient])