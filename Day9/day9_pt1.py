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
    x_pos = 0
    y_pos = 0

    for line in lines:
        l = line.split()
        dir = l[0]
        move = int(l[1])


        if dir == 'R':
            x_pos += move
            if x_pos > x_max:
                x_max = x_pos

        elif dir == 'L':
            x_pos -= move

        elif dir == 'U':
            y_pos += move
            if y_pos > y_max:
                y_max = y_pos

        elif dir == 'D':
            y_pos -= move

    print(f'Grid Size: [{x_max}, {y_max}]')

    return [x_max+1, y_max+1]



def print_state(x_pos, y_pos):
    
    for y in range(grid_size[0], -1, -1):
        print('')
        for x in range(grid_size[1]):
            if x == x_pos and y == y_pos:
                print('H', end='')
            else:
                print('.', end='')
    print()


def moves(lines):
    x_pos = 0
    y_pos = 0
    print_state(x_pos, y_pos)

    for line in lines:
        
        
        l = line.split()
        dir = l[0]
        move = int(l[1])

        if dir == 'R':
            x_pos += move

        elif dir == 'L':
            x_pos -= move

        elif dir == 'U':
            y_pos += move

        elif dir == 'D':
            y_pos -= move
        print_state(x_pos, y_pos)

def main():
    assert (len(sys.argv) == 2), 'Invalid CL Argument'
    data_file = str(sys.argv[1])

    instr = parse_input(data_file)
    print(instr)

    global grid_size
    grid_size = get_grid_size(instr)

    moves(instr)
    

if __name__ == '__main__':
    main()