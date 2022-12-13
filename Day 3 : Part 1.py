# Day 3 : Challenge 1

print("ord a", ord("a"),ord("z"),ord("A"),ord("Z") )

def points(letter):
    num = ord(letter)
    if(num < 97):
        out = 26+ num - 64
    else :
        out = (num - 96)
    #print(out)
    return out

assert points("a") == 1 
assert points("z") == 26
assert points("A") == 27
assert points("Z") == 52

def both(line):
    half = int(len(line)/2)
    a = list(line[:half]) 
    b = list(line[half:]) 
    print (a,b,len(a), len(b))
    remaining = next(filter((lambda l: l in b), a), None)
    
    print("remaining", remaining)
    
    return remaining

assert both('vJrwpWtwJgWrhcsFMMfFFhFp') == 'p'
assert both('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL') == 'L'
assert both('PmmdzqPrVvPwwTWBwg') == 'P'
assert both('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn') == 'v'
assert both('ttgJtRGJQctTZtZT') == 't'
assert both('CrZsJsPPZsGzwwsLwLmpwMDw') == 's'

    
def rucksackPriority(line):
    share = both(line)
    return points(share)

assert rucksackPriority('vJrwpWtwJgWrhcsFMMfFFhFp') == 16
assert rucksackPriority('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL') == 38
assert rucksackPriority('PmmdzqPrVvPwwTWBwg') == 42
assert rucksackPriority('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn') == 22
assert rucksackPriority('ttgJtRGJQctTZtZT') == 20
assert rucksackPriority('CrZsJsPPZsGzwwsLwLmpwMDw') == 19

    
def totalPriority(rucksacks):
    return sum([rucksackPriority(line) for line in rucksacks.split("\n")])

assert totalPriority('''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw''') == 157

##14652
with open("Day 3 input.txt","r") as file:
    input = file.read()
    print ("input", input)
    print(totalPriority(input))

