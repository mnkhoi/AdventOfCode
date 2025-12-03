# ===== PART 1 =====

# if __name__ == "__main__":
#     f = open('input.txt', 'r')
#     count = 0
#     curr = 50
#     for line in f.readlines():
#
#         dir = line[0]
#         num = int(line[1:])
#         num %= 100
#         print(dir ,num)
#
#         if dir == 'L':
#             curr = curr - num
#             if curr < 0:
#                 curr = 100 + curr
#         else:
#             curr = (curr + num) % 100
#
#         print(curr)
#         if curr == 0:
#             count += 1
#     f.close()
#     print(count)

# ===== PART 2 =====

if __name__ == "__main__":
    f = open('input.txt', 'r')
    # f = open('test.txt', 'r')
    count = 0
    curr = 50
    for line in f.readlines():

        dir = line[0]
        num = int(line[1:])
        print(count)
        count += num // 100
        print(count)
        num %= 100

        temp = curr
        if dir == 'L':
            curr = curr - num
            if curr < 0:
                curr = 100 + curr
                count += 1 if curr != 0 and temp != 0 else 0
        else:
            curr += num
            if curr > 99:
                curr %= 100
                count += 1 if curr != 0 and temp != 0 else 0

        print(curr)
        if curr == 0:
            count += 1
    f.close()
    print(count)
