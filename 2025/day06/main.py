# PART 1
import re
import math

# if __name__ == "__main__":
#     # f = open('input.txt', 'r')
#     f = open('test.txt', 'r')
#
#     # Get the ranges sort then, merge ranges if overlap
#     lines = f.readlines()
#     lines.reverse()
#     f.close()
#
#     sign = lines[0]
#     lines = lines[1:]
#     SPACE = r"\s+"
#
#     sign = re.split(SPACE, sign)
#     out = [0 if s == "+" else 1 for s in sign if s != ""]
#
#     for line in lines:
#         nums = [s for s in re.split(SPACE, line) if s != ""]
#         for i in range(len(out)):
#             if sign[i] == "+":
#                 out[i] += int(nums[i])
#             else:
#                 out[i] *= int(nums[i])
#
#     print(sum(out))


# PART 2
if __name__ == "__main__":
    f = open('input.txt', 'r')
    # f = open('test.txt', 'r')

    # Get the ranges sort then, merge ranges if overlap
    lines = [l.strip('\n') for l in f.readlines()]
    f.close()

    sign = lines[-1]
    lines = lines[:-1]
    REGEX = r"([+|*])(\s+|$)"
    NUM = r"(\d+)"

    # Take in account space to split the input and the space to parse
    sign = [(s[0], len(s[1])) for i, s in enumerate(re.findall(REGEX, sign))]
    sign[-1] = (sign[-1][0], sign[-1][1] + 1)
    number_ranges = []
    for i, s in enumerate(sign):
        start = number_ranges[-1][1] + 1 if number_ranges else 0
        end = start + s[1] 
        number_ranges.append((start,end))
    print(number_ranges)
    out = [[""] * (s[1]) for s in sign]
    print(len(sign), sign)

    for line in lines:
        nums = [line[start: end] for start,end in number_ranges]
        print(len(nums), nums)
        for i, num in enumerate(nums):
            for j in range(len(num)):
                if num[j] != " ":
                    out[i][j] += num[j]
    
    summation = 0
    for i, s in enumerate(sign):
        o = 0
        print(i, s, out[i])
        if s[0] == "+":
            o = sum(map(int, out[i]))
            print(o)
        else:
            o = math.prod(map(int, out[i]))
            print(o)
        print(out[i], s, o)

        summation += o
            
    print(summation)
