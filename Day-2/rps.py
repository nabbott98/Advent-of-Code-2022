# Open input document
input_guide_txt = open("input-guide.txt", "r")

# Read input document and save to variable
data = input_guide_txt.read()
input_guide_txt.close()

# Replace ABC and XYZ with 123 and split list by newline
split_list = data.replace('A', '1').replace('B', '2').replace('C', '3').replace('X', '1').replace('Y', '2').replace('Z', '3').split("\n")

# Define Score Variable
score = 0

for i in split_list:
    # Pull values from string and convert them to int types
    me = int(i[2])
    opp = int(i[0])

    # Game logic
    if me == opp:
        score += 3 + me
    elif me == 3 and opp == 2 or me == 2 and opp == 1 or me == 1 and opp == 3:
        score += 6 + me
    else:
        score += me

    print(score)

print('My final score is', score)

# Answer based on my data is 8392