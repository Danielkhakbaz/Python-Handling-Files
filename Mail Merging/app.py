import os

names = []
address = "D:/Programming/Python Repositories/Python-Handling Files/Mail Merging"

path = os.path.join(address, "Output")

if not os.path.exists(f"{address}/Output"):
    os.mkdir(path)

with open("./Names/invited_names.txt") as file:
    names.append(file.read().split("\n"))

for names in names:
    for name in names:
        with open(f"./Output/letter_for_{name}.txt", mode="w") as file:
            with open("./Letters/starting_letter.txt") as letter:
                the_letter = letter.read()
                file.write(the_letter.replace("[name]", name))
