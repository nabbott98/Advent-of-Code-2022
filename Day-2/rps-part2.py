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
    opp = int(i[0])
    # Results 1 = loss 2 = tie 3 = win
    result = int(i[2])

    # Game logic
    if result == 2:
        score += 3 + opp
    elif result == 3:
        play = opp + 1
        if play > 3:
            play = 1

        score += 6 + play
    
    elif result == 1:
        play = opp - 1
        if play < 1:
            play = 3

        score += play

# Print final score
print('My final score is', score)

# correct answer for my set is 10116, Complete!