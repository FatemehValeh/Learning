t = int(input())
for i in range(t):
    a, b = [int(x) for x in input().split()]
    max_possible = int((a + b) / 4)
    _min = min(a, b)
    groups = 0
    possible_groups = min(max_possible, _min)
    a -= possible_groups
    b -= possible_groups
    remaining = int((a + b) / 2)
    groups = min(remaining, possible_groups)
    print(groups)
