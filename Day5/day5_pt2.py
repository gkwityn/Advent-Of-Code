def build_stack(lines):
    size = 9
    stack = []

    for i in range(0, size):
        stack.append([])

    for line in lines:
        j = 0
        
        for i in range(0, len(line), 4):
            if line[i+1] != ' ':
                stack[j].append(line[i+1])
            j+=1

    #reverse each column/stack
    for list in stack:
        list.reverse()

    return stack


def parse_data(file):

    lines = file.readlines()
    init_state = []

    for line in lines:
        if line[1] == '1':
            # rows = line.strip().split(sep='   ')
            break
        else:
            init_state.append(line.strip('\n'))

    file.close()
    return init_state    
        
    
def read_initial_struct():
    #path = './test.txt'
    path = './data.txt'
    file = open(path, 'r', encoding='UTF-8')
    init_state = parse_data(file)
    
    return init_state


def read_instr():
    path = './data.txt'
    file = open(path, 'r', encoding='UTF-8')
    lines = file.readlines()

    instr_list = []

    for line in lines:
        if 'move' in line:
            instr_list.append(line)
    return instr_list


def follow_instr(instr_list, stack):
    
    for instr in instr_list:
        #Examples
        #move 1 from 2 to 1
        #move 3 from 1 to 3
        f_instr = instr.split(sep=" ")
        move_num = int(f_instr[1])
        src = int(f_instr[3])-1
        dest = int(f_instr[5])-1

        move_list = []
        for i in range(move_num):
            temp = stack[src].pop() 
            move_list.insert(0, temp)

        for el in move_list:
            stack[dest].append(el)
    
    return stack

def print_stack(stack):
    print('Original:')
    for el in stack:
        print(el)

    print('Last Elements:')
    for el in stack:
        print(f'{el[-1]}', end='')
    print('\n')

def main():
    
    init_state = read_initial_struct()
    stack = build_stack(init_state)
    instr_list = read_instr()

    stack = follow_instr(instr_list, stack)

    print_stack(stack)
    # for el in stack:
    #     print(el)
    # for single in instr:
    #     print(single)

main()
    
