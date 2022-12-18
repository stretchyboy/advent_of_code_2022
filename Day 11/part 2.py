# Day 11 : Challenge 2

#import gmpy2
#from codetiming import Timer
#from memory_profiler import profile

#fp=open('memory_profiler.log','w+')

class Monkeys():
    rounds = 10000
    #rounds = 1000
    
    def __init__(self, text) -> None:
        monkeytext = text.split("\n\n")
        #print("monkeytext", len(monkeytext))
        self.monkeys = [Monkey(item) for item in monkeytext]
        clockspace = 1
        for i in range(len(self.monkeys)):
            clockspace *= self.monkeys[i].divisible
        for i in range(len(self.monkeys)):
            self.monkeys[i].clockspace = clockspace
            
    
    #@Timer(name="Run", text="{name} {tick} - Elapsed time: {:0.4f} seconds")
    def run(self):
        self.reset()
        self.j = 0 
        while self.j < self.rounds:
            self.round()
            self.j +=1
            if(self.j == 1 or self.j ==20 or ((self.j)%1000 )== 0) :
                print("Round", self.j, [k.getScore() for k in self.monkeys])
          
    
    #@Timer(name="Round", min=10, text="{name} {tick} - Elapsed time: {:0.4f} seconds")
    def round(self):
        for i in range(len(self.monkeys)):
            #print("Monkey", i)
            monkey = self.monkeys[i]
            while monkey.hasItems():
                (val,target) = monkey.turn()
                #print("val", val,"target", target)
                self.monkeys[target].catch(val)
                
        
        
    def reset(self):
        pass
        
    def monkeyBusiness(self):
        scores = [monkey.getScore() for monkey in self.monkeys]
        print("scores", scores)
        scores.sort(reverse=True)
        mb = scores[0] * scores[1]
        print("mb", mb)
        return mb
    
class Monkey():    
    def __init__(self, text) -> None:
        self.source = text
        self.parse()
        self.reset()
    
    def parse(self):
        #print("self.source", self.source)
        attr = {key.strip():value.strip() for key,value in [line.split(":") for line in self.source.split("\n")] }
        #print("attr", attr)
        #'If true': 'throw to monkey 1', 'If false': 'throw to monkey 3'}
        self.operation = attr['Operation']
        self.aOperation = attr['Operation'].split(" ")
        #print("self.aOperation", self.aOperation)
        
        '''
        if self.aOperation[3] == '*':
            if self.aOperation[4] == 'old':
                self._operation2 = lambda value : value * value
            else :
                param = int(self.aOperation[4])
                self._operation2 = lambda value : value * param
        elif self.aOperation[3] == '+':
            if self.aOperation[4] == 'old':
                self._operation2 = lambda value : value + value
            else :
                param = int(self.aOperation[4])
                self._operation2 = lambda value : value + param
        '''
        self.clockspace = 1
        
        
        test = attr['Test'].split(" ")
        if test[0] == 'divisible':
            self.divisible = int(test[2])
            self._test = lambda value : value % (self.divisible) == 0
        
        if_true = attr['If true'].split(" ")
        if if_true[0] == 'throw':
            self.if_true_target = int(if_true[3])
        if_false = attr['If false'].split(" ")
        if if_false[0] == 'throw':
            self.if_false_target = int(if_false[3])
            
        self.items = [int(item.strip()) for item in attr['Starting items'].split(",")] 
        
        
                
    def catch(self, val):
        self.items.append(val)
    
    #@Timer(name="do_operation", min=0.1, text="{name} {tick} - Elapsed time: {:0.4f} seconds")
    def do_operation(self, old):
        data = {"old":old,"new":0}
        
        #print("self.operation", self.operation, "old", old)
        exec(self.operation, {}, data)
        #print("new", data["new"])
        return data["new"]
    
        
    #@Timer(name="test", min=0.1, text="{name} {tick} - Elapsed time: {:0.4f} seconds")
    def test(self, val):
        return self._test(val)
    
    #@profile(stream=fp)
    def _operation(self, value):
        if self.aOperation[3] == '*':
            if self.aOperation[4] == 'old':
                
                out = pow(value,2)
                #print("value", value, "out", out)
                return out
            else :
                return value * int(self.aOperation[4])
        if self.aOperation[3] == '+':
            if self.aOperation[4] == 'old':
                return value + value
            else :
                return value + int(self.aOperation[4])
        
    #@Timer(name="Inspect", min=1, logger=fp.write, text="{name} {tick} - Elapsed time: {:0.4f} seconds")
    def inspect(self, val):
        self.inspections += 1
        #return self.do_operation(val)
        #return int(self._operation2(val))
        return int(self._operation(val))

    def hasItems(self):
        return len(self.items) > 0
    
    def relief(self, val):
        #return val % self.clockspace
        return val % self.divisible
    
    #@Timer(name="turn", min=1, text="{name} {tick} - Elapsed time: {:0.4f} seconds")
    #@profile(stream=fp)
    def turn(self):
        original = int(self.items.pop(0))
        inspected = self.inspect(original)
        relieved = self.relief(inspected)
        target = self.if_false_target
        result = self.test(relieved)
        if result:
            target = self.if_true_target            
        return (inspected, target)
        
    def reset(self):
        self.inspections = 0
        pass
    
    def getScore(self):
        return self.inspections 
'''        
with open("Day 11/test.txt","r") as file:
    monkeys = Monkeys(file.read())
    monkeys.run()
    assert monkeys.monkeyBusiness() == 2713310158
'''

with open("Day 11/input.txt","r") as file2:
    monkeys2 = Monkeys(file2.read())
    monkeys2.run()
    print(monkeys2.monkeyBusiness())
