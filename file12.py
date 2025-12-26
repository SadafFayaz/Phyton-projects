# 14. Check if number is prime


n = int(input("Enter number: "))
prime = True

if n <= 1:
    prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

if prime:
    print("Prime")
else:
    print("Not Prime")
