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

    return [x_max+1, y_max+1]


def print_state(head_x_pos, head_y_pos):
    
    for y in range(grid_size[0], -1, -1):
        print('')
        for x in range(grid_size[1]):
            if x == head_x_pos and y == head_y_pos:
                print('H', end='')
            else:
                print('.', end='')
    print()
    return


def moves(lines):
    head_x_pos, head_y_pos = 0,0
    tail_x_pos, tail_y_pos = 0,0
    print_state(head_x_pos, head_y_pos)

    visited = []
    visited.append([tail_x_pos, tail_y_pos])

    for line in lines:

        l = line.split()
        dir = l[0]
        move = int(l[1])

        if dir == 'R':
            for step in range(move):
                head_x_pos += 1
                print_state(head_x_pos, head_y_pos)

        elif dir == 'L':
            for step in range(move):
                head_x_pos -= 1
                print_state(head_x_pos, head_y_pos)

        elif dir == 'U':
            for step in range(move):
                head_y_pos += 1
                print_state(head_x_pos, head_y_pos)

        elif dir == 'D':
            for step in range(move):
                head_y_pos -= 1
                print_state(head_x_pos, head_y_pos)

    return visited


def update_tail(head_x_pos, head_y_pos, tail_x_pos, tail_y_pos):

    #head and tail at same position
    if head_x_pos == tail_x_pos and head_y_pos == tail_y_pos:
        return  tail_x_pos, tail_y_pos
    #Same row
    elif 


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