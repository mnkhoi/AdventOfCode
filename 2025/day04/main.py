from collections import deque
# PART 1
# if __name__ == "__main__":
#     f = open('input.txt', 'r')
#     # f = open('test.txt', 'r')
#
#     board = [[i for i in line.strip()] for line in f.readlines()]
#     f.close()
#
#     N, M = len(board), len(board[0])
#     print(N, M)
#     directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
#     board_count = {}
#
#     count = 0
#     for i in range(N):
#         for j in range(M):
#             if board[i][j] == '@':
#                 cur = 0
#
#                 for di, dj in directions:
#
#                     mi, mj = di + i, dj + j
#                     if  mi  < 0 or mj < 0 or mi >= N or mj >= M or board[mi][mj] == '.':
#                         continue
#                     cur += 1
#                 if cur < 4:
#                     count += 1
#
#     print(count)

# PART 2
if __name__ == "__main__":
    f = open('input.txt', 'r')
    # f = open('test.txt', 'r')

    board = [[i for i in line.strip()] for line in f.readlines()]
    f.close()

    N, M = len(board), len(board[0])
    print(N, M)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    board_count = [[0] * M for i in range(N)]
    print(len(board_count), len(board_count[0]))

    q = deque()
    count = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == '@':
                cur = 0

                for di, dj in directions:
                    mi, mj = di + i, dj + j
                    if  mi  < 0 or mj < 0 or mi >= N or mj >= M or board[mi][mj] == '.':
                        continue
                    cur += 1
                board_count[i][j] = cur
                if cur < 4:
                    q.appendleft((i, j))

    while q:
        i, j = q.pop()
        if board[i][j] == '.':
            continue

        count += 1
        board[i][j] = '.'
        for di, dj in directions:
            mi, mj = di + i, dj + j
            if  mi  < 0 or mj < 0 or mi >= N or mj >= M or board[mi][mj] == '.':
                continue

            board_count[mi][mj] -= 1
            if board_count[mi][mj] < 4:
                q.appendleft((mi, mj))



    print(count)
