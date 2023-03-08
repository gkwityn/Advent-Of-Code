def parse_input():
    with open("test.txt","r") as f:
        lines = f.readlines()


    return lines


if __name__ == "__main__":
    input_list = parse_input()
    print(input_list)