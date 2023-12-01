f = open("input.txt","r")
lines = f.readlines()

boxes = [[" "]*9 for x in range(8)]

for n in range(8):
    line = lines[n].strip('\n')
    line = [line[n:n+3] for n in range(0,len(line),4)]
    for i in range(len(line)):
        boxes[n][i] = line[i][1]

stacks = [[] for x in range(9)]
for n in range(7,-1,-1):
    for i in range(len(boxes[n])):
        item = boxes[n][i]
        if item != " ":
            stacks[i] += item

def move(start,end):
    box = stacks[start][-1]
    stacks[start] = stacks[start][:-1]
    stacks[end] += box

def move2(start,end,num):
    temp = []
    for n in range(num):
        temp += stacks[start][-1]
        stacks[start] = stacks[start][:-1]
    stacks[end].extend(temp[::-1])

for n in range(10,len(lines)):
    line = lines[n].split()

    num = int(line[1])
    start = int(line[3])-1
    end = int(line[5])-1

    move2(start,end,num)

    # for n in range(num):
    #     move(start,end)

answer = ""
for n in range(len(stacks)):
    answer += stacks[n][-1]

print(answer)