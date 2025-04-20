n = input("Enter a number: ")
if n.isdigit():
    n = int(n)
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")
else:
    print("Invalid input, please enter a number")

p = input("Enter a number: ")