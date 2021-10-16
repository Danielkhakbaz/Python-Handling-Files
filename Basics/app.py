with open("text.txt") as file:
    print(file.read())

with open("text.txt", mode="a") as file:
    file.write("\nThis is a new text.")

with open("text1.txt", mode="w") as file:
    file.write("This is a new text in a new file.")