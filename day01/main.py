

if __name__ == "__main__":
    f = open('input.txt', 'r')
    count = 0
    curr = 50
    for line in f.readlines():

        dir = line[0]
        num = int(line[1:])
        num %= 100
        print(dir ,num)

        if dir == 'L':
            curr = curr - num
            if curr < 0:
                curr = 100 + curr
        else:
            curr = (curr + num) % 100

        print(curr)
        if curr == 0:
            count += 1
    f.close()
    print(count)

