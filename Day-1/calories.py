# Open input document
elves = open("input.txt", "r")

# Read input document and save to variable
data = elves.read()
elves.close()

# Split list by newline
elves_list = data.split("\n")

# Declare new array for elf totals and variable to tally up each elfs total
elf_totals = []
total = 0

# Iterate through list once and add each consecutive number until a blank string
for i in elves_list:
    # is this indicie a blank string?
    if i == '':
        elf_totals.append(total)
        total = 0
    # if not add to total
    else:
        total += int(i)

# print max value in new list! Yummy!
print('The elf with the most calories is carrying', max(elf_totals), 'calories! Yummy!')

# Print the total of the top 3 elves
# Sum(sorted(elf_totals, reverse = True)[:3]) broken down
    # Sort elf totals array highest --> lowest value, then slice the first 3 since those will be the largest
    # Sum that smaller list of 3 values
print('The 3 elves with the most calories are carrying', sum(sorted(elf_totals, reverse = True)[:3]), 'calories total! Yummy!')