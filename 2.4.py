numbers = []

while True:
    num = int(input("Enter a number (or 0 to stop): "))
    if num == 0:
        break
    numbers.append(num)

numbers.sort(reverse=True)

print("The numbers in descending order are:")
for num in numbers:
    print(num)
