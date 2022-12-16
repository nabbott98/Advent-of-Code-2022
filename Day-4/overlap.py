# Open input document
puzzle_input_txt = open("puzzle-input.txt", "r")

# Read input document and save to variable
data = puzzle_input_txt.read()
puzzle_input_txt.close()

# Split string into list based on newline
sector_list = data.split("\n")

# Define Count Variable
count = 0

# Iterate through each pair
for pair in sector_list:
    # Split pair string into list of ints
    int_list = [int(x) for x in pair.replace('-',',').split(',')]
    l1 = int_list[0]
    h1 = int_list[1]
    l2 = int_list[2]
    h2 = int_list[3]

    # Test for overlapping
    if l1 <= l2 and h2 <= h1 or l1 >= l2 and h2 >= h1:
        count += 1


print ('Number of overlapping sectors', count)

# My data set answer is 513, Complete!
