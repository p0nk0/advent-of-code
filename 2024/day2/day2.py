#I'm off by 1, the right answer is 569. I can't figure out what's wrong.

f = open("input.txt","r")

total = 0


def is_valid(report):
    increasing = True if report[0] < report[1] else False
    violations = []
    for i in range(len(report)-1):
        if ((report[i] > report[i+1] and increasing) or (report[i] < report[i+1] and not increasing) or 
            (abs(report[i] - report[i+1]) < 1) or (abs(report[i] - report[i+1]) > 3)):
            violations.append(i)
    return len(violations) == 0, violations



for line in f.readlines():

    report = list(map(lambda x: int(x), line.split(" ")))
    valid, violations = is_valid(report)

    if valid:
        total += 1
        continue
    
    safe = False
    for violation in violations:
        if (is_valid(report[0:violation] + report[violation+1:])[0] or 
           is_valid(report[0:violation+1] + report[violation+2:])[0]):
            safe = True
            break
        

    if safe:
        total += 1

print(total)

