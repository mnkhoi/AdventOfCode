# PART 1
# if __name__ == "__main__":
#     f = open('input.txt', 'r')
#     # f = open('test.txt', 'r')
#
#     # Get the ranges sort then, merge ranges if overlap
#     ranges, fruits = f.read().split("\n\n")
#     ranges = [[int(i.strip()) for i in line.split('-')] for line in ranges.split("\n") if len(line) > 0]
#     fruits = [int(line.strip()) for line in fruits.split("\n") if len(line) > 0]
#     f.close()
#
#     ranges.sort(key=lambda x: x[0])
#     fruits.sort()
#
#     # range_stack = []
#     # i = 0
#     # while i < len(ranges):
#     #     if range_stack and range_stack[-1][1] >= ranges[i][0]:
#     #         print(range_stack[-1], ranges[i] )
#     #         range_stack[-1][1] = ranges[i][1]
#     #     else:
#     #         print(ranges[i])
#     #         range_stack.append(ranges[i])
#     #     i += 1
#     #
#     # count = 0
#     # i = 0
#     # j = 0
#     # print(len(range_stack), len(fruits))
#     # while i < len(fruits) and j < len(range_stack):
#     #     print(range_stack[j], fruits[i])
#     #     if range_stack[j][0] <= fruits[i] <= range_stack[j][1]:
#     #         count += 1
#     #         i += 1
#     #     elif fruits[i] < range_stack[j][0]:
#     #         i += 1
#     #     else:
#     #         j += 1
#
#     count = 0
#     for i in fruits:
#         for j, k in ranges:
#             if j <= i <= k:
#                 count += 1
#                 break
#
#     print(count)
#

# PART 2
if __name__ == "__main__":
    f = open('input.txt', 'r')
    # f = open('test.txt', 'r')

    # Get the ranges sort then, merge ranges if overlap
    ranges, _ = f.read().split("\n\n")
    ranges = [[int(i.strip()) for i in line.split('-')] for line in ranges.split("\n") if len(line) > 0]
    f.close()

    ranges.sort(key=lambda x: x[0])

    range_stack = []
    i = 0
    count = 0
    while i < len(ranges):
        if range_stack and range_stack[-1][1] >= ranges[i][0]:
            print(range_stack[-1], ranges[i] )
            range_stack[-1][1] = max(ranges[i][1], range_stack[-1][1])
        else:
            print(ranges[i])
            range_stack.append(ranges[i])
        i += 1

    for i,  j in  range_stack:
        count += j - i + 1


    print(count)
