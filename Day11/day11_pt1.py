from Monkey import *

def parse_input():

    Monkeys = []

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
            my_Monkey = Monkey(monkey_number, items, opperation, divisible_by, if_true_throw_to, if_false_throw_to)
            Monkeys.append(my_Monkey)
        

    return Monkeys


def inspect_items(monkey):
    #TODO fix this.. breaks for loop with return
    for item in monkey.items:
        
        #update worrylevel
        print(f'\tMonkey inspects an item with a worry level of {item}')
        worry_level = None
        if monkey.opperation[1] == "old\n":
            monkey.opperation[1] = item
        
        
        if monkey.opperation[0] == '+':
            worry_level = item + int(monkey.opperation[1])
            print(f'\tWorry level is increased by {int(monkey.opperation[1])} to {worry_level}')
        elif monkey.opperation[0] == '*':
            worry_level = item * int(monkey.opperation[1])
            print(f'\tWorry level is multiplied by {int(monkey.opperation[1])} to {worry_level}')
        

        worry_level = worry_level // 3
        print(f'\tMonkey gets bored with item. Worry level is divided by 3 to {worry_level}')

        return worry_level, item


def test(current_monkey, worry_level):
    throw_to = None
    if worry_level % current_monkey.divisible_by == 0:
        print(f'\tCurrent worry level is divisible by {current_monkey.divisible_by}.')
        throw_to = current_monkey.if_true_throw_to
    else:
        print(f'\tCurrent worry level is not divisible by {current_monkey.divisible_by}.')
        throw_to = current_monkey.if_false_throw_to

    return throw_to

def Monkey_in_the_middle(Monkeys):
    
    #Run for 20 Rounds
    for round in range(1,2):
        print(f'Round: {round} Start:\n')
        
        #For each round go one Monkey at a time.
        for monkey in Monkeys:
            print(f'monkey_number: {monkey.monkey_number}')
            
            updated_worry, item = inspect_items(monkey)
            throw_to, item = test(monkey, updated_worry)
            
            Monkeys[throw_to].append(item)
            
            #Clear current monkey item list after inpecting all of the items
            monkey.items = None
    
        print("\n****************************")


if __name__ == "__main__":
    Monkeys = parse_input()
    
    #for obj in Monkeys:
        #print(obj.__str__())

    Monkey_in_the_middle(Monkeys)

    
    