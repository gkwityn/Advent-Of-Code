"""
Advent of Code 2022
Day1, Pt.1
"""

def find_max():
    """Function to find max cal"""
    max_cal = 0
    subtotal = 0

    file = open('./data_pt1.txt', 'r', encoding='UTF-8')

    lines = file.readlines()

    for line in lines:
        if line != '\n':
            subtotal += int(line)
            if subtotal > max_cal:
                max_cal = subtotal
        else:
            subtotal = 0
    return max_cal

print("Max: " + str(find_max()))
