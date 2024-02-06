a = int(input("Enter the number : "))
Factorial = 1
for i in range(1, a):
    Factorial = Factorial * a
    a = a - 1
print("Factorial of a Number is", Factorial)
