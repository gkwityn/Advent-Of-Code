class monkey():
    def __init__(self, monkey_number, items, opperation, divisible_by, if_true_throw_to, if_false_throw_to):
        self.monkey_number = monkey_number
        self.items = items #list of starting items
        self.opperation = opperation #[0] = operator, [1] = opperand
        self.divisible_by = divisible_by 
        self.if_true_throw_to = if_true_throw_to
        self.if_false_throw_to = if_false_throw_to

    def __str__(self):
        print(f'monkey_number: {self.monkey_number}')
        print(f'items: {self.items}', end='\n')
        print(f'opperator: {self.opperation[0]}, opperand: {self.opperation[1]}', end='') #[0] = operator, [1] = opperand
        print(f'Divisible_by: {self.divisible_by}', end='\n') 
        print(f'if_true_throw_to: {self.if_true_throw_to}')
        print(f'if_false_throw_to: {self.if_false_throw_to}', end='\n')
        return ""
    


def parse_input():

    monkeys = []

    with open("test.txt","r") as f:
        lines = f.readlines()

    for line_num, line in enumerate(lines, 0):
        

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

        elif (line_num == 6 ) or (line_num % 7) == 6:
            my_monkey = monkey(monkey_number, items, opperation, divisible_by, if_true_throw_to, if_false_throw_to)
            monkeys.append(my_monkey)
        

    return monkeys

def monkey_in_the_middle(monkeys):
    #psuedocode:
    
    #start round
        #each monkey looks at each item they are holding one at a time
        #perform opperation on that item to get new worry level
        #divide new worry level by Divisible_by
            #check new worry level against each condition true/false
            #throw item to new monkey
        




if __name__ == "__main__":
    monkeys = parse_input()
    
    for obj in monkeys:
        print(obj.__str__())

    
    