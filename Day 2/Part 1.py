# Day 2 : Challenge 1
WIN = True
LOOSE = False
A = Rock    = X = 1
B = Paper   = Y = 2
C = Scissors= Z = 3
#Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
SCORES = {"A":A,"B":B,"C":C,"X":X,"Y":Y,"Z":Z} 


def score(line):
    you, me = line.split(" ")
    print("me",SCORES[me], "you",SCORES[you])
    if(SCORES[me] == SCORES[you]):
        return 3 + SCORES[me]
    if(SCORES[me] == Rock and SCORES[you] == Scissors):
        return 6 + SCORES[me]
    if(SCORES[me] == Scissors and SCORES[you] == Paper):
        return 6 + SCORES[me]
    
    if(SCORES[me] == Paper and SCORES[you] == Rock):
        return 6 + SCORES[me]
    return SCORES[me]

assert score('A Y') == 8
assert score('B X') == 1
assert score('C Z') == 6

    
def guideScore(guide):
    return sum([score(line) for line in guide.split("\n")])

assert guideScore('''A Y
B X
C Z'''
) == 15

print(guideScore('''C Y
C Z
C Z
C Z
A Y
C Z
C Z
B Y
C Y
A X
C Z
A Z
C Y
C Z
C Z
B X
A Z
C Z
C Z
C Z
A Z
B X
C Y
C Z
C Z
C Z
C Y
C Z
C Z
C Z
C Z
C Z
A Z
B X
A Z
C Z
C Z
C Z
C Z
A Z
A X
B X
C Y
A Z
A Z
C Y
A Z
A Z
C Y
A Z
B X
A Z
C Z
B X
C Y
C Z
C Z
B Z
C Y
C Z
A Z
C X
C Z
B X
B Y
C Z
C Z
C Y
A Z
C Y
C Y
B X
A Z
B Z
C Z
C Z
C Z
B X
A X
B Y
C Z
C Y
C Y
A Z
A Z
C Z
C Z
C Z
A X
A X
C Y
C Z
A Z
C Y
A Z
A Z
C Z
A Z
C Y
C Z
A Z
A X
C Z
C Z
A Z
B Y
A Z
B X
C Z
C Y
A X
C Z
C Y
C Z
C Z
B Y
C Z
A Z
C Z
B X
C Z
C Y
A Z
B Y
B X
B X
A X
B X
A Z
B X
A Y
A X
A Z
A Z
C Y
B X
C Z
C Z
A X
A Z
A Y
B X
A Y
A Z
C Z
A X
C Z
C Z
C Z
B X
C Z
C Y
C Y
C Z
A Z
C Z
B X
A Z
C Y
A X
A Z
A Y
C Z
A Z
C Z
C Z
A Z
C Y
A Z
C Z
A Z
C Z
B X
C Z
A Z
C Z
C X
B Y
A Z
C Z
C Y
C Z
A Z
C Y
B Z
A X
A Z
B X
C Y
C Z
B X
C Y
C Y
A Z
B X
C Y
C Y
A Z
C X
B X
B Y
C Y
C Z
B X
C Z
A Z
A Z
B X
B X
C Y
C Z
B X
C Z
A Z
B X
C Y
C Z
C Z
A X
B X
A Z
C Z
A X
C Y
B Y
B X
C Z
C Y
C Y
A Y
C Z
C Y
C Z
C Z
A Z
C Z
C Y
A Z
C Y
C Z
C Y
C X
B X
A X
B X
C Z
A Z
C Y
C Z
B X
C X
B X
C Z
C Z
C Y
B X
C Z
A Y
C Z
A X
C Z
C Z
C Y
C Z
C X
B X
C Z
C Z
C Y
B Y
C Z
A X
C X
C Y
A Z
C X
A Z
C Y
C Z
C Z
B X
A X
C Z
B X
C Y
B X
A X
A Z
A Z
C Z
C Z
B X
C Z
A Z
C X
C Z
C Z
C Z
C Y
C Y
A Z
C Z
C Z
C Z
C Z
C Z
C Z
C Z
C Z
C Z
A Z
C Z
C Y
C Y
A Z
C Z
A Z
A X
C Z
C Y
C Z
C Z
C Z
C Z
C Y
C Z
A Z
B X
A X
B X
A Y
C Z
C Y
A Z
C X
C Z
C Z
C Z
C Z
C Y
A X
B Z
A Z
C Z
A X
C Z
C Z
A Z
C Z
C Z
A Z
C Z
B X
C Z
A X
C Y
A Z
B X
B X
C Z
B Z
C Z
B X
C Y
B X
C Y
A Z
A Y
A Z
C Z
C Z
A Z
C Z
A X
A Z
C Y
A X
C Y
C Z
C Z
C Z
A X
C Y
A Z
A Z
A X
C Z
C Z
B Y
A X
C Y
C Y
C Z
C Z
A Z
A Z
C Y
C Z
A Z
C Y
C Z
A Z
C Z
A Z
C Z
A Z
C Z
C Z
A Z
A Z
C Z
A Z
C Z
A Z
C Z
C Z
A Z
C Z
B Y
A Z
B X
C Y
C Y
C Z
A Z
A X
C Z
C Z
C Z
B Z
C Z
C Z
C Z
A Z
C Z
C Z
A X
C Z
C Y
A X
A Z
C Z
C Z
A Z
C X
A Z
C Z
C Y
A Z
A Y
A Z
C Z
C Z
C Z
C Z
C X
C Z
C Z
B X
B X
A Z
C Z
C Z
A Z
A Z
A Z
C Y
C Z
C Z
C Y
C Y
C Z
C Z
B X
A Z
C Z
C Y
A Z
C Z
A Z
C Z
C Y
C Y
C Z
B X
A Z
B X
C Z
C Z
C Z
A Z
C Z
C Y
C Z
B Y
C Z
C Z
C Y
A Z
C Z
B X
C Z
B Y
C Y
C Z
C Z
C Z
B Y
A Z
C Z
A Y
A Z
C Y
A Z
C Z
C Z
C Y
B Z
B X
C Z
B Z
C Z
C Y
B X
C Y
C Z
A X
A Z
C Y
C Y
A Z
C Y
B Z
B Y
C X
B X
C X
C Z
C Y
C Z
C Z
C Y
C Z
A Z
C Y
A X
C Z
C Z
C Z
C Z
C Z
C Z
A Z
B Y
C Z
C Z
A Z
B X
C Z
C Z
A Z
C Z
C Z
A Z
C Z
A X
B Y
C Y
C Y
C X
A Z
C X
C Z
B Z
B X
C Y
A Z
C Z
C Z
A X
A Z
C Y
A X
C Z
C Z
C Z
A Z
A Z
C Z
B Y
B X
B X
A Z
C Z
C Y
C Z
C Z
A Z
A X
C Y
A Z
C Y
C Y
A X
A Z
B X
A Z
B Y
A Z
C Z
B X
A Z
B X
C Y
B Z
C Y
C X
C Z
C Y
B X
B Y
B Y
C Z
C Y
A Z
A Z
C Y
C Z
C Y
B Z
C Z
C X
C Z
C Z
B X
C Z
B X
A Z
C Z
C Y
A Z
C Z
C Y
C X
A X
A Y
C Y
C Y
C Y
A Z
B Z
A Z
C Z
C Z
C Z
A Z
A X
A Z
C X
B X
C Z
A X
A Z
C Y
A Z
A Z
A Z
C Z
C Z
A Z
C Z
A Z
A Z
C Z
C Y
A Z
C Y
A Z
A Z
A Z
B X
B X
A Z
C Z
C Y
A Z
C Z
B X
C Z
C Z
C Z
A Z
A X
C Z
C Z
A X
A Z
C Y
C Z
C Z
C Z
C Z
C Z
C Y
C Z
A Z
C Z
B X
B X
A Z
C Z
C Y
C Y
B X
B X
C Y
C X
B X
A Z
A Z
C Z
C Y
A Z
C Z
C Z
C Z
A Z
C Z
C Z
B X
C Y
C Z
C Z
C Z
C Z
C Z
C Y
A X
C Z
C Z
A Z
A Z
C Y
C Z
C Z
C Z
A Z
B X
C Z
A X
A Z
A Z
C Z
A Z
C Z
C Z
C Z
C X
C Z
B X
C X
C Y
C Z
A X
A X
A Y
C X
C Y
B X
C X
A Z
C Z
C X
C Z
C Y
A X
A Z
C Z
C Z
A X
A Y
B X
C Z
C Z
C Z
B X
C Z
A Z
A Y
A Z
C Z
B X
A Z
C Z
C Z
C Z
B X
C Z
C X
C Z
C Z
B X
C Y
A X
C Z
C Y
C Z
C Y
A Z
C Z
A Z
A Z
C Z
C Z
A Z
C Y
C Y
B Y
A Z
A Z
B X
C Z
C Z
A X
B Z
C Z
C Z
A Z
A X
C Z
C Z
C X
C Z
B X
A Z
C Y
A Z
C Z
C Z
A X
C Z
C Z
A Z
C Z
A Z
B X
C Y
A Z
C Y
A Z
A Y
B X
C Z
A Y
C Z
C Z
B X
C Z
A X
C Z
A Z
A X
C Y
B X
C Z
C Z
C Y
A X
B X
A X
A Z
C Z
B Y
C Z
A Z
C Z
A X
B Z
C Z
C Y
C Y
A Y
B X
C Y
C Z
A Y
C Y
C Y
A Z
A Z
C Z
C Z
C Z
C Y
A Z
C Z
C Z
A Z
B Y
C Z
C Y
C Z
C Z
B Y
A X
C Z
A X
C Z
C X
A Z
C Z
A Z
C Z
B X
C Z
C Z
C X
C Z
C Z
A Z
A Z
B Z
C X
C Y
C Y
C Y
A Z
C X
C Z
A X
C Z
C Z
C X
A X
A X
C Z
A X
B Z
C Y
C Z
C Y
C Z
C Y
C Z
A Z
A X
C Z
B Y
C Z
C Z
B X
C Z
B X
C Z
C Y
A X
A Z
C X
C Y
C Z
C X
C Z
B X
A Z
C X
A Y
B Z
C Z
B X
C Z
C Z
C Y
C Z
A X
B X
C Z
A Z
C Z
C Z
C Z
A X
C Z
A Y
C Z
C Z
C Z
C Y
A Z
C X
A X
C Y
C Z
A Z
A Y
C Z
B Y
C X
A Z
C Y
C Z
A X
C Z
A Z
B X
A Z
C Z
B Z
A Z
A Z
C Y
C Z
A Y
A Z
C Y
C Z
C Z
C Z
C Y
C X
B X
C Z
B Y
C X
A Z
C Z
C Z
A Z
C Z
B Y
A Z
B Y
A Z
C Y
C Z
C Z
A Z
C Z
B Y
C X
A Z
A X
C Z
C Z
C X
A X
C Z
C Y
C Z
C Z
C Z
B Y
C Z
A Z
A Z
B X
A Z
C Z
C Z
C Z
A X
C Y
C Z
C Z
C Z
B X
A Z
A X
B Y
B X
B X
C Z
B X
C Y
A X
C X
C Z
C Z
C Y
C Z
C Z
A X
A Z
A X
B Y
A X
A Z
B Y
C X
C Y
C Z
C Z
A Z
A X
B Y
A Z
C Z
C Z
C Y
A Z
A X
C Z
A Y
A Z
A X
B X
B Y
C Z
C Z
A Z
C Z
A X
A Z
C Z
C Y
B X
A Z
B X
C Y
B X
A Z
A Z
A Z
B Y
C Z
A Z
C Z
C X
B Y
C Z
A Z
C Z
A Z
A X
C Z
C Z
C X
C Y
B X
B Y
A Z
A Y
A Z
C Z
A X
A X
A Z
B X
C Z
B X
B X
C Y
A Z
A X
C Z
B X
B Y
A X
B X
A Y
C Z
A Z
C Z
C Y
C Y
C Z
C Y
B X
C Z
B Y
A Z
A X
B X
C X
C Z
A Z
C Z
C Z
B X
B Y
C Y
A Z
C X
C Z
A Z
C Z
C Z
C Y
A Z
A Z
C X
C X
C Y
C Z
A X
A Z
C Y
C Y
C Z
A Z
B Y
C Y
A Z
C Y
A Z
B Z
B Y
A Y
B X
C Y
C Z
A Z
C Z
B Z
C Z
C Z
A Z
B Y
C Z
B X
C Z
C Z
C Y
C Y
A Z
A Y
C Z
C X
C Z
A Z
A Z
C Z
C X
C Y
A Y
C Y
A X
C Z
A Z
C Z
B X
C Z
C Z
C Z
A Z
A Y
B Y
A Z
A Z
B X
A X
C Z
C Z
B X
C Y
A X
C Y
A X
B X
C Z
C Z
C X
A Z
C Z
C Z
C Z
C Z
A Z
A Y
A Z
B Z
C Z
B X
C Z
B X
A Z
C Z
C Z
B Z
C Y
B Y
C Z
A Z
A Z
C Y
C Y
C Z
C Y
C Z
A X
C Y
B X
C Y
C Y
B Y
C Z
C Z
B X
C Z
B X
B Y
B X
B X
C Y
A Z
C Y
C Y
C Z
C Z
B X
C Z
A Z
C Y
B X
B X
C Y
C X
C Z
C Z
A X
C Z
B X
C Z
C Z
A X
A Z
C X
A Z
A Z
C Y
C Z
C X
C Y
C Z
A Z
C Z
B X
C Z
C Z
A X
C Z
A X
C Z
C X
C Y
A X
A Z
C X
C Z
A X
A Z
C Z
C Y
B X
A X
B X
C Z
A Z
C X
C Z
B X
A Z
C Z
C Z
B Z
B X
B Y
C Y
C Z
B X
C Z
B Y
C Y
A Z
C Z
C Y
A Z
C Z
A Z
C Y
C Y
A X
B Z
C Y
B X
C Z
C Y
C Z
C X
B X
B Y
A Z
C Z
C Z
A Z
B Z
C Z
C Y
C X
A Z
C Z
B X
C Z
A X
C Z
C Z
A Z
A X
C Y
B Z
C Y
C Z
C Z
C Z
A Z
A Z
C Z
A X
C Z
A Z
C Z
C Z
C Z
B Y
C Z
C Z
B Y
A X
B X
C Z
C Z
C Y
A X
C Z
A Z
C Y
A Z
A Z
C Y
B X
A Z
C Y
C Z
C X
B X
A Z
C Z
C Y
C Z
B Z
B X
A Z
A Z
C Y
A Z
C Z
B X
A Z
C Z
C Z
C X
C Z
C Y
B X
A Z
C Z
C Z
C Z
B X
A Z
B Y
C Z
C Z
A Z
B X
B X
B X
C Z
C Z
A Z
C Z
C Z
B Y
B X
A Z
C Z
C Z
C Z
A Z
B X
C Z
C Z
C Y
C Z
C Y
A Z
C Z
A X
C Z
C Z
B Y
C Z
C Y
B X
A Z
C Z
C Z
C Z
A Z
C Y
A X
C Z
C Z
A Z
C Z
A X
B X
A Z
C Z
B Z
C Z
A Y
B X
A X
C Z
C Z
C Z
C Y
B X
C X
A Z
C Z
C Z
C Y
A Z
C Z
C Z
B Y
C Y
B X
C Z
A X
A Z
C Z
C Z
C X
C Z
B X
C Z
C Z
C Z
C Y
C Z
C Z
C Z
C Z
A Z
C Z
A Z
A Z
B X
A Z
C X
B X
B X
A Z
C Z
C Y
C Z
C Z
C X
C Z
A X
A Z
C Z
C Z
C Z
C Z
C Z
C Z
B Z
C Z
A Z
C Z
A Z
A X
B X
A Z
C Z
C Y
C Z
C Y
A Z
A Z
A Z
A Z
A Z
B Z
A Z
C X
C Z
C Z
C Z
B Y
C Z
B X
A Z
B Y
C Y
C Y
C Z
B X
B X
A Z
A Z
A Z
A Z
C Z
C X
A Z
C Y
B X
C Z
C Z
C Z
C Z
A X
C Z
A Z
C Y
A Z
C Z
C Z
B X
C Z
B Z
C Y
C Z
C Z
C Z
C Z
C Z
A Z
C Z
A Z
A Z
A Z
C Z
C Z
A Z
C Y
C Z
B Z
C Z
C Z
C Y
C Z
A Y
C Z
A X
A Z
C X
C Z
A Z
A Z
A Z
A Z
C Z
A Z
A Z
C Z
C Z
C Z
C Z
A Z
C Y
C Z
C Z
A Z
C Z
B X
B Y
C Z
C Z
A Z
C Z
A Z
C Y
C Z
A Z
C Z
C X
A Z
C Z
C X
C Z
C Y
A Z
C Z
C Z
C Z
B Z
C X
C Z
C Z
A X
A Z
A Z
A Z
C Z
C Z
C X
A Z
A Z
C Y
C Z
A Z
A Z
A Z
C Y
A Z
C Z
A Z
C Z
C Z
A Z
C Y
B X
B X
A Z
B Z
A Z
C Z
C Z
C X
A Z
C Y
C Z
C Y
C Z
C Z
A Z
C Y
C Z
C Y
C Z
C Z
C Z
C Z
C Y
A X
A X
C Z
C Z
B X
C X
C X
C Z
A X
C Y
A X
B X
C X
C Z
C Z
A X
C Y
A Y
A Z
C Z
C Y
C Y
B X
A X
C Z
C Z
B X
A Z
C Z
B Z
C Z
C Y
C X
C Z
A Z
C Z
B X
B X
C Y
C Y
C Z
C Y
A Z
B X
C Z
C Y
A Z
C Z
B Z
B X
A Z
A Z
B Y
B Y
A Z
C Z
B X
A Z
C Z
A Z
C Z
B X
A Z
B X
B X
A X
C Z
A X
A X
A Z
C Y
C X
A X
C Z
C Y
C Z
A Z
A Z
A X
C Z
A Z
C Z
C Y
A Z
C Z
B X
A Z
B Y
C Z
C Y
C Z
C Z
A Z
A Z
C X
A X
C Y
C Z
C Y
C Z
C Z
C Z
A Z
A Y
A X
A Z
C X
B Z
C Z
A Z
A Z
A Z
B X
A Z
C Z
C Z
B X
C Z
A X
A Y
C Z
A Z
C Z
C Z
B X
C Z
C Z
C Z
C Z
C Y
C Z
A Z
C Z
C Y
C Z
C Z
C Z
B X
A Z
C Z
C Z
C Z
A X
C Y
C Z
A Z
C Y
A Z
C Y
C Z
C Z
A Z
A Z
C Y
A Z
B Z
C Z
C Z
B Z
A X
B X
C Z
C Y
A Z
C Y
B Y
A X
C Z
C Z
C Z
C Z
A Z
C Z
A X
C Y
A Z
C Z
B X
B Y
C Z
C Y
C Z
B X
C Y
C Y
C Z
B X
C X
A Y
C Z
C Y
A Z
C Y
A X
B Y
A Y
C Z
C Z
A Z
C Z
C X
A Z
C Z
C Z
C Z
C Y
C Z
A Z
B X
A Z
C Z
B X
C Z
A Z
C Z
B Y
A Z
C Z
A Z
C Z
A X
C Y
A Z
C Z
C Z
C Y
A Z
B X
C Z
A Z
C Z
C Z
A Z
C Z
C X
A Z
C Z
C Z
C Z
C Z
B Z
C Z
C Z
C Z
C Y
B X
A X
C Z
C Z
C Z
C Z
C Z
C Z
C Z
B Z
C Z
A X
C Z
B Y
A Z
A X
C Z
C Z
A Z
C Z
C Y
A X
C Y
C Z
C Z
C Z
C X
C Y
C Z
C Y
C Z
A Y
C Z
A X
C X
C Z
C Z
C Z
A Z
C Z
B X
C Y
A Z
C Z
C X
C Z
C Z
C Z
A Y
A X
A Z
C Y
B X
B X
A Z
A Z
A Z
C Z
C Z
A Z
C Z
A Y
C Y
C Z
C Y
B Z
B Y
B X
A X
C Z
C Z
C Z
C Y
B X
A X
C X
A Z
A Z
C Z
C Y
A Z
A Z
A Z
C Z
C Z
C Y
B X
A Z
C Z
A X
C Y
A Y
B Y
A Z
A Z
A Z
C Z
C Z
B X
A Y
C Z
A Y
C Y
C Z
A Z
C Y
B X
C Z
C Z
C Z
B X
B X
C X
B X
A Z
A Z
C Z
C Z
A X
C Z
C Z
C Z
A Z
A Z
A Z
B X
C X
C Z
A Z
A Z
B X
B X
C X
B X
A Z
C Z
C Z
A X
C X
A Z
C Y
A Z
A Z
B X
C Z
C Z
A Z
A Z
C Z
C Z
C Y
C Y
C Z
C Y
C Z
C Z
C Y
A X
C Z
C Z
A Z
C Z
A Z
C Z
C Z
C Y
C Z
C Y
A Z
C Z
C Y
B Z
B X
B X
A X
C Z
C Z
A Y
C Z
C X
C Z
A Z
A Z
A Z
C Y
B Y
B X
A Z
C Z
C Z
C Y
A Z
C Z
C Z
A X
A X
B X
A Z
C Z
A X
C Z
A Z
C Z
C Z
A Z
C Z
B Y
B X
A Z
C Y
C Z
C Z
A X
C Z
C X
A Z
B X
C Z
C Z
C Z
C Z
C X
C Z
A Z
C Z
A Y
B X
A Z
A X
A Z
C Y
C Z
C Y
C Y
C Y
C X
C Y
C Z
C Z
C Z
C Y
B X
C Z
B X
C Z
C Z
A Z
B X
C Z
A X
C Y
B Y
A X
B Z
B X
A X
A X
A X
B Y
C Y
C Z
B X
C Y
C X
A Z
C Y
A Z
C Z
C X
B X
C Y
A Z
C Y
C Z
A Z
C Y
B Y
C Y
B X
A Z
C Y
C Y
C Z
C Z
C X
B X
C Z
B X
C Z
C Z
A Z
C Z
A Z
C Z
C Z
C Y
C Y
C Z
C Y
A Z
C Z
C Y
A Z
C Z
C Z
C Y
C Z
B X
B X
A X
C Z
A Z
C Z
A Z
C Z
B Y
A X
C Y
C Y
B X
A Z
C Z
C Z
C Y
C Z
A Z
C Y
B Z
C Y
C Z
C Z
C X
C Y
B X
C Y
C Z
C X
A Z
C Z
C Z
C Y
A Z
C Z
A Z
C Y
A Z
A Z
A Y
C Z
A Z
C Z
A Z
C Z
C Z
B Z
A X
C Y
A X
C Z
C Z
A Z
C Z
A X
A X
C Z
B X
B Z
C Y
C Z
A X
B X
C Z
C Z
B X
A Z
C Z
A Z
A Y
C Z
A Z
C Y
C Y
A Y
B X
C Z
C Y
A X
C Z
C Y
A X
A Z
C Y
B X
C Z
A Z
C Z
C Z
A Z
C Z
C Y
C Y
C Z
A Z
B Z
C Y
A Z
C Z
C Y
C X
C Z
C Z
A Z
C Z
C X
C Z
C X
C Y
C Z
A Z
C Z
A Z
B X
C Z
B X
C Z
A X
C Z
C Z
B Y
C Z
C Z
B X
C Z
C Y
C Y
B X
A Z
A X
A Z
A X
C Y
B X
A Z
C Y
A Z
C Z
B X
B Z
C Z
C Y
C Y
C Y
A Z
B X
C Z
C X
A X
B Z
C Y
B X
A Z
C Z
C Z
C Z
C Z
C Y
B X
C Z
C Z
C Z
C Z
A X
A Z
C Z
C Y
C Y
C Z
A Y
C Z
C Z
C Z
B X
C Y
C Z
C Z
A Z
C Z
C Z
C Z
B X
A Z
B X
C Z
C X
A X
C Z
C Z
C Z
C X
A Z
A Z
B X
A Z
C Z
C Z
A Z'''))

