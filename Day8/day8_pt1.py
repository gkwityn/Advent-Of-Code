def parse_input():
    path = 'test.txt'
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

def is_row_visible(row, col, forest):

    full = forest[row]
    key = forest[row][col]


    if col == 0 or col == len(full)-1:
        return True
    # else:
    #     for i in range(1, len(full)):
    #         if i  == col and visible == False
    #         if full[i] < key :
    #             visible = True
    #         else:
    #             visible = False
    # return visible


def is_col_visible(row, col, forest):
    full = [i[col] for i in forest]
    key = forest[row][col]

    if row == 0 or row == len(full)-1:
        return True
    # else:
    #     for i in range(1, len(full)):
    #         if i >= key :
    #             return False
    # return True


def main():
    forest = parse_input()
    #print(forest)

    count = 0
    printForest(forest)

    print('-----------------------')
    
    for i in range( len(forest)):
        for j in range( len(forest[i])):
            if is_row_visible(i, j, forest) or is_col_visible(i, j, forest):
                print('T', end='')
                count+=1
            else:
                print(' ', end='')
        print()

    print(f'Count: {count}')
    
main()
