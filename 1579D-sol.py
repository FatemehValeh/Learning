import heapq as hp

t = int(input())
for i in range(t):
    answers = [[] for i in range(2)]
    _ = int(input())
    
    heap = [(-1 * int(item), idx + 1) for idx, item in enumerate(input().split()) if int(item) > 0]

    hp.heapify(heap)
    while len(heap) >= 2:
        person1 = hp.heappop(heap)
        person2 = hp.heappop(heap)
        answers[0].append(person1[1])
        answers[1].append(person2[1])
        if person1[0] <= -2:
            hp.heappush(heap, (person1[0]+1, person1[1]))
        if person2[0] <= -2:
            hp.heappush(heap, (person2[0]+1, person2[1]))
    print(len(answers[0]))
    for i, foo in enumerate(answers[0]):
        print(answers[1][i], answers[0][i])
        
        
        
        