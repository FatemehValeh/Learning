t = int(input())
for i in range(t):
    n = int(input())
    array = [int(x) for x in input().split()]
    if array[0] != n and array[-1] != n:
        print("-1")
    else:
        for item in reversed(array):
            print(item, end=" ")
        print()