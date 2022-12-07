

def read_data():
    #path = './test.txt'
    path = './data.txt' 
    file = open(path, 'r', encoding='UTF-8')
    lines = file.readlines()

    return lines

def find_common(group):
    common = set.intersection(*map(set,group))
    return set.pop(common)

def score(char):

    lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper =[]
    for el in lower:
        upper.append(el.upper())


    if char.islower():
        score = lower.index(char) + 1 
    elif  char.isupper():
        score = upper.index(char) + 27
    return score

def main():
    lines = read_data()

    total = 0
    group_list = []
    group_count = 0

    for line in lines:
        group_count += 1
        group_list.append(line.strip())

        if group_count % 3 == 0:
            common = find_common(group_list)
            for item in group_list:
                print(item)
            subtotal = score(common)
            total += subtotal
            print(f'Common: {common}, Score:{subtotal}')
            print("-------------")
            group_count = 0
            group_list = []

        
    print(f'Total: {total}')


main()
