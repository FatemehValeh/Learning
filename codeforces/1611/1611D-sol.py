def weight(n):
    b = [None] * (n + 1)
    b[1:] = [int(j) for j in input().split()]
    p = [None] * (n + 1)
    p[1:] = [int(k) for k in input().split()]
    distance = [None] * (n + 1)
    distance[1:] = [-1] * n
    if p[1] != b[p[1]]:  # root must be the first element in permutation
        print("-1")
        return
    distance[p[1]] = 0
    for ii in range(2, n+1):
        if distance[b[p[ii]]] == -1:
            print("-1")
            return
        distance[p[ii]] = distance[p[ii - 1]] + 1
    for jj in range(1, n+1):
        print(distance[jj] - distance[b[jj]], end=" ")
    print()


t = int(input())
for i in range(t):
    number = int(input())
    weight(number)

