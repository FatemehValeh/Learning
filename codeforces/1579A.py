def chars_in_list(str):
    num_a = num_b = num_c = 0
    for char in str:
        if (char == 'A'):
            num_a += 1
        if (char == 'B'):
            num_b += 1
        if (char == 'C'):
            num_c += 1
    return num_a, num_b, num_c

def accepted(num_a, num_b, num_c):
    if ((num_a == num_b) and num_c == 0):
        return True
    if ((num_b == num_c) and num_a == 0):
        return True
    if (num_a + num_c == num_b):
        return True
    else:
        return False

t = int(input())

for i in range(t):
    string = list(input())
    num_a , num_b , num_c = chars_in_list(string)
    print("YES") if (accepted(num_a, num_b, num_c))  else print("NO")
    

