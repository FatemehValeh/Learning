t = int(input())
for i in range(t):
    string = input()
    string_length = len(string)
    num_b = string.count('B')
    print("YES") if (num_b * 2 == string_length) else print("NO")