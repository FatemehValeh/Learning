import math
t = int(input())
for i in range(t):
    answer = -1
    number = int(input())
    if (number % 10) % 2 == 0:
        answer = 0
    else:
        digits = int(math.log10(number))
        if int(number / pow(10, digits)) % 2 == 0:
            answer = 1
        else:
            while number > 10:
                number = number % pow(10, digits)
                digits -= 1
                if int(number / pow(10, digits)) % 2 == 0:
                    answer = 2
                    break
    print(answer)
