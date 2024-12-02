f = open("input.txt","r")

total = 0

left = []
right = dict()

for line in f.readlines():
    line = line.split(" ")
    left.append(int(line[0]))
    # right.append(int(line[-1])) 
    right[int(line[-1])] = right.get(int(line[-1]), 0) + 1

# left.sort()
# right.sort()

print(left)
print(right)

for i in range(len(left)):
    # total += abs(left[i] - right[i])
    total += left[i] * right.get(left[i],0)
    print(i, left[i], right.get(left[i],0))

print(total)

