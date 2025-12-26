# 9. Sum of first N natural numbers
N = int(input("Enter N: "))
s = 0
for i in range(1, N + 1):
    s += i
print("Sum:", s)
