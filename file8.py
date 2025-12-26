# 10. Count digits in a number (while)


num = int(input("Enter number: "))
count = 0
n = num

while n > 0:
    n //= 10
    count += 1

print("Digits:", count)
