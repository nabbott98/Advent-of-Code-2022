# Open input document
puzzle_input_txt = open("puzzle-input.txt", "r")

# Read input document and save to variable
data = puzzle_input_txt.read()
puzzle_input_txt.close()

# Replace ABC and XYZ with 123 and split list by newline
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
    print(priority_sum)

print('The total sum of the priorities is', priority_sum)

# Correct answer for my data 8493! Part 1 Complete!
