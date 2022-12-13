# Day 8 : Challenge 1



## idea one
# build array of tuples 
#   key (coords)
#   The trees to that point from the outside 
#filter the list
#turn intoa set and count the set

## idea 2 iterate in from the edges
## add coords to list if still visibble (and set new max)
#turn intoa set and count the set

LEFT    = 0
TOP     = 1
RIGHT   = 2
BOTTOM  = 3

class TreeMap():
    
    def __init__(self, aLines) -> None:
        self.aLines = list(map(lambda x: x.strip(), aLines))
        #print(self.aLines)
        self.height = len(self.aLines)
        self.width  = len(self.aLines[0])
        self.aDirections = [LEFT, TOP, RIGHT, BOTTOM]
        self.aMaxes = [0,0,0,0]
        self.aPosition = [0,0,0,0]
        #print(self)
    
    def countVisibleTrees(self):
        treeList = []
        self.aMaxes = [0,0,0,0]
        self.aPosition = [0,0,0,0]
    
        for top in range(self.height):
            
            self.aPosition[TOP]     = top
            self.aPosition[BOTTOM]  = self.height - (1 + top)
            for left in range(self.width):
                self.aPosition[LEFT]    = left
                self.aPosition[RIGHT]   = self.width - (1 + left)

                for yDirection in [TOP, BOTTOM]:
                    
                    treeValue = int(self.aLines[self.aPosition[yDirection]][self.aPosition[xDirection]])
                    if treeValue > self.aMaxes[yDirection]:
                        treeList.append((self.aPosition[yDirection],left))
                        self.aMaxes[yDirection] = treeValue
                
                    treeValue = int(self.aLines[top][])
                    if treeValue > self.aMaxes[xDirection]:
                        treeList.append((top, self.aPosition[xDirection]))
                        self.aMaxes[xDirection] = treeValue
                
                '''
                #print(self.aPosition) 
                for yDirection in [TOP, BOTTOM]:
                    treeValue = int(self.aLines[self.aPosition[yDirection]][left])
                    if treeValue > self.aMaxes[yDirection]:
                        treeList.append((self.aPosition[yDirection],left))
                        self.aMaxes[yDirection] = treeValue
                for xDirection in [LEFT, RIGHT]:
                    treeValue = int(self.aLines[top][self.aPosition[xDirection]])
                    if treeValue > self.aMaxes[xDirection]:
                        treeList.append((top, self.aPosition[xDirection]))
                        self.aMaxes[xDirection] = treeValue
                    #print(xDirection, self.aLines[top][self.aPosition[xDirection]])
                '''
        
        print("treeList",treeList)
        print("treeList",set(treeList))
        print(len(set(treeList)))
                        
        return len(set(treeList))
        
with open("Day 8/test.txt","r") as file:
    trees = TreeMap(file.readlines())
    assert trees.countVisibleTrees() == 21
 
with open("Day 8/input.txt","r") as file2:
    trees2 = TreeMap(file2.readlines())
    print(trees2.countVisibleTrees())

