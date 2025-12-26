# Sum of digits of a number


num = int(input("Enter number: "))
s = 0
n = num

while n > 0:
    s += n % 10
    n //= 10

print("Sum of digits:", s)