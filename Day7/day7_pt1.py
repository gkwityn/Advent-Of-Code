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
   def __init__(self, type):
      self.left = None
      self.right = None
      self.type = type
      self.size = None
   def PrintTree(self):
      print(self.data)

root = Node(10)
root.PrintTree()


from anytree import Node, RenderTree


root = Node("root")
marc = Node("Marc", parent=udo)
lian = Node("Lian", parent=marc)
dan = Node("Dan", parent=udo)
jet = Node("Jet", parent=dan)
jan = Node("Jan", parent=dan)
joe = Node("Joe", parent=dan)

for pre, fill, node in RenderTree(udo):
    print("%s%s" % (pre, node.name))