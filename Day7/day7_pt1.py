# $ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k

# - / (dir)
#   - a (dir)
#     - e (dir)
#       - i (file, size=584)

#     - f (file, size=29116)
#     - g (file, size=2557)
#     - h.lst (file, size=62596)

#   - b.txt (file, size=14848514)
#   - c.dat (file, size=8504156)

#   - d (dir)
#     - j (file, size=4060174)
#     - d.log (file, size=8033020)
#     - d.ext (file, size=5626152)
#     - k (file, size=7214296)


def scan(lines):

   for line in lines:
      limit = 100000
      path_list = []
      line_parse = line.strip().split(' ')
      dir_sizes = {}
      

      #check for $ cmds
      if line_parse[0] == '$':
         #check for cd
         if line_parse[1] == 'cd':

            #Root
            if line_parse[2] == '/':
               path_list.append(line_parse[2])

            #Prev Dir
            elif line_parse[2] == '..':
               path_list.pop()

            #Change Dir.  Add to pathlist
            else:
               path_list.append(line_parse[2])

         #check for ls. Can ignore for now.
         elif line_parse[1] == 'ls':
            continue

      #Check if its a file
      elif line_parse[0] != 'dir':
         size = int(line_parse[0])

         for i in range(len(path_list)):
            if i <= 1:
               dir_sizes[path_list[i]] += size
            else:
               parent = path_list[i-1]
               current = path_list[i]
               dir_key = f'{parent}/{current}'
               dir_sizes[dir_key] += size

   print(dir_sizes)
      #Check for dir cmd
      # elif line_parse[0] == 'dir':
      #    pass



def parse_input():
   path = 'test.txt'
   file = open(path, 'r', encoding='UTF-8')
   lines = file.readlines()
   return lines


def main():
   lines = parse_input()
   scan(lines)

main()
