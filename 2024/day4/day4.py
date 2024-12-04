f = open("input.txt","r")

total = 0 
array = []

for line in f.readlines():
    array.append(list(line.strip()))

# def is_word(target, row, col, drow, dcol):
#     for i in range(len(target)):
#         r = row+drow*i
#         c = col+dcol*i
#         if 0 > r or r >= len(array) or 0 > c or c >= len(array[0]) or array[r][c] != target[i]:
#             return False
#     return True

# directions = [(x,y) for y in range(-1,2) for x in range(-1,2)]

def is_word(r,c):
        if 1 > r or r >= len(array)-1 or 1 > c or c >= len(array[0])-1:
             return False
        
        if (((array[r+1][c+1] == "M" and array[r-1][c-1] == "S") or
            (array[r+1][c+1] == "S" and array[r-1][c-1] == "M")) and
            ((array[r+1][c-1] == "M" and array[r-1][c+1] == "S") or
            (array[r+1][c-1] == "S" and array[r-1][c+1] == "M"))):
             return True
        
        return False

for r in range(len(array)):
    for c in range(len(array[0])):
        
        if array[r][c] == "A":
            if is_word(r,c):
                total += 1

        # if array[r][c] == "X":
        #     for dr,dc in directions:
        #         if is_word("XMAS",r,c,dr,dc)
        #             # print(array[r:r+dr*4][c:c+dr*4])
        #             total += 1

print(total)

