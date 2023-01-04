def parse_input():
    path = 'test.txt'
    #path = 'data.txt'
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

def get_col(row, col, forest):
    full_col = []
    for r in range(len(forest[col])):
        for c in range(len(forest[r])):
            if c == row:
                full_col.append(forest[r][c])
    return full_col

def is_row_visible(row, col, forest):

    full_row = forest[row]
    key = forest[row][col]

    left, right = False, False
    
    #Check if item is on the perimiter
    if is_perimeter(row, col, forest):
        return True
    else:
        for i in range(0, len(full_row)):
            if i < col:
                if full_row[i] < key:
                    left = True
                else:
                    left = False
                    i = col+1
            if i == col:
                continue
            if i > col:
                if full_row[i] < key:
                    right = True
                else:
                    right = False
                    break
    return left or right


def is_col_visible(row, col, forest):
    
    #Extract given column from forest
    full_col = extract_col(row, col, forest)

    key = forest[row][col]
    up, down = False, False

    if is_perimeter(row, col, forest):
        return True
    else:
        for i in range(0, len(full_col)):
            if i < row:
                if full_col[i] < key:
                    up = True
                else:
                    up = False
                    i = row+1
            if i == row:
                continue
            if i > row:
                if full_col[i] < key:
                    down = True  
                else:
                    down = False 
                    break
    return up or down

def is_perimeter(row, col, forest):
    #First Row
    if row == 0 and col >= 0:
        return True
    #Last Row
    elif row == len(forest)-1 and col >= 0:
        return True
    #First Col
    elif row >= 0 and col ==0:
        return True
    #Last Col
    elif row >= 0 and col == len(forest[0])-1:
        return True
    
    return False
    

        

def main():
    forest = parse_input()
    #print(forest)

    count = 0
    printForest(forest)

    print('-----------------------')
    
    for i in range( len(forest)):
        for j in range( len(forest[i])):
            #if is_row_visible(i, j, forest):
            #if is_col_visible(i, j, forest):
            if is_row_visible(i, j, forest) or is_col_visible(i, j, forest):
                print('T', end='')
                count+=1
            else:
                print(' ', end='')
        print()

    print(f'Count: {count}')
    
main()
