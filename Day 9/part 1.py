# Day 9 : Challenge 1


class Board():
    lines = []
    tailTrail = []
    head_x = 0
    head_y = 0
    def __init__(self, lines) -> None:
        self.lines = [(dir, int(dist)) for (dir,dist) in [line.split(" ") for line in lines]]
        print(self.lines)
        pass
    
    def reset(self):
        self.tailTrail = [(0,0)]
        self.head_x = 0
        self.head_y = 0
        self.tail_x = 0
        self.tail_y = 0
    
    def _moveHead(self, dir):
        if dir == "U":
            self.head_y += 1
        if dir == "D":
            self.head_y -= 1
        if dir == "R":
            self.head_x += 1
        if dir == "L":
            self.head_x -= 1
            
        self.follow()
    
    def isTouching(self):
        if abs(self.head_x - self.tail_x) > 1:
            return False
        if abs(self.head_y - self.tail_y) > 1:
            return False
        return True
    
    def follow(self):
        if self.isTouching():
            return
        
        diff_x = self.head_x - self.tail_x
        diff_y = self.head_y - self.tail_y
        
        amp_x = abs(diff_x)
        amp_y = abs(diff_y)
        if amp_x != 0:
            self.tail_x += (diff_x / amp_x)
        if amp_y != 0:
            self.tail_y += (diff_y / amp_y)
        
        self.tailTrail.append((self.tail_x, self.tail_y))
        
    def moveHead(self, dir, num):
        for i in range(num):
            self._moveHead(dir)   
        
    def part1(self):
        self.reset()
        for dir, dist in self.lines:
            self.moveHead(dir, dist)   
        out = len(list(set(self.tailTrail)))
        print("out", out)
        return out

        
with open("Day 9/test.txt","r") as file:
    board = Board(file.readlines())
    assert board.part1() == 13
 
with open("Day 9/input.txt","r") as file2:
    board2 = Board(file2.readlines())
    print(board2.part1())

