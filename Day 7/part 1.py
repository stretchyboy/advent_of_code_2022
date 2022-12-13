# Day 7 : Challenge 1


class Listing():
    aCurrent = []
    dSizes = {"/" : 0}
    def __init__(self, aLines) -> None:
        self.aCurrent = []
        self.aCurrentKeys = []
        self.dSizes = {"/" : 0}
        for sLine in aLines :
            aLine = sLine.strip("\n").split(" ")
            if aLine[0] == "$":
                if aLine[1] == "cd":
                    self.cd(aLine[2])
                if aLine[1] == "ls":
                    pass
            elif aLine[0] == "dir":
                self.dir(aLine[1])
            else:
                self.add(int(aLine[0]))            
    
    def key(self, dir=None):
        aCurr = []+self.aCurrent 
        if (dir):
            aCurr.append(dir)
        
        k = "-".join(aCurr)
        print("key", k)
        return k
    
    def dir(self, dir):
        self.dSizes[self.key(dir)] = 0
        
    def cd(self, dir):
        if dir == "..":
            self.aCurrent.pop()
            self.aCurrentKeys.pop()
        else :
            self.aCurrent.append(dir)
            self.aCurrentKeys.append(self.key())
        print("cd", dir, self.aCurrent, self.aCurrentKeys)
    
    def add(self, size):
        print("Adding", size , "to",self.key())
        for key in self.aCurrentKeys:
            self.dSizes[key] += size
    
    def atMost100000(self):
        atMost = {key:size for key, size in self.dSizes.items() if size <= 100000}
        print(sum(atMost.values()), atMost)
        return sum(atMost.values())
        
            

with open("Day 7/test.txt","r") as file:
    listing = Listing(file.readlines())
    assert listing.atMost100000() == 95437

 
with open("Day 7/input.txt","r") as file2:
    listing2 = Listing(file2.readlines())
    print(listing2.atMost100000())

