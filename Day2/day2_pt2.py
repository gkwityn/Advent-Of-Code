"""
Advent of Code 2022
Day2, Pt.1

--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. 
"Anyway, the second column says how the round needs to end:
 X means you need to lose,
 Y means you need to end the round in a draw,
 and Z means you need to win. Good luck!"

The total score is still calculated in the same way,
but now you need to figure out what shape to
choose so the round ends as indicated.
The example above now goes like this:

In the first round, your opponent will choose Rock (A),
and you need the round to end in a draw (Y),
so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B),
and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round,
you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide,
you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?


"""


def read_file():
    """Return filelist"""

    #path = './test.txt'
    path = 'data.txt'
    file = open(path, 'r', encoding='UTF-8')
    files = file.readlines()
    return files


def rock_paper_sissor(game):

    score = 0

    play = game.strip().split(' ')
    player1 = play[0];
    player2 = play[1]

    #Opponent Plays Rock
    if player1 == 'A':
        #Lose w/ Scissors
        if player2 == 'X':
            score += 3 + 0  #3pts for Scissors + 0 points for lose
        #Draw w/ Rock
        elif player2 == 'Y':
            score += 1 + 3  #1pt for Rock + 3 points for Tie
        #Win w/ Paper
        elif player2 == 'Z':
            score += 2 + 6  #2pts for paper + 6 points for win
            
    #Opponent Plays Paper
    elif player1 == 'B':
        #Lose w/ Rock
        if player2 == 'X':
            score += 1 + 0  #1pts for Rock + 0 points for lose
        #Draw w/ Paper
        elif player2 == 'Y':
            score += 2 + 3  #2pt for Paper + 3 points for Tie
        #Win w/ Scissors
        elif player2 == 'Z':
            score += 3 + 6  #3pts for paper + 6 points for win
            
    #Opponent Plays Scissors
    elif player1 == 'C':
        #Lose w/ paper
        if player2 == 'X':
            score += 2 + 0  #2pts for Paper + 0 points for lose
        #Tie w/ Scissors
        elif player2 == 'Y':
            score += 3 + 3  #3pts for Scissors + 3 points for Tie
        #Lose w/ Rock
        elif player2 == 'Z':
            score += 1 + 6  #3pts for paper + 6 points for win
            

    return score

def main():
    """ Main Function """
    total = 0

    games = read_file()

    for game in games:
        subtotal = rock_paper_sissor(game)
        total += subtotal
        print(f"{game.strip()}: {subtotal}")
        

    print(f"Total: {total}")




    


main()
