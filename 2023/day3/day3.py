
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


def is_adjacent(array, i, j):
    for dx in range(-1,2):
        for dy in range(-1,2):
                if is_symbol(array,i+dx,j+dy):
                    return True
    return False


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
        while j < len(row):
            if row[j].isdigit():
                if is_adjacent(schem, i, j):
                    total += get_num(schem, i, j)
                    while j < len(row) and (row[j].isdigit()):
                        j += 1
            j += 1

                    #continue to end of row, or end of current number


    print(total)

if (__name__ == "__main__"):
    main()