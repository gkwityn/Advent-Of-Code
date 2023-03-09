class monkey():
    def __init__(self, monkey_number, items, 
                 opperation, divisible_by, 
                 if_true_throw_to, if_false_throw_to):
        self.monkey_number = monkey_number
        self.items = items
        self.opperation = opperation
        self.divisible_by = divisible_by
        self.if_true_throw_to = if_true_throw_to
        self.if_false_throw_to = if_false_throw_to

        




def parse_input():
    with open("test.txt","r") as f:
        lines = f.readlines()

    for line in lines:
        split_line = line.split(" ")
        if split_line[0] == "Monkey":
            monkey_number = int(split_line[1])
        elif split_line[0] == "Operation":
            

    return lines


if __name__ == "__main__":
    input_list = parse_input()
    print(input_list)