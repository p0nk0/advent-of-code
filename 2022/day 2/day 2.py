f = open("input.txt","r")

total = 0

for line in f.readlines():
    # A,B,C = rock,paper,scissors
    # X,Y,Z = rock,paper,scissors
    op = line[0]
    me = line[2]
    
    score = 0

    if me == "X":
        # need to lose
        if op == "A": me = "Z"
        elif op == "B": me = "X"
        elif op == "C": me = "Y"
    elif me == "Y":
        # need to tie
        if op == "A": me = "X"
        elif op == "B": me = "Y"
        elif op == "C": me = "Z"
    elif me == "Z":
        # need to win
        if op == "A": me = "Y"
        elif op == "B": me = "Z"
        elif op == "C": me = "X"

    if me == "X":
        score += 1
    elif me == "Y":
        score += 2
    elif me == "Z":
        score += 3
    
    if ((me == "X" and op == "C") or 
    (me == "Y" and op == "A") or 
    (me == "Z" and op == "B")):
        # I win
        score += 6
    elif ((me == "X" and op == "A") or 
    (me == "Y" and op == "B") or 
    (me == "Z" and op == "C")):
        # tie
        score += 3
    
    total += score

print(total)
