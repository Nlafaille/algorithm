number = int(input("Enter a positive number: "))
for i in range(1, number + 1):
    spaces = number - i  # Spaces before the Xs
    stars = 2 * i - 1  # Number of Xs
    print(" " * spaces + "X" * stars)

for i in range(number -1, 0, -1):
    spaces = number - i
    stars = 2 * i - 1
    print(" " * spaces + "X" * stars)


