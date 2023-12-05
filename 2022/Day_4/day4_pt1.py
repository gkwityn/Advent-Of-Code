def read_data():
    #path = './test.txt'
    path = 'data.txt'
    file = open(path, 'r', encoding='UTF-8')
    lines = file.readlines()
    return lines

    
def is_subset(A, B):

    if A.issubset(B):
        return True
    elif B.issubset(A):
        return True
    else:

        return False

def build_list(section):
    my_list = []
    str_list = section.strip().split('-')
    int_list = list(map(int, str_list))
    
    start = int_list[0]
    end = int_list[1] + 1
    for i in range(start, end):
        my_list.append(i)
    return my_list


def main():
    lines = read_data()
    total = 0

    for line in lines:
        sections = line.strip().split(sep=',')
        print(f'A: {sections[0]}, B:{sections[1]}')
    
        A = build_list(sections[0])
        B = build_list(sections[1])

        if is_subset(set(A),set(B)):
            total += 1        

    print(f'Total: {total}')

main()
