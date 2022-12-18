# Day 10 : Challenge 1


class CPU():
    
    def __init__(self, lines) -> None:
        self.lines = [(item[0].strip("\n"), int(item[1]) if len(item)>1 else None) for item in [line.split(" ") for line in lines]]
        print(self.lines)
        self.reset()
    
    def run(self):
        for instruction, val in self.lines:
            self.execute(instruction, val)
        self.aX.append(self.X)
        
        
    def execute(self, name: str, V):
        do = f"do_{name}"
        if hasattr(self, do) and callable(func := getattr(self, do)):
            func(V)
    
    
    def reset(self):
        self.cycle = 0
        self.X = 1
        self.aX = []
        self.signalStrengths=[]
    
    def tick(self):
        self.aX.append(self.X)
        self.cycle += 1
        if (self.cycle - 20) % 40 == 0:
            print("signalStrengths", self.cycle, self.X, self.cycle * self.X)
            self.signalStrengths.append(self.cycle * self.X)    
            
    def do_noop(self, V):
        self.tick()
    
    def do_addx(self, V):
        self.tick()
        self.tick()
        self.X += V
         
    def part1(self):
        out = sum(self.signalStrengths)
        print("out", out)
        return out

        
with open("Day 10/test.txt","r") as file:
    cpu = CPU(file.readlines())
    cpu.run()
    #print("cpu.aX", cpu.aX)
    assert cpu.aX == [1,1,1,4,4,-1]

        
with open("Day 10/test2.txt","r") as file:
    cpu = CPU(file.readlines())
    cpu.run()
    assert cpu.part1() == 13140

 
with open("Day 10/input.txt","r") as file2:
    cpu2 = CPU(file2.readlines())
    cpu2.run()
    print(cpu2.part1())

