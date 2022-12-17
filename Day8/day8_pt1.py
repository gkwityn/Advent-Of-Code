def parse_input():
    path = 'test.txt'
    file = open(path, 'r', encoding='UTF-8')
    lines = file.readlines()
    
    forest = []
    for line in lines:
        trees = list(map( int, line.strip('\n')))
        forest.append(trees)
    
    return forest

def is_visible(n, line):
    visible = False
    
    return visible


def main():
    forest = parse_input()
    print(forest)
main()
