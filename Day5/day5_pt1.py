class cargo:
    state = ''
    row_size = -1

def get_stack_state(file):
    init_cargo = cargo()

    lines = file.readlines()
    init_state = ''

    for line in lines:
        if line[1] == '1':
            rows = line.strip().split(sep='   ')
            break
        else:
            init_state += line
        
    
    init_cargo.row_size = len(rows)
    init_cargo.state = init_state

    return init_cargo

def read_initial_struct():
    #path = './test.txt'
    path = './data.txt'
    file = open(path, 'r', encoding='UTF-8')
    
    init_cargo = get_stack_state(file)
    
    return init_cargo


def main():
    
    my_cargo = read_initial_struct()
    print(f'State:\n{my_cargo.state}')
    print(f'RowSize: {my_cargo.row_size}')


main()
    
