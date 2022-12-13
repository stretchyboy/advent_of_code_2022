# Day 5 : Challenge 2

def parseCrates(sCrates):
    aCrates = []
    aLines = sCrates.split("\n")
    for j in range(1, len(aLines[0]), 4):
        aCrates.append("")
        
    for i in range(len(aLines)-1):
        for j in range(1, len(aLines[i]), 4):
            if(aLines[i][j] != " "):
                aCrates[int(j/4)] = aLines[i][j] +aCrates[int(j/4)]
    print("aCrates", aCrates)
    return aCrates

    

assert parseCrates('''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 ''') == ["ZN","MCD","P"]

assert parseCrates('''    [D]    
[N] [C]    
[Z] [M]   
 1   2   3 ''') == ["ZN","MCD",""]


assert parseCrates('''        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3 ''') == ["C","M","PDNZ"]


class Stacks():
    aCrates = []
    def __init__(self, sCrates) -> None:
        self.aCrates = parseCrates(sCrates)
    
    def getMessage(self):
        aMsg = [s[-1] if len(s) else " " for s in self.aCrates]
        msg = "".join(aMsg)
        print("msg", msg)
        return msg

    def _moveCrate(self, fromStack, toStack):
        fromCrate = self.aCrates[fromStack-1][-1]
        self.aCrates[fromStack-1] = self.aCrates[fromStack-1][:-1]
        self.aCrates[toStack-1] = self.aCrates[toStack-1] +fromCrate
        
    def _moveCrates(self,num, fromStack, toStack):
        print("_moveCrates", num, fromStack, toStack)
        
        fromCrates = self.aCrates[fromStack-1][(-1*num):]
        print("fromCrates", fromCrates)
        self.aCrates[fromStack-1] = self.aCrates[fromStack-1][:(-1*num)]
        self.aCrates[toStack-1] = self.aCrates[toStack-1] +fromCrates
        
    def moveCrates(self, sLine):
        aLine = sLine.split(" ")
        self._moveCrates(int(aLine[1]), int(aLine[3]),int(aLine[5]))

def getMessage(sCrates):
    stack = Stacks(sCrates)
    return stack.getMessage()

assert getMessage('''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 ''') == "NDP"

assert getMessage('''    [D]    
[N] [C]    
[Z] [M]   
 1   2   3 ''') == "ND "


assert getMessage('''        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3 ''') == "CMZ"

crates1 = Stacks('''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 ''')
crates1._moveCrates(1,2,1)
print(crates1.aCrates)
assert crates1.aCrates == ["ZND","MC","P"]

crates1._moveCrates(3,1,3)
print(crates1.aCrates)
assert crates1.aCrates == ["","MC","PZND"]


def doMoves(text):
    sCrates, sMoves = text.split("\n\n")
    stack = Stacks(sCrates)
    for sMove in sMoves.split("\n"):
        stack.moveCrates(sMove) 
    return stack.getMessage()


with open("Day 5/test.txt","r") as file:
    assert doMoves(file.read()) == "MCD"

with open("Day 5/input.txt","r") as file:
    print(doMoves(file.read()))

