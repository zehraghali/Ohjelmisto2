import random

def roll_dice(num_sides):
    return random.randint(1, num_sides)
num_sides = int(input("Enter the number of sides on the dice: "))
print("<ul>")
while True:
    roll = roll_dice(num_sides)
    print(f"<li>{roll}</li>")
    if roll == num_sides:
        break
print("</ul>")
