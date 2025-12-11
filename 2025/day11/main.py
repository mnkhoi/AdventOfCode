# PART 1

# if __name__ == "__main__":
#     # f = open('input.txt', 'r')
#     f = open('test.txt', 'r')
#
#     lines = [s.strip().split(" ") for s in f.readlines()]
#     f.close()
#
#     adj = {l[0][:-1]: l[1:] for l in lines}
#
#
#     visited = {}
#     def dfs(cur):
#         if cur == "out":
#             return 1
#         if cur not in adj:
#             return 0
#         if cur in visited:
#             return visited[cur]
#
#         visited[cur] = 0
#
#         for nei in adj[cur]:
#             visited[cur] += dfs(nei)
#
#         return visited[cur]
#
#
#     print(dfs("you"))


# PART 2
if __name__ == "__main__":

    f = open('input.txt', 'r')
    # f = open('test2.txt', 'r')

    lines = [s.strip().split(" ") for s in f.readlines()]
    f.close()

    adj = {l[0][:-1]: l[1:] for l in lines}

    def dfs(cur, target, visited = {}):
        # print(cur)
        if cur == target:
            # print(cur, cur_visited)
            return 1
        if cur not in adj:
            return 0
        
        if cur in visited:
            return visited[cur]

        visited[cur] = 0

        for nei in adj[cur]:
            visited[cur] += dfs(nei, target, visited)

        return visited[cur]
    src_dac = dfs("svr", "dac", {})
    dac_fft = dfs("dac", "fft", {})
    fft_out = dfs("fft", "out", {})

    src_fft = dfs("svr", "fft", {})
    fft_dac = dfs("fft", "dac", {})
    dac_out = dfs("dac", "out", {})

    print(src_dac, dac_fft, fft_out, src_fft, fft_dac, dac_out, src_dac * dac_fft * fft_out + src_fft * fft_dac * dac_out)

