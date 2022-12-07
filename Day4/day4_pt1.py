def read_data():
    path = './test.txt'
    file = open(path, 'r', encoding='UTF-8')
    lines = file.readlines()
    return lines
def a_subset_b(a, b):
    return a.issubset(b)

def main():
    lines = read_data()

    for line in lines:
        sections = line.strip().split(sep=',')
        print(f'A: {sections[0]}, B:{sections[1]}')
        A = set(sections[0])
        B = set(sections[1])

        if a_subset_b(A,B):
            pass
main()
