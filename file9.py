# 11. Reverse a number (loop)

num = int(input("Enter number: "))
rev = 0
n = num

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print("Reversed:", rev)