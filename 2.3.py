
dog_names = []


for i in range(6):
    dog_name = input("Enter the name of dog {}: ".format(i+1))
    dog_names.append(dog_name)


dog_names.sort(reverse=True)


print("<ul>")
for dog_name in dog_names:
    print("  <li>{}</li>".format(dog_name))
print("</ul>")
