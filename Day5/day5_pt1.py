class cargo:
    state = ''
    row_size = -1
    
    def build_structure(self):
        stacks = []
        lines = self.state.split('\n')

        for line in lines:
            crate = line.strip().split(' ')


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
     
    return get_stack_state(file)


def main():
    
    my_cargo = read_initial_struct()
    my_cargo.build_structure()
    print(f'State:\n{my_cargo.state}')
    print(f'RowSize: {my_cargo.row_size}')


main()
    
