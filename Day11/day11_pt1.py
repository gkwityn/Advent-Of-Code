class monkey():
    def __init__(self, monkey_number, items, opperation, divisible_by, if_true_throw_to, if_false_throw_to):
        self.monkey_number = monkey_number
        self.items = items #list of starting items
        self.opperation = opperation #[0] = operator, [1] = opperand
        self.divisible_by = divisible_by 
        self.if_true_throw_to = if_true_throw_to
        self.if_false_throw_to = if_false_throw_to

#TODO Fix obj parsings
def parse_input():

    monkeys = []

    with open("test.txt","r") as f:
        lines = f.readlines()

    for line_num, line in enumerate(lines, 0):
        monkey_number = None
        items = None #list of starting items
        opperation = None #[0] = operator, [1] = opperand
        divisible_by = None 
        if_true_throw_to = None
        if_false_throw_to = None

        if line_num == 0 or (line_num % 7) == 0:
            monkey_number = line.split()[1]
            #print(f'monkey_number: {monkey_number}')

        elif (line_num == 1 ) or (line_num % 7) == 1:
            items_list = [x.strip(',') for x in line.split()[2:]]
            items = list(map(int, items_list))
            #print(f'items: {items}', end='\n')
        
        elif (line_num == 2 ) or (line_num % 7) == 2:
            opperator = line.split(' ')[6]
            opperand = line.split(' ')[7]
            opperation = [opperator, opperand]
            #print(f'opperator: {opperator}, opperand: {opperand}', end='')
        
        elif (line_num == 3 ) or (line_num % 7) == 3:
            divisible_by = int(line.split()[3])
            #print(f'Divisible_by: {divisible_by}', end='\n')

        elif (line_num == 4 ) or (line_num % 7) == 4:
            if_true_throw_to = int(line.split()[5])
            #print(f'if_true_throw_to: {if_true_throw_to}')

        elif (line_num == 5 ) or (line_num % 7) == 5:
            if_false_throw_to = int(line.split()[5])
            #print(f'if_false_throw_to: {if_false_throw_to}')

        elif line == '\n':
            pass
            #print()
        monkey(monkey_number, items, opperation, divisible_by, if_true_throw_to, if_false_throw_to)
        monkeys.append(monkey)
    return monkeys


if __name__ == "__main__":
    monkeys = parse_input()
    print((monkeys))
    