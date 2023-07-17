class CPU():
    def __init__(self, clock, registerX):
        self.clock = clock
        self.registerX = registerX
        self.signal_list = []

    def tick(self):

        self.clock += 1
        self.__str__()

        if self.clock == 20 or (self.clock + 20)% 40  == 0:
            self.signal_list.append(self.clock*self.registerX)


    def opp(self, op, val ):
        if op == "addx":
            self.tick()
            self.tick()
            self.addX(val)
        elif op == "noop":  
            self.tick()
            

    def addX(self, num):
        self.registerX += num 
    
    
    def __str__(self):
        print(f"Clock: {self.clock}, RegX: {self.registerX}")
        return

    


def parse_input():
    with open("data.txt", "r") as f:
        lines = f.readlines()
        
        instructions=[]
        for line in lines:
            operation = line.strip().split()[0]
            
            if len(line.strip().split()) == 2:
                value = int(line.strip().split()[1])
            else:
                value = None
            
            instructions.append([operation, value])
    return instructions



if __name__ == "__main__":

    instructions = parse_input()
    print(instructions)

    #initialize  values
    myCPU = CPU(clock = 0, registerX = 1)

    myCPU.__str__()
    for instr in instructions:
        myCPU.opp(instr[0], instr[1])
    print("\n")
    print(f"Signal_list: {myCPU.signal_list}")
    print(f"Signal Sum: {sum(myCPU.signal_list)}")
    

