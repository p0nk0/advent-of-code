f = open("input.txt","r")

currentElf = 0
bestElves = set([1,2,3])
for line in f.readlines():
    print(line, currentElf)
    print(bestElves)
    if line == "\n":
        worstElf = min(bestElves)
        if currentElf > worstElf:
            bestElves.remove(worstElf)
            bestElves.add(currentElf)
        currentElf = 0
    else:
        currentElf += int(line)

print(sum(bestElves))

    