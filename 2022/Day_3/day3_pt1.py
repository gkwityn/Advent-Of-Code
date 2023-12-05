

def read_data():
    #path = './test.txt'
    path = './data.txt' 
    file = open(path, 'r', encoding='UTF-8')
    lines = file.readlines()

    return lines

def find_common(a, b):
    return ''.join(set(a).intersection(b))

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

    for line in lines:
        half = int(len(line)/2)
   
        first = line[0:half]
        second = line[half:].strip()
        common = find_common(first, second)
        char_score = score(common)
        total += char_score
        print(f'input: {first} {second}\n\tCommon:{common}, Score:{char_score}')
        
    print(f'Total: {total}')


main()
