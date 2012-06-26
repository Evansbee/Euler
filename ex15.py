#grid 0,0 1,0 2,0
#     1,0 1,1 2,1
#     2,0 2,1 2,2

#Can be changed, grid is assumed square
GRID_SIZE = 2

START = (0,0)
END = (2,2)

tree = [START]

#takes a list of steps in, prints out a list of valid moves
def valid_moves(path):
   c = path[-1]
   valid = [(x,y) for x in [c[0]-1,c[0], c[0]+1] for y in [c[1]-1,c[1],c[1]+1] if (x==c[0] or y==c[1]) and x >= 0 and x <= GRID_SIZE and y >= 0 and y <=GRID_SIZE and path.count((x,y))==0]
   return valid


def unwind(path, ttree):
   path.append(ttree[0])
   if len(ttree) == 1:
      ttree.append(valid_moves(path))
   else:
      for x in ttree[1]:
         unwind(path, x)
      
unwind([],tree)

print tree
