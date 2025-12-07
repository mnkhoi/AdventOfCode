# PART 1

# if __name__ == "__main__":
#     f = open('input.txt', 'r')
#     # f = open('test.txt', 'r')
#
#     board = [s.strip() for s in f.readlines()]
#     f.close()
#
#     ROWS, COLS = len(board), len(board[0])
#
#     visited = set()
#     def dfs(r, c):
#         if r < 0 or c < 0 or c >= COLS or r >= ROWS:
#             return 0
#         if (r,c ) in visited:
#             return 0
#
#         visited.add((r,c))
#         if board[r][c] == "^":
#             return dfs(r + 1, c + 1) + dfs(r + 1, c - 1) + 1
#         else:
#             return dfs(r+1, c)
#
#     for i in range(COLS):
#         if board[0][i] == "S":
#             print(dfs(0, i))

# PART 2
from functools import cache

if __name__ == "__main__":
    f = open('input.txt', 'r')
    # f = open('test.txt', 'r')

    board = [s.strip() for s in f.readlines()]
    f.close()

    ROWS, COLS = len(board), len(board[0])

    visited: dict[tuple[int,int], int]= {}

    @cache
    def dfs(r: int, c:int) -> int:
        if r < 0 or c < 0 or c >= COLS:
            return 0
        if (r, c) in visited:
            return visited[(r,c)]
        if r >= ROWS:
            return 1
        if board[r][c] == "^":
            return dfs(r + 1, c + 1) + dfs(r + 1, c - 1)
        else:
            return dfs(r+1, c)

    for i in range(COLS):
        if board[0][i] == "S":
            print(dfs(0, i))
            break
