# Import regexp
import re

# Open input document
puzzle_input_txt = open("puzzle-input.txt", "r")

# Read input document and save to variable
data = puzzle_input_txt.read()
puzzle_input_txt.close()

# Split string into list based on newline
sector_list = data.split("\n")

# Define Count Variables
full_overlap_count = 0
any_overlap_count = 0

# Iterate through each pair
for command in sector_list:
    # Split pair string into list of ints
    int_list = re.findall(r'\d+', command)
    # num = int_list[0]
    # p1 = int_list[1]
    # p2 = int_list[2]
    print(int_list)