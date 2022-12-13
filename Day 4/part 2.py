# Day 4 : Challenge 1


def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

def expand(item):
    c,d = [int(i) for i in item.split("-")]
    out = list(range(c,d+1))
    print("expand",out)
    return out
    

assert expand("2-4") == [2,3,4]
assert expand("2-2") == [2]
assert expand("6-8") == [6,7,8]

def overlaps(line):
    a,b = [expand(item) for item in line.split(",")]
    out = any(map(lambda c: (c in b), a)) or any(map(lambda c: (c in a), b))
    print("contains", out)
    return out

assert overlaps("2-4,6-8") == False
assert overlaps("2-3,4-5") == False
assert overlaps("5-7,7-9") == True
assert overlaps("2-8,3-7") == True
assert overlaps("6-6,4-6") == True
assert overlaps("2-6,4-8") == True



def countOverlaps(lines):
    out = len(list(filter(overlaps, lines)))
    print("countOverlaps", out)
    return out

def contains(line):
    a,b = [expand(item) for item in line.split(",")]
    out = all(map(lambda c: (c in b), a)) or all(map(lambda c: (c in a), b))
    print("contains", out)
    return out

assert contains("2-4,6-8") == False
assert contains("2-3,4-5") == False
assert contains("5-7,7-9") == False
assert contains("2-8,3-7") == True
assert contains("6-6,4-6") == True
assert contains("2-6,4-8") == False

def countContains(lines):
    out = len(list(filter(contains, lines)))
    print("countContains", out)
    return out

with open("Day 4/test.txt","r") as file:
    assert countOverlaps(file.readlines()) == 4 

with open("Day 4/input.txt","r") as file:
    print(countOverlaps(file.readlines()))

