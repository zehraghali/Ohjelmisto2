numbers = []

while True:
    num = int(input("Enter a number: "))
    if num in numbers:
        print(f"The number {num} has already been entered!")
        break
    numbers.append(num)

numbers.sort()

print("The numbers in ascending order are:")
for num in numbers:
    print(num)
