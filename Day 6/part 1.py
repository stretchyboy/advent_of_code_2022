# Day 6 : Challenge 1

def getStart(sBuffer):
    aBuffer = list(sBuffer)
    for i in range(4,len(aBuffer)):
        if len(set(aBuffer[i-4:i])) == 4:
            return i        
        
        
assert getStart("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
assert getStart("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
assert getStart("nppdvjthqldpwncqszvftbrmjlhg") == 6
assert getStart("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
assert getStart("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11



def getStartM(sBuffer):
    aBuffer = list(sBuffer)
    target =14
    for i in range(target,len(aBuffer)):
        if len(set(aBuffer[i-target:i])) == target:
            return i        
    

assert getStartM("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
assert getStartM("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
assert getStartM("nppdvjthqldpwncqszvftbrmjlhg") == 23
assert getStartM("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
assert getStartM("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26

with open("Day 6/input.txt","r") as file:
    #print(getStart(file.read()))
    print(getStartM(file.read()))

