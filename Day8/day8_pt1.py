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


def is_left_visible():
    pass

def get_row(row, forest):
    return forest[row]

def get_col():
    pass


def is_row_visible(row, col, forest):

    full_row = forest[row]
    key = forest[row][col]

    left, right = True, True

    if row == 0 or row == len(forest)-1:
        return True
    else:
        for i in range(0,full_row[col]):
            if full_row[i] >= key:
                left = False
                break
        
        #If left is not visible, Test Right side
        if left == False:
            for i in range(full_row[col], len(full_row)):
                if full_row[i] >= key:
                    right = False
                    break
        return left and right
    
        


def is_col_visible(row, col, forest):
    
    #Extract given column from forest
    full_col = []
    for r in range(len(forest[col])):
        for c in range(len(forest[r])):
            if c == row:
                full_col.append(forest[r][c])

    #full_col = [i[col] for i in forest]
    key = forest[row][col]
    up, down = True, True

    if row == 0 or row == len(forest)-1 or col == 0 or col == len(forest[0])-1:
        return True
    else:
        for i in range(0,full_col[row]):
            if full_col[i] >= key:
                up = False
                break
        
        #If up is not visible, Test below key
        if up == False:
            for i in range(full_col[row], len(full_col)):
                if full_col[i] >= key:
                    down = False
                    break
        return up and down


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
