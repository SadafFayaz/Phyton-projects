#Account Program (deposit, withdraw, check balance)

balance = 0

while True:
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = float(input("Enter amount: "))
        balance += amount
        print("Deposited:", amount)

    elif choice == 2:
        amount = float(input("Enter amount: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance!")

    elif choice == 3:
        print("Current Balance:", balance)

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")

