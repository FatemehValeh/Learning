INF = 1000000000
t = int(input())
for i in range(t):
    size = int(input())
    array = [int(j) for j in input().split()]
    max_item = max(array)
    dp = [[INF for k in range(2 * max_item + 1)] for m in range(size + 1)]
    # place 0 segment
    dp[0][0] = 0
    for idx, item in enumerate(array):
        for j in range(2 * max_item + 1):
            if dp[idx][j] == INF:
                continue
            # go left
            new_end = max(0, j - item)
            dp[idx + 1][new_end] = min(dp[idx + 1][new_end], dp[idx][j] + max(0, item - j))
            if j + item < len(dp[idx + 1]):
                # go right
                new_end = j + item
                dp[idx + 1][new_end] = min(dp[idx + 1][new_end], max(dp[idx][j], j + item))

    answer = INF
    for p in range(2 * max_item + 1):
        answer = min(answer, dp[size][p])
    print(answer)
