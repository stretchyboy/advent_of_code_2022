# Day 2 : Challenge 1
WIN = True
LOOSE = False
A = Rock    = X = 1
B = Paper   = Y = 2
C = Scissors= Z = 3
#Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
SCORES = {"A":A,"B":B,"C":C,"X":X,"Y":Y,"Z":Z} 


def score(line):
    you, end = line.split(" ")
    #print("end",end, "you",SCORES[you])
    if(end == "Y"):
        return 3 + SCORES[you]
    if(end == "Z"):
        if SCORES[you] == Scissors:
            return 6 + Rock
        if SCORES[you] == Rock:
            return 6 + Paper
        if SCORES[you] == Paper:
            return 6 + Scissors
    else:
        if SCORES[you] == Paper:
            return Rock
        if SCORES[you] == Scissors:
            return Paper
        if SCORES[you] == Rock:
            return Scissors
        

assert score('A Y') == 4
assert score('B X') == 1
assert score('C Z') == 7

    
def guideScore(guide):
    return sum([score(line) for line in guide.split("\n")])

assert guideScore('''A Y
B X
C Z''') == 12

##14652
with open("Day 2 input","r") as file:
    input = file.read()
    print ("input", input)
    print(guideScore(input))

