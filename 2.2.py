
num_participants = int(input("Enter the number of participants: "))


participants = []


for i in range(num_participants):
    participant = input("Enter the name of participant {}: ".format(i+1))
    participants.append(participant)


participants.sort()


print("<ol>")
for participant in participants:
    print("  <li>{}</li>".format(participant))
print("</ol>")
