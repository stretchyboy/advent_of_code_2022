# Day 8 : Challenge 1



## idea one
# build array of tuples 
#   key (coords)
#   The trees to that point from the outside 
#filter the list
#turn into a set and count the set

## idea 2 iterate in from the edges
## add coords to list if still visible (and set new max)
#turn into a set and count the set

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
        self.aMaxes = [[-1]*self.width,[-1]*self.height,[-1]*self.width,[-1]*self.height]
        
        for top in range(self.height):
            bottom  = self.height - (1 + top)
            for left in range(self.width):
                right   = self.width - (1 + left)
                treeValue = int(self.aLines[top][left])
                if treeValue > self.aMaxes[TOP][left]:
                    treeList.append((top,left))
                    self.aMaxes[TOP][left] = treeValue
                
                if treeValue > self.aMaxes[LEFT][top]:
                    treeList.append((top,left))
                    self.aMaxes[LEFT][top] = treeValue
                
                treeValue = int(self.aLines[bottom][right])
                if treeValue > self.aMaxes[BOTTOM][right]:
                    treeList.append((bottom,right))
                    self.aMaxes[BOTTOM][right] = treeValue
                
                if treeValue > self.aMaxes[RIGHT][bottom]:
                    treeList.append((bottom,right))
                    self.aMaxes[RIGHT][bottom] = treeValue
        '''        
        print("treeList",treeList)
        print("treeList",set(treeList))
        print(len(set(treeList)))
        '''
                     
        return len(set(treeList))
    
    def getTree(self, y, x):
        if y<0 or x<0:
            return -1
        try:
            return self.aLines[y][x]
        except:
            print("getTree failed",y,x)
            return -1 
        
    def lookSomeWhere(self, y, x, dir):
        start = self.getTree(y, x)
        print("y=",y, "x=",x, " start=",start, " dir=", dir)
        found = 0
        count = 0
        while (True):
            if(dir == TOP):
                y -= 1
            if(dir == BOTTOM):
                y += 1
            if(dir == LEFT):
                x -= 1
            if(dir == RIGHT):
                x += 1
            next = self.getTree(y,x)
            print("next", next,y,x)
            if (next == -1):
                break
            count += 1
            if (next >= start):
                break
        print("count=", count)
        
        return count 
    
    
    def scenicScore(self, y, x):
        score = 1
        for dir in self.aDirections:
            score *= self.lookSomeWhere(y, x, dir)
        
        print("x=",x," y=",y, " score=", score)
        return score
    
    def maxScenicScore(self):
        maxScore = 0
        for x in range(self.width):
            for y in range(self.height):
                newScore = self.scenicScore(y,x)
                if newScore > maxScore:
                    maxScore = newScore
        return maxScore
            
with open("Day 8/test.txt","r") as file:
    trees = TreeMap(file.readlines())
    assert trees.countVisibleTrees() == 21
    assert trees.scenicScore(0,2) == 0
    assert trees.scenicScore(1,4) == 0
    assert trees.scenicScore(1,2) == 4
    assert trees.scenicScore(3,2) == 8
    assert trees.maxScenicScore() == 8
 
 
with open("Day 8/input.txt","r") as file2:
    trees2 = TreeMap(file2.readlines())
    print("countVisibleTrees", trees2.countVisibleTrees())
    print("maxScenicScore", trees2.maxScenicScore())
