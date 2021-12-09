def check(field, n, m):
    for i in range(n):
        for j in range(m):
            if field[i][j] == '*':
                return False
    return True

t = int(input())
for p in range(t):
    n, m, k = [int(n) for n in input().split()]
    field = [['.' for j in range(m)] for i in range(n)]
    for i in range(n):
        field[i] = list(input())
    
    last = n - 1
    start = -1
    for i in range(n-1, -1, -1):
        for j in range(0 , m):
            if field[i][j] == '.':
                continue
            len = 0
            while i - len > 0 and j - len > 0 and j + len + 1 < m :
                if field[i - len - 1][j - len - 1] == '.' or field[i - len - 1][j + len + 1] == '.':
                    break
                len += 1 
            if len >= k:
                for p in range(len+1):
                    field[i - p][j - p] = '-'
                    field[i - p][j + p] = '-'

    print("YES") if check(field, n, m)  else print("NO")