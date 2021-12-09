def check(field, n, m):
    print(field)
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

    for i in range(n):
        print("i:", i)
        i_copy = i
        for j in range(m):
            print("j:", j)
            vert_cor = i 
            horz_cor = j
            downward = 0
            upward = 0
            flag = 1
            while 0 <= i < n and 0 <= j < m and field[i][j] != '.':
                while i + 1 < n and j + 1 < m and field[i+1][j+1] != '.' and flag == 1:
                    i += 1
                    j += 1
                    downward += 1

                y = i
                x = j
                
                while i - 1 >= 0 and j + 1 < m and field[i-1][j+1] != '.' and upward != downward:
                    i -= 1
                    j += 1
                    upward += 1
                
                if downward == upward and downward >= k:
                    down_count = 0
                    up_count = 0
                    while i + 1 < n and j - 1 >= 0 and i + 1 <= y and field[i+1][j-1] != '.':
                        field[i][j] = '-'
                        i += 1
                        j -= 1
                        down_count += 1
                    while i - 1 >= 0 and j - 1 >= 0 and field[i-1][j-1] != '.' and up_count != down_count:
                        field[i][j] = '-'
                        i -= 1
                        j -= 1
                        up_count += 1
                    field[i][j] = '-'
                if x - 1 == horz_cor and y - 1 == vert_cor:
                    i = vert_cor
                    j = horz_cor
                    break
                i = y - 1
                j = x - 1 
                downward -= 1
                upward = 0
                flag = 0
        i = i_copy
        print("*j:", j)
        
    print("YES") if check(field, n, m)  else print("NO")