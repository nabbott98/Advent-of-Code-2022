elves = open("input.txt", "r")

data = elves.read()

elves_list = data.split("\n")

print(elves_list)
elves.close()