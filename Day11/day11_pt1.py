class monkey():

    def __init__(self):
        self.monkey_number = None
        self.items = [] #list of starting items
        self.opperation = []  #[0] = operator, [1] = opperand
        self.divisible_by = None 
        self.if_true_throw_to = None
        self.if_false_throw_to = None
     
    def set_monkey_number(self, monkey_number):
        self.monkey_number = monkey_number

    def set_items(self, items):
        self.items = items

    def 

        



#TODO FIX line parse
def parse_input():

    monkeys = []

    with open("test.txt","r") as f:
        lines = f.readlines()

    for line_num, line in enumerate(lines, 0):
        
              
        if line_num == 0 or (line_num % 7) == 0:
            #print(f'{line_num}, {line}', end="")
            monkey_number = line.split()[1]
            print(f'monkey_number: {monkey_number}')

        elif (line_num == 1 ) or (line_num % 7) == 1:
            items_list = [x.strip(',') for x in line.split()[2:]]
            items = list(map(int, items_list))
            print(f'items: {items}', end='\n')
        
        elif (line_num == 2 ) or (line_num % 7) == 2:
              opperator = line.split(' ')[6]
              opperand = line.split(' ')[7]
              opperation = [opperator, opperand]
              print(f'opperator: {opperator}, opperand: {opperand}', end='')
        
        elif (line_num == 3 ) or (line_num % 7) == 3:
            divisible_by = int(line.split()[3])
            print(f'Divisible_by: {divisible_by}', end='\n')

        elif (line_num == 4 ) or (line_num % 7) == 4:
            if_true_throw_to = int(line.split()[5])
            print(f'if_true_throw_to: {if_true_throw_to}')

        elif (line_num == 5 ) or (line_num % 7) == 5:
            if_false_throw_to = int(line.split()[5])
            print(f'if_false_throw_to: {if_false_throw_to}')

        elif line == '\n':
            monkey(monkey_number, items, opperation, divisible_by, if_true_throw_to, if_false_throw_to)
            print()
        
        #else:
        #    print(f'{line_num}, {line}', end="")

        

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
    