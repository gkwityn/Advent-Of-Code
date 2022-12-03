"""
Advent of Code 2022
Day1, Pt.2

--- Part Two ---
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.
To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. 
That way, even if one of those Elves runs out of snacks, they still have two backups.
In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). 
The sum of the Calories carried by these three elves is 45000.
Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

"""

def find_max():
    """Function to find max cal"""
    
    subtotal = 0
    top3 = []

    file = open('./data_pt1.txt', 'r', encoding='UTF-8')

    lines = file.readlines()

    for line in lines:
        if line == '\n':
            pass
        else:
            pass

    




print("Max: " + str(find_max()))