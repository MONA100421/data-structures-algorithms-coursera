import sys

def read_input():
    pieces = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            pieces.append(tuple(line.strip("()").split(",")))
    return pieces

def valid(board, r, c, piece):
    if r > 0:  # check up
        if board[r-1][c][2] != piece[0]:
            return False
    if c > 0:  # check left
        if board[r][c-1][3] != piece[1]:
            return False
    return True

def solve(pieces):
    n = 5
    used = [False] * len(pieces)
    board = [[None]*n for _ in range(n)]

    def backtrack(r, c):
        if r == n:
            return True
        nr, nc = (r, c+1) if c+1 < n else (r+1, 0)
        for i, piece in enumerate(pieces):
            if not used[i] and valid(board, r, c, piece):
                used[i] = True
                board[r][c] = piece
                if backtrack(nr, nc):
                    return True
                used[i] = False
        return False

    backtrack(0, 0)
    return board

def main():
    pieces = read_input()
    board = solve(pieces)
    for row in board:
        print(";".join("({},{},{},{})".format(*p) for p in row))

if __name__ == "__main__":
    main()
