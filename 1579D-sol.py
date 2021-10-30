import heapq as hp

t = int(input())
for i in range(t):
    answers = [[] for i in range(2)]
    n = int(input())
    arr = [int(el) for el in input().split()]
    heap = []
    for i in range(n):
        if arr[i] > 0:
            heap.append((-1 * arr[i], i+1))
    # indexes = list(range(1,n+1))
    # heap = list(zip(arr, indexes))
    while(len(heap) >= 2):
        hp.heapify(heap)
        p1 = hp.heappop(heap)
        p2 = hp.heappop(heap)
        answers[0].append(p1[1])
        answers[1].append(p2[1])
        if p1[0] <= -2:
            hp.heappush(heap, (p1[0]+1, p1[1]))
        if p2[0] <= -2:
            hp.heappush(heap, (p2[0]+1, p2[1]))
    print(len(answers[0]))
    for i, ele in enumerate(answers[0]):
        print(answers[1][i], answers[0][i])
        
        
        
        