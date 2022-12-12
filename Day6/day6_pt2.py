# --- Part Two ---
# Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also needs to look for messages.

# A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.

# Here are the first positions of start-of-message markers for all of the above examples:

# mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
# bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
# nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26
# How many characters need to be processed before the first start-of-message marker is detected?




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
    for i in range(0, len(line)-14):
        group = line[i:i+14]
        if len(set(group)) == len(group):
            return i + 14
    return -1

def main():
    data_list = read_data()
    
    #Print All Input Lines
    for line in data_list:
        #print(line)
        marker = find_marker(line)
        print(f'End of Marker Index: {marker}')    
    
main()