# PART 1
import heapq
import ast
from collections import deque
import math

if __name__ == "__main__":
    f = open('input.txt', 'r')
    # f = open('test.txt', 'r')

    lines = [s.strip().split(" ") for s in f.readlines()]
    f.close()


    def bfs(goal, masks):
        # print("Start", goal, masks)
        q = deque([(0, 0)])

        visited = {0}

        while q:
            cur, moves = q.pop()
            # print(cur, moves)

            if cur == goal:
                return moves
            
            for mask in masks:
                nxt = cur ^ mask
                # print("next", nxt)

                if nxt not in visited:
                    visited.add(nxt)
                    q.appendleft((nxt, moves + 1))
        return 0

    out = 0
    for line in lines:
        goal = 0
        for i, c in enumerate(line[0][1:-1]):
            if c == '#':
                goal |= 1 << i

        m = ast.literal_eval(f"[{",".join(line[1:-1])}]")

        masks = []

        for v in m:
            mask = 0
            if isinstance(v, int):
                mask |= 1 << v
            else:
                for j in v:
                    mask |= 1 << j

            masks.append(mask)
        out += bfs(goal, masks)


    print(out)




# PART 2
