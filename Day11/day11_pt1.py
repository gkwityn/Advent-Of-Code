class monkey():

        
    
    def __init__(self):
        self.monkey_number = None
        self.items = [] #list of starting items
        self.opperation = []  #[0] = operator, [1] = opperand
        self.divisible_by = None 
        self.if_true_throw_to = None
        self.if_false_throw_to = None
     
        

        



#TODO FIX line parse
def parse_input():

    monkeys = []

    with open("test.txt","r") as f:
        lines = f.readlines()

    for line_num, line in enumerate(lines, 1):
        
        if line == '\n':
            print(f'{line_num}, break\n', end="")
        else:
            print(f'{line_num}, {line}', end="")

        

        # split_line = line.strip().split(" ")
        # if split_line[0] == "Monkey":
        #     monkey_number = int(split_line[1].strip(":"))
        # elif split_line[0] == "Starting":
            
        #     items = split_line[2:]
        # elif split_line[0] == "Operation":
            
        #     opperation = split_line[1:]
        # elif split_line[0] == "Test":
        #     divisible_by = int(split_line[3])
        # elif split_line[1] == "true":
        #     if_true_throw_to = int(split_line[5])
        # elif split_line[1] == "false":
        #     if_false_throw_to = int(split_line[5])
        
        # monkey(monkey_number, items, opperation, divisible_by, if_true_throw_to, if_false_throw_to)
        # monkeys.append(monkey)
            
    #return monkeys


if __name__ == "__main__":
    parse_input()
    #input_list = parse_input()
    