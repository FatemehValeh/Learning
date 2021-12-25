from collections import deque


def solve():
    _ = input()
    n, k = [int(x) for x in input().split()]
    color = [-1 for x in range(n)]
    queue = deque()
    friends = [int(y) - 1 for y in input().split()]
    for friend in friends:
        color[friend] = 0
        queue.append(friend)

    color[0] = 1
    queue.append(0)

    vertices = [[] for x in range(n)]
    for i in range(n - 1):
        a, b = [int(x) - 1 for x in input().split()]
        vertices[a].append(b)
        vertices[b].append(a)

    while queue:
        item = queue[0]
        queue.popleft()
        for room in vertices[item]:
            if color[room] == -1:
                color[room] = color[item]
                queue.append(room)

    for m in range(1, n):
        if len(vertices[m]) == 1 and color[m] == 1:
            print("yes")
            return
    print("no")


t = int(input())
for c in range(t):
    solve()
