# PART 1
# import heapq
# from math import sqrt
# import math
#
# if __name__ == "__main__":
#     f = open('input.txt', 'r')
#     # f = open('test.txt', 'r')
#
#     lines = [s.strip() for s in f.readlines()]
#     boxes = [[int(i) for i in line.split(",")] for line in lines]
#     f.close()
#
#     parent = [i for i in range(len(boxes))]
#     rank = [1] * len(boxes)
#
#     def distance(x, y):
#         return sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 + (x[2] - y[2]) ** 2)
#
#     allDistance = []
#     for i in range(len(boxes)):
#         for j in range(i+1, len(boxes)):
#             heapq.heappush(allDistance, (distance(boxes[i], boxes[j]), i, j))
#
#     def find(cur):
#         if parent[cur] == cur:
#             return cur
#         parent[cur] = find(parent[cur])
#         return parent[cur]
#
#     def union(x, y):
#         px = find(x)
#         py = find(y)
#
#         if px == py:
#             return False
#         else:
#             if rank[px] < rank[py]:
#                 px, py = py, px
#
#             parent[py] = px
#             rank[px] += rank[py]
#
#             return True
#         
#
#     i = 0
#     max_i = 1000
#
#     while allDistance and i < max_i:
#         distance, x, y = heapq.heappop(allDistance)
#
#         # print(distance, boxes[x], boxes[y])
#
#         i += 1
#         union(x, y)
#
#     roots = set([find(x) for x in range(len(boxes))])
#     # print(roots)
#     # print(rank)
#     # print(parent)
#     top3 = sorted([rank[i] for i in roots],reverse=True)[:3]
#     # print(top3)
#     print(math.prod(top3))


# PART 2

import heapq
from math import sqrt
import math

if __name__ == "__main__":
    # f = open('input.txt', 'r')
    f = open('test.txt', 'r')

    lines = [s.strip() for s in f.readlines()]
    boxes = [[int(i) for i in line.split(",")] for line in lines]
    f.close()

    parent = [i for i in range(len(boxes))]
    rank = [1] * len(boxes)

    def distance(x, y):
        return sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 + (x[2] - y[2]) ** 2)

    allDistance = []
    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
            heapq.heappush(allDistance, (distance(boxes[i], boxes[j]), i, j))

    def find(cur):
        if parent[cur] == cur:
            return cur
        parent[cur] = find(parent[cur])
        return parent[cur]

    def union(x, y):
        px = find(x)
        py = find(y)

        if px == py:
            return False
        else:
            if rank[px] < rank[py]:
                px, py = py, px

            parent[py] = px
            rank[px] += rank[py]

            return True
        

    num_sets = len(boxes)
    last_x, last_y = None, None

    while allDistance and num_sets > 1:
        distance, x, y = heapq.heappop(allDistance)

        # print(distance, boxes[x], boxes[y])

        if union(x, y):
            last_x = x
            last_y = y
            num_sets -= 1
    if last_x and last_y:
        print(boxes[last_y][0] * boxes[last_x][0])
    else:
        print("Its none bruh")

