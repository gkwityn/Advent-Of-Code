"""
Advent of Code 2022
Day2, Pt.1

  The first column is what your opponent is going to play: 
  A for Rock, B for Paper, and C for Scissors.

  The second column, you reason, must be what you should play in response:
  X for Rock, Y for Paper, and Z for Scissors

  Scoring:
  1 for Rock, 2 for Paper, and 3 for Scissors
  +
  plus the score for the outcome of the round
  (0 if you lost, 3 if the round was a draw, and 6 if you won


"""
def read_file():
    """Return filelist"""

    # path = './data.txt'
    path = 'data.txt'
    file = open(path, 'r', encoding='UTF-8')
    files = file.readlines()
    return files


def rock_paper_sissor(game):

    score = 0

    play = game.strip().split(' ')
    player1 = play[0];
    player2 = play[1]

    if player2 == 'X':
        score += 1
    elif player2 == 'Y':
        score += 2
    elif player2 == 'Z':
        score += 3
    
    #Opponent Plays Rock
    if player1 == 'A':
        #Paper - You Win
        if player2 == 'Y':
            score += 6
        #Rock - Tie
        elif player2 == 'X':
            score += 3
    
    #Opponent Plays Paper
    elif player1 == 'B':
        #Scissors -You Win
        if player2 == 'Z':
            score += 6
        #Paper - Tie
        elif player2 == 'Y':
            score += 3
    
    #Opponent Plays Scissors
    elif player1 == 'C':
        #Rock - You Win
        if player2 == 'X':
           score += 6
        #Scissors - Tie
        elif player2 == 'Z':
            score += 3
    
    return score

def main():
    """ Main Function """
    total = 0

    games = read_file()

    for game in games:
        total += rock_paper_sissor(game)
        #print(f"{game.strip()}: {score}")

    print(f"Total: {total}")




    


main()
