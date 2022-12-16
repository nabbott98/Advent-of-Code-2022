# Open input document
puzzle_input_txt = open("puzzle-input.txt", "r")

# Read input document and save to variable
data = puzzle_input_txt.read()
puzzle_input_txt.close()

# Split string into list based on newline
split_list = data.split("\n")

priority_sum = 0

for string in split_list:
    # Find the common item in each compartment
    compartment_1, compartment_2 = string[:len(string) // 2], string[len(string) // 2:]
    a = list(set(compartment_1) & set(compartment_2))
    common_item = a[0]

    # Calculate common item priority and add to running sum
    # Use ASCII numbers to do quick math, capital letters start at 27 so add 26
    if common_item.islower():
        priority_sum += ord(common_item) - 96
    else:
        priority_sum += ord(common_item) - 64 + 26

# print('The total sum of the priorities is', priority_sum)

# Correct answer for my data 8493! Part 1 Complete!

# Part 2
group_priority_sum = 0

for i in range(int(len(split_list)/3)):
    # Find common items between 3 strings
    a = list(set(split_list[i * 3]) & set(split_list[i * 3 + 1]) & set(split_list[i * 3 + 2]))
    common_item = a[0]

    # Calculate common item priority and add to running sum
    # Use ASCII numbers to do quick math, capital letters start at 27 so add 26
    if common_item.islower():
        group_priority_sum += ord(common_item) - 96
    else:
        group_priority_sum += ord(common_item) - 64 + 26

print('The total sum of the group priorities is', group_priority_sum)

# Correct answer for my data set 2552 Complete!