with open("test_large.txt", "r") as f:
    lines = f.readlines()
    
    instructions=[]
    for line in lines:
         operation = line.strip().split()[0]
         
         if len(line.strip().split()) == 2:
            cycle = int(line.strip().split()[1])
         else:
             cycle = 1
         instructions.append([operation, cycle])


#initialize  values
registerX = 1
global clock
clock = 1 
signal = []

def tick():
    clock += 1

    if clock == 20:
        signal.append(clock*registerX)
    elif clock%40 == 0:
        signal.append(clock*registerX)
    else:
        print(f'Cycle: {clock}, X: {registerX}')








for instr in instructions:
    if instr[0] == "addx":
     for cycle in range(1,3):
         tick()
         if cycle == 2:
          registerX += instr[1]
         
             
     else:
        tick()
    
    
    

print(f'Signal Value: {clock*registerX}')

print(signal)

