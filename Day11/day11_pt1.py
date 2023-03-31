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
    
    for item, index in enumerate(monkey.items):
        
        #update worrylevel
        print(f'\tMonkey inspects an item with a worry level of {item}')
        worry_level = None
        if monkey.opperation[1] == "old\n":
            monkey.opperation[1] = item
        
        
        if monkey.opperation[0] == '+':
            worry_level = item + int(monkey.opperation[1])
            print(f'Worry level is increased by {monkey.opperation[1]} to {worry_level}')
        elif monkey.opperation[0] == '*':
            worry_level = item * int(monkey.opperation[1])
            print(f'Worry level is multiplied by {monkey.opperation[1]} to {worry_level}')
        
        removeListIndex = []
     
    #TODO Write the test function


    #If thrown remove thrown items from this monkeys item list
    for index in removeListIndex:
        monkey.items.pop(index)   


def Monkey_in_the_middle(Monkeys):
    
    #Run for 20 Rounds
    for round in range(1,21):
        print(f'Round: {round} Start:\n')
        
        #For each round go one Monkey at a time.
        for monkey in Monkeys:
            print(f'monkey_number: {monkey.monkey_number}')

            inspect_items(monkey)

        print("\n****************************")


if __name__ == "__main__":
    Monkeys = parse_input()
    
    for obj in Monkeys:
        print(obj.__str__())

    Monkey_in_the_middle(Monkeys)

    
    