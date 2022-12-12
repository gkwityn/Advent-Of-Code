#Test input
#mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 7
# bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
# nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11


def read_data():
    #path = 'test.txt'
    path = 'data.txt'
    file = open(path, 'r', encoding='UTF-8')
    lines = file.readlines()
    return lines

def find_marker(line):
    for i in range(0, len(line)-4):
        group = line[i:i+4]
        if len(set(group)) == len(group):
            return i + 4
    return -1

def main():
    data_list = read_data()
    
    #Print All Input Lines
    for line in data_list:
        #print(line)
        marker = find_marker(line)
        print(f'End of Marker Index: {marker}')    
    
main()