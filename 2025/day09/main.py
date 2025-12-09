# PART 1
# import heapq
# import math
#
# if __name__ == "__main__":
#     f = open('input.txt', 'r')
#     # f = open('test.txt', 'r')
#
#     lines = [s.strip() for s in f.readlines()]
#     corners = [[int(i) for i in line.split(",")] for line in lines]
#     f.close()
#
#
#     def get_area(u, v):
#         return (abs(u[0] - v[0]) + 1) * (abs(u[1] - v[1]) + 1)
#
#     maxArea = 0
#     for i in range(len(corners)):
#         for j in range(i + 1, len(corners)):
#             maxArea = max(maxArea, get_area(corners[i], corners[j]))
#
#     print(maxArea)
#             




# PART 2

# Learnt from Boojum on Reddit

# Invalid only if it intersects the current box
import itertools

if __name__ == "__main__":
    f = open('input.txt', 'r')
    # f = open('test.txt', 'r')

    lines = [s.strip() for s in f.readlines()]
    corners = [[int(i) for i in line.split(",")] for line in lines]
    # add index 0 to the end for pairwise looping
    looped = corners + [corners[0]]
    f.close()


    def get_area(u, v):
        return (abs(u[0] - v[0]) + 1) * (abs(u[1] - v[1]) + 1)

    maxArea = 0
    # loops through all combinations with better efficiency
    for [x1, y1], [x2, y2] in itertools.combinations(corners, 2):
        mx1, mx2 = min(x1,x2), max(x1,x2)
        my1, my2 = min(y1,y2), max(y1,y2)
        # loops throuhg the pairs that are next to each other
        for [lx1,ly1], [lx2, ly2] in itertools.pairwise(looped):
            if not (max(lx1,lx2) <= mx1 or mx2 <= min(lx1,lx2) or
                    max(ly1,ly2) <= my1 or my2 <= min(ly1,ly2)):
                break
        else:
            a = get_area([x1,y1], [x2,y2])
            if a > maxArea:
                maxArea = a

    print(maxArea)
            
