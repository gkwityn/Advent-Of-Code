"""
Advent of Code 2022
Day1, Pt.2

--- Part Two ---
By the time you calculate the answer to the Elves' question,
they've already realized that the Elf carrying the most Calories
of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like
to know the total Calories carried by the top three Elves carrying the most Calories.
That way, even if one of those Elves runs out of snacks, they still have two backups.
In the example above, the top three Elves are the fourth Elf (with 24000 Calories),
then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories).

The sum of the Calories carried by these three elves is 45000.
Find the top three Elves carrying the most Calories.
How many Calories are those Elves carrying in total?

"""

def get_calories():
    """
        Function to extract each elf's calorie sum from file.
        Returns a list of sums of each elfs calorie total.
    """

    subtotal = 0
    elves = []

    file = open('./data_pt1.txt', 'r', encoding='UTF-8')

    lines = file.readlines()

    for line in lines:
        if line != '\n':
            subtotal += int(line)
        else:
            elves.append(subtotal)
            subtotal = 0
    return elves

def main():
    """
        1) Main Method to get the list of elfs calorie sum
        2) Sort the list in ascending order
        3) Sum the top 3 calorie amounts.
    """
    elves = get_calories()
    elves.sort()

    print(elves[-3:])
    print(sum(elves[-3:]))

main()
