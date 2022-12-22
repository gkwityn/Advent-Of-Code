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

def extract_col(row, col, forest):
    full_col = []
    for r in range(len(forest[col])):
        for c in range(len(forest[r])):
            if c == row:
                full_col.append(forest[r][c])
    return full_col

def is_row_visible(row, col, forest):

    full_row = forest[row]
    key = forest[row][col]
    
    #Check if item is on the perimiter
    if is_perimeter(row, col, forest):
        return True
    else:
        for i in range(0, len(full_row)):
            if i == col:
                continue
            else:
                if full_row[i] >= key:
                    return False


def is_col_visible(row, col, forest):
    
    #Extract given column from forest
    full_col = extract_col(row, col, forest)

    key = forest[row][col]

    if is_perimeter(row, col, forest):
        return True
    else:
        for i in range(0, len(full_col)):
            if i == row:
                continue
            else:
                if full_col[i] >= key:
                    return False    


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
            if is_row_visible(i, j, forest) and is_col_visible(i, j, forest):
                print('T', end='')
                count+=1
            else:
                print(' ', end='')
        print()

    print(f'Count: {count}')
    
main()
