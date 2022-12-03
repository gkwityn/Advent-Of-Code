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
    path = './data.txt'
    file = open(path, 'r', encoding='UTF-8')
    files = file.readlines()
    return files

def rock_paper_sissor():
    pass

def main():
    """ Main Function """

    games = read_file()

    game = games[0]
    play = game.strip().split(' ')
    player1 = play[0]
    player2 = play[1]

    win = False
    if player1 = 



    


main()
