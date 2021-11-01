from collections import deque
t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(el) for el in input().split()]
    answer = deque([])
    answer.append(arr[0])
    for j in range (1, n):
        if arr[j] > answer[0]:
            answer.append(arr[j])
        else:
            answer.appendleft(arr[j])
            
    print(*answer, sep=' ')