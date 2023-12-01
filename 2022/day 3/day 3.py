f = open("input.txt","r")
import copy 

totalDuplicates = []
n = 0
duplicates = set()


for line in f.readlines():

    if n % 3 == 0:
        totalDuplicates += duplicates
        duplicates = set()

    line = set(line.strip())
    duplicatesCopy = copy.copy(duplicates)

    if duplicates == set():
        duplicates = line
    else:
        for char in duplicatesCopy:
            if char not in line:
                duplicates.remove(char)

    n += 1
    
totalDuplicates += duplicates
    
# for testcase in f.readlines():
#     midpoint = len(testcase)//2
#     first = set(testcase[:midpoint])
#     second = set(testcase[midpoint:])

#     for char in first:
#         if char in second:
#             duplicates += char

def getScore(item):
    if str.islower(item):
        return ord(item) - ord("a") + 1
    else:
        return ord(item) - ord("A") + 27

total = 0
for item in totalDuplicates:
    total += getScore(item)

print(total)