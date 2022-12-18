# Day 9 : Challenge 1

class Knot():
    x = 0
    y = 0
    def __init__(self, pos=(0,0)):
        self.x = pos[0]
        self.y = pos[1]
        

    def __repr__(self) -> str:
        return str((self.x,self.y))    
    
class Board():
    lines = []
    tailTrail = []
    rope = []
    head_x = 0
    head_y = 0
    def __init__(self, lines, startPos=(0,0)) -> None:
        self.startPos = startPos
        self.reset()
        self.lines = [(dir, int(dist)) for (dir,dist) in [line.split(" ") for line in lines]]
        print(self.lines)
        
    
    def reset(self):
        print("reset", self.startPos)
        self.rope = [Knot(self.startPos) for i in range(10)]
        print("self.rope", self.rope)
        self.tailTrail = [Knot(self.startPos)]
        
    def _moveHead(self, dir):
        if dir == "U":
            self.rope[0].y += 1
        if dir == "D":
            self.rope[0].y -= 1
        if dir == "R":
            self.rope[0].x += 1
        if dir == "L":
            self.rope[0].x -= 1
        
        self.follow()
        print("_moveHead", self.rope)
    
    def isTouching(self, i=1):
        #print("isTouching",i, self.rope[i-1].x,  self.rope[i].x, self.rope[i-1].x - self.rope[i].x)
        if abs(self.rope[i-1].x - self.rope[i].x) > 1:
            return False
        if abs(self.rope[i-1].y - self.rope[i].y) > 1:
            return False
        return True
    
    def follow(self):
        for i in range (1,10):
            #print("follow", i)
            self._follow(i)
    
    def _follow(self, i):
        if self.isTouching(i):
            return
        
        #print("Not Touching", i , self.rope[i])
        
        diff_x = self.rope[i-1].x - self.rope[i].x
        diff_y = self.rope[i-1].y - self.rope[i].y
        
        amp_x = abs(diff_x)
        amp_y = abs(diff_y)
        if amp_x != 0:
            self.rope[i].x += int(diff_x / amp_x)
        if amp_y != 0:
            self.rope[i].y += int(diff_y / amp_y)
        
        #print("_follow", i, self.rope[i])
        if(i == 9):
            self.tailTrail.append(str(self.rope[i]))
        
    def moveHead(self, dir, num):
        for i in range(num):
            self._moveHead(dir)   
        
    def part2(self):
        self.reset()
        for dir, dist in self.lines:
            self.moveHead(dir, dist)   
        out = len(list(set(self.tailTrail)))
        print("out", out)
        return out

        
with open("Day 9/test.txt","r") as file:
    board = Board(file.readlines())
    assert board.part2() == 1
 
newKnot = Knot((11,5))
assert newKnot.x == 11
assert newKnot.y == 5


with open("Day 9/test2.txt","r") as file:
    board3 = Board(file.readlines(),(11,5))
    assert board3.startPos == (11,5)
    #assert board3.rope[0] == Knot((11,5))
    assert board3.part2() == 36
    
with open("Day 9/input.txt","r") as file2:
    board2 = Board(file2.readlines())
    print(board2.part2())

