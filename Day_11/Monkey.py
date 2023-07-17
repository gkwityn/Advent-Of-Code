class Monkey():
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
