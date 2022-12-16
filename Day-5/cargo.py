# Open input document
puzzle_input_txt = open("puzzle-input.txt", "r")

# Read input document and save to variable
data = puzzle_input_txt.read()
puzzle_input_txt.close()

# Split string into list based on newline
sector_list = data.split("\n")

# Define cargo position lists
# [V]     [B]                     [C]
# [C]     [N] [G]         [W]     [P]
# [W]     [C] [Q] [S]     [C]     [M]
# [L]     [W] [B] [Z]     [F] [S] [V]
# [R]     [G] [H] [F] [P] [V] [M] [T]
# [M] [L] [R] [D] [L] [N] [P] [D] [W]
# [F] [Q] [S] [C] [G] [G] [Z] [P] [N]
# [Q] [D] [P] [L] [V] [D] [D] [C] [Z]
#  1   2   3   4   5   6   7   8   9 

# Store in arrays since pop and push methods are exactley what we want to do here
cargo = {
    1: ['Q', 'F', 'M','R', 'L', 'W', 'C', 'V'],
    2: ['D', 'Q', 'L'],
    3: ['P', 'S', 'R', 'G', 'W', 'C', 'N', 'B'],
    4: ['L', 'C', 'D', 'H', 'B', 'Q', 'G'],
    5: ['V', 'G', 'L', 'F', 'Z', 'S'],
    6: ['D', 'G', 'N', 'P'],
    7: ['D', 'Z', 'P', 'V', 'F', 'C', 'W'],
    8: ['C', 'P', 'D', 'M', 'S'],
    9: ['Z', 'N', 'W', 'T', 'V', 'M', 'P', 'C']
}


# Iterate through each pair
for pair in sector_list:
    # Split pair string into list of ints
    int_list = [int(x) for x in pair.replace('-',',').split(',')]
    num = int_list[0]
    p1 = int_list[1]
    p2 = int_list[2]