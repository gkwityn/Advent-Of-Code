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


class Node:
   def __init__(self, name):
      self.parent = None
      self.children = []
      
      self.name = name
      self.type = None
      self.size = 0
   
   def set_size(self, size):
      if self.type == 'file':
         self.size = size
      else:
         raise Exception('Type: "file", only allowed to set_size.') 

   def set_type(self, type):
      if type == 'file' or type == 'dir':
         self.type = type
      else:
         raise Exception(f'Inproper Node type given: {type}.')
   
   def add_child(self, child):
      child.parent = self
      self.childern.append(child)

def build_tree(lines):
   for line in lines:
      line_parse = line.splice().split(' ')

      #check for $
      if line_parse[0] == '$':
         #check for cd
         if line_parse[1] == 'cd'
            root = Node('root')
            root.set_type('dir')
         elif line_parse[2] == ''




def parse_input():
   path = 'test.txt'
   file = open(path, 'r', encoding= 'UTC-8')
   lines = file.readlines()
   return lines


def main():
   lines = parse_input()
   build_tree(lines)

main()
