# Day 11 : Challenge 1
import yaml

class Monkeys():
    def __init__(self, text) -> None:
        monkeytext = text.split("\n\n")
        print("monkeytext", len(monkeytext))
        self.monkeys = [Monkey(item) for item in monkeytext]
    
    def run(self):
        self.reset()
        for j in range(20):
            print("Round", j+1)
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
        print("self.source", self.source)
        attr = {key.strip():value.strip() for key,value in [line.split(":") for line in self.source.split("\n")] }
        print("attr", attr)
        #'If true': 'throw to monkey 1', 'If false': 'throw to monkey 3'}
        self.operation = attr['Operation']
        test = attr['Test'].split(" ")
        if test[0] == 'divisible':
            self.test = lambda value : value % int(test[2]) == 0
        
        if_true = attr['If true'].split(" ")
        if if_true[0] == 'throw':
            self.if_true_target = int(if_true[3])
        if_false = attr['If false'].split(" ")
        if if_false[0] == 'throw':
            self.if_false_target = int(if_false[3])
            
        self.items = [int(item.strip()) for item in attr['Starting items'].split(",")] 
        
        
                
    def catch(self, val):
        self.items.append(val)
    
    def do_operation(self, old):
        data = {"old":old,"new":0}
        
        #print("self.operation", self.operation, "old", old)
        exec(self.operation, {}, data)
        #print("new", data["new"])
        return data["new"]
    
    def inspect(self, val):
        self.inspections += 1
        return self.do_operation(val)
    
    def relief(self, val):
        return int(val / 3)

    def hasItems(self):
        return len(self.items) > 0
    
    def turn(self):
        original = self.items.pop(0)
        inspected = self.inspect(original)
        relieved = self.relief(inspected)
        
        target = self.if_false_target
        result = self.test(relieved)
        if result:
            target = self.if_true_target
            
        #print("original",original,"inspected", inspected, "relieved", relieved, "result", result, "target", target)
        #print("self.items", self.items)
        return (relieved, target)
        
    def reset(self):
        self.inspections = 0
        pass
    
    def getScore(self):
        return self.inspections 
        
with open("Day 11/test.txt","r") as file:
    monkeys = Monkeys(file.read())
    monkeys.run()
    assert monkeys.monkeyBusiness() == 10605
 
with open("Day 11/input.txt","r") as file2:
    monkeys2 = Monkeys(file2.read())
    monkeys2.run()
    print(monkeys2.monkeyBusiness())

