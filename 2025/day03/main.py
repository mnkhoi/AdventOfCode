
# PART 1
# if __name__ == "__main__":
#     f = open('input.txt', 'r')
#     # f = open('test.txt', 'r')
#     summed = 0
#     for line in f.readlines():
#         line = line.strip()
#         l, r = 0, 1 
#         largest = int(line[:2])
#         while r < len(line):
#             l_int, r_int = int(line[l]) , int(line[r])
#
#             number = int(line[l] + line[r])
#             largest = max(largest, number)
#
#             if r_int > l_int:
#                 l = r 
#             r += 1
#         print(largest)
#         summed += largest
#     f.close()
#
#     print(summed)

# PART 2
# Very Very inefficient solution due to backtracking
# if __name__ == "__main__":
#     f = open('input.txt', 'r')
#     # f = open('test.txt', 'r')
#     summed = 0
#     for line in f.readlines():
#         line = line.strip()
#
#         possible = 0
#         def dfs_check(i, num_left, curr):
#             global possible
#             if num_left > len(line) - i:
#                 return 
#
#             if num_left == 0:
#                 possible = max(possible, curr)
#                 return 
#
#
#             # print(curr)
#             curr = int(str(curr) + line[i])
#             dfs_check(i+1, num_left - 1, curr)
#             curr = str(curr)[:-1]
#             dfs_check(i+1, num_left, curr)
#             return
#         dfs_check(0, 12, "")
#         # print(possible)
#         summed += possible
#     f.close()
#
#     print(summed)

# Monotonic Stack 
# Answer with help from Reddit using monotonic stack.
if __name__ == "__main__":
    f = open('input.txt', 'r')
    # f = open('test.txt', 'r')
    summed = 0
    for line in f.readlines():
        line = line.strip()

        stack = []

        for i in range(len(line)):
            digit = int(line[i])

            while stack and stack[-1] < digit and len(stack) + (len(line) - i) > 12:
                stack.pop()

            if len(stack) < 12:
                stack.append(digit)

        # print(possible)
        summed += int("".join(map(str, stack)))
    f.close()

    print(summed)
