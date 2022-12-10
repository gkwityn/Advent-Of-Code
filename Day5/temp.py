# lines = ['    [D]    ',
#          '[N] [C]    ',
#          '[Z] [M] [P]']

 
lines =['                [B] [L]     [J]    ',
        '            [B] [Q] [R]     [D] [T]',
        '            [G] [H] [H] [M] [N] [F]',
        '        [J] [N] [D] [F] [J] [H] [B]',
        '    [Q] [F] [W] [S] [V] [N] [F] [N]',
        '[W] [N] [H] [M] [L] [B] [R] [T] [Q]',
        '[L] [T] [C] [R] [R] [J] [W] [Z] [L]',
        '[S] [J] [S] [T] [T] [M] [D] [B] [H]']


size = 9
stack = []

for i in range(0, size):
    stack.append([])s

for line in lines:
    j = 0
    
    for i in range(0, len(line), 4):
        if line[i+1] != ' ':
            stack[j].append(line[i+1])
        j+=1

#reverse
for list in stack:
    list.reverse()

return stack
