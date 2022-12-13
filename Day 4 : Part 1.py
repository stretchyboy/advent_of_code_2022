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

def shared(lines):
    a = lines[0]
    b = lines[1]
    c = lines[2]
    remaining = next(filter((lambda l: (l in b ) and (l in c)), a), None)
    
    print("remaining", remaining)
    
    return remaining

assert shared('''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg'''.split("\n")) == "r"
    
assert shared('''wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''.split("\n")) == "Z"

def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

def groupPriority(lines):
    return points(shared(lines))
    
assert groupPriority('''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg'''.split("\n")) == 18
    
assert groupPriority('''wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''.split("\n")) == 52

def totalPriority(text):
    groups = divide_chunks(text.split("\n"), 3)
    return sum([groupPriority(group) for group in groups])

assert totalPriority('''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw''') == 70

##14652
with open("Day 3 input.txt","r") as file:
    input = file.read()
    #print ("input", input)
    print(totalPriority(input))

