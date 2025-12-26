# 13. Fibonacci series up to N terms


N = int(input("Enter terms: "))

a, b = 0, 1
print(a, b, end=" ")

for i in range(N - 2):
    c = a + b
    print(c, end=" ")
    a = b
    b = c
