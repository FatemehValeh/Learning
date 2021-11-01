from collections import deque
t = int(input())
for i in range(t):
    _ = int(input())
    array = [int(entry) for entry in input().split()]
    answer = deque([])
    answer.append(array[0])
    for item in array[1:]:
        if item > answer[0]:
            answer.append(item)
        else:
            answer.appendleft(item)
            
    print(*answer, sep=' ')