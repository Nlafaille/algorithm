count = 0

while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    if number > 0:
        count += 1
print(f"{count} positive numbers were entered")