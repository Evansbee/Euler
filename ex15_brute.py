#grid 0,0 1,0 2,0
#     1,0 1,1 2,1
#     2,0 2,1 2,2
from math import sqrt

#Can be changed, grid is assumed square
GRID_SIZE = 20

START = (0,0)
END = (20,20)
paths = 0
basetree = [START]

#returns a tree, expects a tuple for the node to start with, and the path thus far
# tree.append(pop_tree((ROOT),[]))
def dist(p1, p2):
   #2 tuples
   x = p1[0] - p2[0]
   y = p1[1] - p2[1]
   dist = x**2 + y**2
   dist = sqrt(dist)
   return dist


def make_tree(path):
   global paths
   root = path[-1]
   print "Building tree from %r" % (root,)
   tree = []
   #1 tupple added in
   tree.append(root)           
   next_moves = valid_moves(path)
   
   if root == END:
      paths += 1
      return tree

   if len(next_moves) == 0:
      return tree
                                 
   next_tree = []
                                          
   for move in next_moves:
      new_path = list(path)
      new_path.append(move)
      tree.append(make_tree(new_path))
                                                              
   return tree
   #need to get valid positions for 

#given the path, we're returning a list of moves
def valid_moves(path):
   c = path[-1]
   return [(x,y) for x in [c[0], c[0]+1] for y in [c[1],c[1]+1] if (x==c[0] or y==c[1]) and x >= 0 and x <= GRID_SIZE and y >= 0 and y <=GRID_SIZE and path.count((x,y))==0]

basetree= make_tree([START])

#takes a list of steps in, prints out a list of valid moves

print basetree
print paths
