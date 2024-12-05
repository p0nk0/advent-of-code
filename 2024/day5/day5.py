f = open("input.txt","r")

total = 0 
rules = {} # X|Y means rules[x] = set with Y in it

rulesOver = False

def isCorrect(pages):
    validPages = set()
    seen = set()
    pages = line.split(",")
    dependencies = {}
    valid = True

    for page in pages:
        if page in rules:
            for validPage in rules[page]:
                if validPage in seen:
                    valid = False
                validPages.add(validPage)

        seen.add(page)

    for page in seen:
        dependencies[page] = set()
        if page in rules:
            for value in rules[page]:
                if value in seen:
                    dependencies[page].add(value)

    return (valid, dependencies)

for line in f.readlines():
    line = line.strip()
    if line == "":
        print(rules)
        rulesOver = True
        continue

    if not rulesOver:
        rule = line.split("|")
        if rule[0] not in rules:
            rules[rule[0]] = set()
        rules[rule[0]].add(rule[1])
    else:
        pages = line.split(",")
        valid, dependencies = isCorrect(pages)
        if not valid:
            res = list(dependencies.keys())
            res.sort(key=lambda x: len(dependencies[x]), reverse=True)
            total += int(res[len(res)//2])
        
print(total)