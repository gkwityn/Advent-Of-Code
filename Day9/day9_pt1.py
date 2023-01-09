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

    for line in lines:
        l = line.split()
        
        if l[0] == 'R':
            if int(l[1]) > x_max:
                x_max = int(l[1])
           
        elif l[0] == 'L':
            x_dim -= int(l[1])
        elif l[0] == 'U':
            y_dim += int(l[1])
        elif l[0] == 'D':
            y_dim -= int(l[1])
    
    return [x_dim, y_dim]



def main():
    assert (len(sys.argv) > 1), 'Invalid CL Argument'
    data_file = str(sys.argv[1])

    lines = parse_input(data_file)
    print(lines)

    grid_size = get_grid_size(lines)

    print(f'X:{grid_size[0]}, Y:{grid_size[1]}')

if __name__ == '__main__':
    main()