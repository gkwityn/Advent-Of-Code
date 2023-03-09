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

        



#TODO FIX line parse
def parse_input():

    monkeys = []

    with open("test.txt","r") as f:
        lines = f.readlines()

    for line in lines:

        split_line = line.strip().split(" ")
        if split_line[0] == "Monkey":
            monkey_number = int(split_line[1].strip(":"))
        elif split_line[0] == "Starting":
            items = []
        elif split_line[0] == "Operation":
            opperation = split_line[1:]
        elif split_line[0] == "Test":
            divisible_by = int(split_line[3])
        elif split_line[1] == "true":
            if_true_throw_to = int(split_line[5])
        elif split_line[1] == "false":
            if_false_throw_to = int(split_line[5])
        
        monkey(monkey_number, items, opperation, divisible_by, if_true_throw_to, if_false_throw_to)
        monkeys.append(monkey)
            
    return monkeys


if __name__ == "__main__":
    input_list = parse_input()
    print(input_list)