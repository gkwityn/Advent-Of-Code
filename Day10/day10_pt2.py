class CPU():
    def __init__(self, clock, registerX):
        self.clock = clock
        self.registerX = registerX
        self.signal_list = []

    def tick(self):
        
        self.render()
        self.clock += 1
        
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

    def render(self):

        #Begin new row to render and check if clk is at sprite pos
        if self.clock % 40 == 0 :
            print()
            if (self.clock%40 == self.registerX - 1 or
                self.clock%40 == self.registerX or 
                self.clock%40 == self.registerX + 1):
                print("#", end="")
            else:
                print(".", end="")
        #check if clk is at sprite pos
        elif (self.clock%40 == self.registerX - 1 or
            self.clock%40 == self.registerX or 
            self.clock%40 == self.registerX + 1):
            print("#", end="")
        #Otherwise clk not at sprite pos
        else:
            print(".", end="")
        

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
    
    #initialize  values
    myCPU = CPU(clock = 0, registerX = 1)
    
    #Move through instruction list and pass the opperations to CPU obj to process
    for instr in instructions:
        myCPU.opp(instr[0], instr[1])
    print("\n")
    
    

