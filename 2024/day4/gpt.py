f = open("input.txt","r")


count = 0
board = []

for line in f.readlines():
    board.append(list(line.strip()))

# Directions: (dr, dc) -> (down, right), (down, left), (up, right), (up, left), horizontal, vertical
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def is_word_found(board, word, row, col, dr, dc):
    """Check if the word can be found starting at (row, col) in direction (dr, dc)."""
    for i in range(len(word)):
        r, c = row + i * dr, col + i * dc
        # Check if out of bounds or the character doesn't match
        if not (0 <= r < len(board) and 0 <= c < len(board[0])) or board[r][c] != word[i]:
            return False
    return True

for row in range(len(board)):
    for col in range(len(board[0])):
        for dr, dc in directions:
            if is_word_found(board, "XMAS", row, col, dr, dc):
                count += 1

print(count)