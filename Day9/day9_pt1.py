import sys


def parse_input(path):
    try:
        file = open(path, 'r', encoding='UTF-8')
    except FileNotFoundError:
        print('File not found.')
        sys.exit(1)
    else:
        print(f'{path} open sucessfully.')

        lines = file.readlines()
        instructions =[]

        for line in lines:
            instructions.append(line.strip('\n'))            
       
        return instructions


def get_grid_size(lines):
    x_max = 0
    y_max = 0
    head_x_pos = 0
    head_y_pos = 0

    for line in lines:
        l = line.split()
        dir = l[0]
        move = int(l[1])


        if dir == 'R':
            head_x_pos += move
            if head_x_pos > x_max:
                x_max = head_x_pos

        elif dir == 'L':
            head_x_pos -= move

        elif dir == 'U':
            head_y_pos += move
            if head_y_pos > y_max:
                y_max = head_y_pos

        elif dir == 'D':
            head_y_pos -= move

    print(f'Grid Size: [{x_max}, {y_max}]')

    return [x_max, y_max]

#TODO: DEBUG GRID SIZE
def print_state(head_x_pos, head_y_pos, tail_x_pos, tail_y_pos):
    
    for y in range(grid_size[0], 0, -1):
        print('')
        for x in range(grid_size[1]):
           
            #Head Location
            if x == head_x_pos and y == head_y_pos:
                print('H', end='')
            #Tail Location
            elif x == tail_x_pos and y == tail_y_pos:
                print('T', end='')
            #Empty Location
            else:
                print('.', end='')
    print()
    return


def moves(lines):
    head_x_pos, head_y_pos = 0,0
    tail_x_pos, tail_y_pos = 0,0
    print_state(head_x_pos, head_y_pos, tail_x_pos, tail_y_pos)

    visited = []
    visited.append([tail_x_pos, tail_y_pos])

    for line in lines:

        l = line.split()
        dir = l[0]
        move = int(l[1])

        if dir == 'R':
            for step in range(move):
                head_x_pos += 1
                print_state(head_x_pos, head_y_pos, tail_x_pos, tail_y_pos)

                if check_adjacent(head_x_pos, head_y_pos, tail_x_pos, tail_y_pos):
                    continue
                else:
                    tail_x_pos, tail_y_pos = update_tail(head_x_pos, head_y_pos, tail_x_pos, tail_y_pos)
                    print_state(head_x_pos, head_y_pos, tail_x_pos, tail_y_pos)

        elif dir == 'L':
            for step in range(move):
                head_x_pos -= 1
                print_state(head_x_pos, head_y_pos, tail_x_pos, tail_y_pos)

                if check_adjacent(head_x_pos, head_y_pos, tail_x_pos, tail_y_pos):
                    continue
                else:
                    tail_x_pos, tail_y_pos = update_tail(head_x_pos, head_y_pos, tail_x_pos, tail_y_pos)
                    print_state(head_x_pos, head_y_pos, tail_x_pos, tail_y_pos)

        elif dir == 'U':
            for step in range(move):
                head_y_pos += 1
                print_state(head_x_pos, head_y_pos, tail_x_pos, tail_y_pos)

                if check_adjacent(head_x_pos, head_y_pos, tail_x_pos, tail_y_pos):
                    continue
                else:
                    tail_x_pos, tail_y_pos = update_tail(head_x_pos, head_y_pos, tail_x_pos, tail_y_pos)
                    print_state(head_x_pos, head_y_pos, tail_x_pos, tail_y_pos)

        elif dir == 'D':
            for step in range(move):
                head_y_pos -= 1
                print_state(head_x_pos, head_y_pos, tail_x_pos, tail_y_pos)

                if check_adjacent(head_x_pos, head_y_pos, tail_x_pos, tail_y_pos):
                    continue
                else:
                    tail_x_pos, tail_y_pos = update_tail(head_x_pos, head_y_pos, tail_x_pos, tail_y_pos)
                    print_state(head_x_pos, head_y_pos, tail_x_pos, tail_y_pos)

    return visited

def check_adjacent(head_x_pos, head_y_pos, tail_x_pos, tail_y_pos):
    if head_x_pos == tail_x_pos and head_y_pos == tail_y_pos:
        return True

    #Check if directly left or right
    if ((head_x_pos == tail_x_pos + 1) and (head_y_pos == tail_y_pos)) or ((head_x_pos == tail_x_pos - 1) and (head_y_pos == tail_y_pos)):
        return True
    #Check if directly up or down
    elif ((head_y_pos == tail_y_pos +1) and (head_x_pos ==  tail_y_pos)) or ((head_y_pos == tail_y_pos -1) and (head_x_pos ==  tail_y_pos)):
        return True
    #check Diagonal left up or right up
    elif ((head_x_pos == tail_x_pos - 1) and (head_y_pos == tail_y_pos + 1)) or ((head_x_pos == tail_x_pos + 1) and (head_y_pos == tail_y_pos + 1)):
        return True
    #check Diagonal left down or right down
    elif ((head_x_pos == tail_x_pos - 1) and (head_y_pos == tail_y_pos - 1)) or ((head_x_pos == tail_x_pos + 1) and (head_y_pos == tail_y_pos - 1)):
        return True

    return False



def update_tail(head_x_pos, head_y_pos, tail_x_pos, tail_y_pos):

    #head and tail at same position, return same pos
    if head_x_pos == tail_x_pos and head_y_pos == tail_y_pos:
        return  tail_x_pos, tail_y_pos
    #Same row
    elif head_y_pos == tail_y_pos:
        #if +1 to right or left of head, return same pos
        if head_x_pos == (tail_x_pos + 1) or head_x_pos == (tail_x_pos - 1):
            return tail_x_pos, tail_y_pos
        #if +2 to right, move tail to right
        elif head_x_pos == (tail_x_pos + 2):
            return tail_x_pos + 1, tail_y_pos
        #if -2 to left, move tail to left
        elif head_x_pos == (tail_x_pos - 2):
            return tail_x_pos - 1, tail_y_pos
    #Same Col
    elif head_x_pos == tail_x_pos:
        #if +1 up or down, return same pos
        if head_y_pos == (tail_y_pos + 1) or head_y_pos == (tail_y_pos - 1):
            return tail_x_pos, tail_y_pos
        #if +2 up, move tail up
        elif head_y_pos == (tail_y_pos + 2):
            return tail_x_pos, tail_y_pos + 1
        #if -2 down, move tail up
        elif head_y_pos == (tail_y_pos - 2):
            return tail_x_pos, tail_y_pos - 1
    #Diagonal
    else:
        #up
        #if right +1 and up +2
        # .....    .....
        # ..H..    ..H..
        # ..... -> ..T..
        # .T...    .....
        # .....    .....
        if  head_x_pos == (tail_x_pos + 1) and head_y_pos == (tail_y_pos + 2):
            return tail_x_pos + 1, tail_y_pos +1

        #up2
        #if left -1 and up +2
        # .....    .....
        # ..H..    ..H..
        # ..... -> ..T..
        # ...T.    .....
        # .....    .....
        elif head_x_pos == (tail_x_pos - 1) and head_y_pos == (tail_y_pos + 2): 
            return tail_x_pos - 1, tail_y_pos +1

        #Right
        #if right +2 and up +1
        # .....    .....
        # .....    .....
        # ...H. -> ..TH.
        # .t...    .....
        # .....    .....
        elif  head_x_pos == (tail_x_pos + 2) and head_y_pos == (tail_y_pos + 1): 
            return tail_x_pos + 1, tail_y_pos +1

        #Right2
        #if right +2 and up +1
        # .....    .....
        # .t...    .....
        # ...H. -> ..TH.
        # .....    .....
        # .....    .....
        elif  head_x_pos == (tail_x_pos + 2) and head_y_pos == (tail_y_pos - 1): 
            return tail_x_pos + 1, tail_y_pos - 1

        #Left
        #if left -2 and up +1   
        # .....    .....
        # .....    .....
        # .H... -> .HT..
        # ...T.    .....
        # .....    .....
        elif head_x_pos == (tail_x_pos - 2) and head_y_pos == (tail_y_pos + 1): 
            return tail_x_pos - 1, tail_y_pos +1

        #Left2
        #if left -2 and up -1  
        # .....    .....
        # ...T.    .....
        # .H... -> .HT..
        # .....    .....
        # .....    .....
        elif head_x_pos == (tail_x_pos - 2) and head_y_pos == (tail_y_pos - 1): 
            return tail_x_pos - 1, tail_y_pos -1

        #Down
        #if right +1 and down -1  
        # .....    .....
        # .T...    .....
        # ..... -> ..T..
        # ..H..    ..H..
        # .....    .....
        elif head_x_pos == (tail_x_pos + 1) and head_y_pos == (tail_y_pos - 2): 
            return tail_x_pos +1, tail_y_pos -1
        
        #Down2
        #if left-1 and up -2  
        # .....    .....
        # ...T.    .....
        # ..... -> ..T..
        # ..H..    ..H..
        # .....    .....
        elif head_x_pos == (tail_x_pos + 1) and head_y_pos == (tail_y_pos - 2): 
            return tail_x_pos -1, tail_y_pos -1

        return 99, 99


def main():
    assert (len(sys.argv) == 2), 'Invalid CL Argument'
    data_file = str(sys.argv[1])

    instr = parse_input(data_file)
    print(instr)

    global grid_size
    grid_size = get_grid_size(instr)

    visited = moves(instr)
    

if __name__ == '__main__':
    main()