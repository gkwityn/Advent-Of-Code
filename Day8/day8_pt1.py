def parse_input():
    path = 'test.txt'
    file = open(path, 'r', encoding='UTF-8')
    lines = file.readlines()
    
    forest = []
    for line in lines:
        trees = list(map( int, line.strip('\n')))
        forest.append(trees)
    
    return forest

def count_visible(forest, row, col):
    key = forest[row][col]
    visible = False
    count = 0
    #Check row visibility 
    #To the right of n
    temp = 0
    for i in range(col, len(forest[row]) ):
        if forest[row][i] < key:
            temp += 1
        else:
            temp = 0
    count += temp
    
    #To the right of n
    temp = 0
    for i in range(row, 0, -1):
        if forest[i][col] < key:
            count += 1
        else:
            temp = 0
    count += temp

    #To the top of n
    temp = 0
    for i in range(row, len(forest[col])):
        if forest[i][col] < key:
            count += 1
        else:
            temp = 0
    count += temp

    return count
    #To the bottom on n

    
    return count


def main():
    forest = parse_input()
    print(forest)

    row_size = len(forest)
    
    total = 0
    for i in range(]):
        for j in forest:
            total += count_visible(forest, )

    print(f'Total: {total}')
main()
