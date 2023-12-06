
# gets all digits of a number located at row i, col j
# assumes array is a square
def get_num(array, i, j):
    if not array[i][j].isdigit():
        return 0
    
    # go left until we hit left edge or a non-digit
    # same with going right
    left = j
    right = j
    row = array[i]

    while left > 0 and row[left-1].isdigit():
        left -= 1

    while right < len(row) and row[right].isdigit():
        right += 1
    
    res = 0
    for digit in row[left:right]:
        res *= 10
        res += int(digit)

    print(res)
    return res


def is_symbol(array, i, j):
    if i < 0 or i >= len(array) or j < 0 or j >= len(array[0]):
        return False
    elif not array[i][j].isdigit() and array[i][j] != ".":
        return True
    return False

def in_bounds(array, i, j):
    return not (i < 0 or i >= len(array) or j < 0 or j >= len(array[0]))


def num_adjacent(array, i, j):
    num_adjacent = 0
    total = 1


    sub_array = [["."]*3 for _ in range(3)]

    for dx in range(-1,2):
        for dy in range(-1,2):
            if in_bounds(array,i+dx,j+dy):
                sub_array[dx+1][dy+1] = array[i+dx][j+dy]
    
    top = sub_array[0]
    bottom = sub_array[2]
    left = sub_array[1][0]
    right = sub_array[1][2]

    if top[1] == ".":
        if top[0] != ".":
            num_adjacent += 1
            total *= get_num(array,i-1,j-1)
        if top[2] != ".":
            num_adjacent += 1
            total *= get_num(array,i-1,j+1)
    else:
        num_adjacent += 1
        total *= get_num(array,i-1,j)
    

    if bottom[1] == ".":
        if bottom[0] != ".":
            num_adjacent += 1
            total *= get_num(array,i+1,j-1)
        if bottom[2] != ".":
            num_adjacent += 1
            total *= get_num(array,i+1,j+1)
    else:
        num_adjacent += 1
        total *= get_num(array,i+1,j)

    if left != ".":
        num_adjacent += 1
        total *= get_num(array,i,j-1)

    if right != ".":
        num_adjacent += 1
        total *= get_num(array,i,j+1)

    print(f"{num_adjacent} adjacent to {i,j}")

    if num_adjacent == 2:
        return total
    else:
        return 0

def main():
    f = open("input.txt","r")

    total = 0

    schem = []
    # creates schematic as 2d array
    for line in f.readlines():
        schem.append(list(line.strip()))

    for i, row in enumerate(schem):
        print(i, row)
        j = 0
        for j in range(len(row)):
            if row[j] == "*":
                total += num_adjacent(schem, i, j)


    print(total)

if (__name__ == "__main__"):
    main()