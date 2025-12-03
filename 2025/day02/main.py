# PART 1
# if __name__ == "__main__":
#     f = open('input.txt', 'r')
#     # f = open('test.txt', 'r')
#     line = f.readline()
#     f.close()
#
#     invalid_sum = 0
#     for ids in line.split(","):
#         vals = ids.split("-")
#         first = vals[0]
#         last = vals[1]
#         for i in range(int(first), int(last) + 1):
#             curr = str(i)
#             if curr[:len(curr)//2 ] == curr[len(curr)//2:]:
#                 invalid_sum += i
#
#     print(invalid_sum)


# PART 2
if __name__ == "__main__":
    f = open('input.txt', 'r')
    # f = open('test.txt', 'r')
    line = f.readline()
    f.close()

    invalid_sum = 0
    for ids in line.split(","):
        vals = ids.split("-")
        first = vals[0]
        last = vals[1]
        for i in range(int(first), int(last) + 1):
            curr = str(i)
            for j in range(1,len(curr)//2 + 1):
                mult = len(curr) // j
                multiple = curr[:j] * mult
                if len(multiple) == len(curr) and multiple == curr:
                    # print(curr, multiple, mult, len(curr))
                    invalid_sum += i
                    break


    print(invalid_sum)
