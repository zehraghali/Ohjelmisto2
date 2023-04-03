import random

def roll_dice():
    return random.randint(1, 6)
print("<ul>")
while True:
    roll = roll_dice()
    print(f"<li>{roll}</li>")
    if roll == 6:
        break
print("</ul>")
