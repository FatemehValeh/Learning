t = int(input())
for i in range(t):
    n, d = map(int, input().split())
    array = [int(entry) for entry in input().split()]
    visited = [False for j in range(n)]
    block_size = 0  # number of ones in a block
    res = 0  # final result
    max_block_size = 0
    fail = False
    for idx in range(n):
        if visited[idx]:
            continue
        block_idx = idx
        block_size = 0
        max_block_size = 0
        pref, iterations = 0, 0
        while True:
            visited[block_idx] = True
            if array[block_idx] == 1:
                block_size += 1
                if iterations == pref:
                    pref += 1
            else:
                max_block_size = max(max_block_size, block_size)
                block_size = 0
            block_idx = (block_idx + d) % n
            iterations += 1
            if block_idx == idx:
                break
        if iterations != pref:
            max_block_size = max(max_block_size, pref + block_size)
        else:
            fail = True
            break

        res = max(res, max_block_size)
    if fail:
        print("-1")
    else:
        print(res)
