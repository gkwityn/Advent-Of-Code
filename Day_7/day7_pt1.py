from collections import defaultdict

def scan(lines):
   limit = 100000
   path_list = []
   dir_sizes = defaultdict(int)

   for line in lines:
       
      line_parse = line.strip('\n').split(' ')
      
      #check for $ cmds
      if line_parse[0] == '$' and line_parse[1] == 'cd':
         #Root
         if line_parse[2] == '/':
            path_list = ['/']
         #Prev Dir
         elif line_parse[2] == '..':
            path_list.pop()  
         #Change Dir.  Add to pathlist
         else:
            path_list.append(line_parse[2])

      elif line_parse[0] == '$' and line_parse[1] == 'ls':
         pass

      # Check if its a file. 
      # Exclude dir
      else:
         if line_parse[0] != 'dir':
            size = int(line_parse[0])
            for i in range(0, len(path_list)):
                  dir_sizes['/'.join(path_list[:i+1])] += size
         
            

   return dir_sizes
   
def calc_and_print(dir_sizes):

   total = 0
   print(dir_sizes)

   for size in dir_sizes.values():
      if size <= 100000:
         total += size

   print(f'Total:{total}')

def parse_input():
   #path = 'test.txt'
   path = 'data.txt'

   file = open(path, 'r', encoding='UTF-8')
   lines = file.readlines()
   return lines


def main():
   lines = parse_input()
   dir_sizes = scan(lines)
   calc_and_print(dir_sizes)

main()

#Not
#Total:1160629
#Total:258641

#ans
#Total:1306611
