

def parse_input():
    #path = 'test.txt'
    path = 'data.txt'
    file = open(path, 'r', encoding='UTF-8')
    lines = file.readlines()
    
    forest = []
    for line in lines:
        trees = list(map( int, line.strip('\n')))
        forest.append(trees)
    return forest


def printForest(forest):
    for i in range( len(forest)):
            for j in range( len(forest[i])):
                print(forest[i][j], end='')
            print()
    return None


def is_left_visible(line, index):
    key = line[index]

    if index == 0:
        return True
    
    for num in range(index-1, -1, -1):
        if line[num] >= key:
            return False
    return True


def is_right_visible(line, index):
    key = line[index]

    if index == len(line):
        return True

    for num in range(index+1, len(line)):
        if line[num] >= key:
            return False
    return True


def is_up_visible(line, index):
    key = line[index]

    if index == 0:
        return True
    
    for num in range(index-1, -1, -1):
        if line[num] >= key:
            return False
    return True


def is_down_visible(line, index):
    key = line[index]

    if index == len(line):
        return True

    for num in range(index+1, len(line)):
        if line[num] >= key:
            return False
    return True


def get_row(row, col, forest):
    return forest[row]


def get_col(r, col, forest):
    return [row[col] for row in forest]


def main():
    forest = parse_input()
    #print(forest)

    count = 0
    printForest(forest)

    print('-----------------------')
    
    for i in range( len(forest)):
        for j in range( len(forest[i])):
            my_row = get_row(i, j, forest)
            my_col = get_col(i, j, forest)

            if is_left_visible(my_row, j) or is_right_visible(my_row, j) or is_up_visible(my_col, i) or is_down_visible(my_col, i):
                print('T', end='')
                count+=1
            
            else:
                print(' ', end='')
        print()

    print(f'Count: {count}')
    

if __name__ == '__main__':
    main()
