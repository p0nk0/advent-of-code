f = open("input.txt","r")
lines = f.readlines()
line = lines[0]

curchars = line[0:14]

index = 14

def isMarker(l):
    for n in range(len(l)):
        if l[n] in l[:n] + l[n+1:]:
            return False
    return True

for char in line[14:]:
    index += 1
    curchars = curchars[1:] + char
    if isMarker(curchars):
        break

print(index,curchars)

# there's a bug somewhere in here lmao