def max_index(array):
    max_value = max(array)
    return array.index(max_value)

def cyclical_shift(first, last, array):
    if first == last:
        return array
    first_el = array[first]
    curr = first 
    for i in range(last - first):
        array[curr] = array[curr+1]
        curr += 1
    array[last] = first_el
    return array

t = int(input())

for i in range(t):
    n = int(input())
    arr = [int(item) for item in input().split()]
    end = n 
    last_index = n - 1
    answers = [[] for i in range(2)]
    while(last_index):
        current_max_position = max_index(arr[:end])
        if current_max_position != last_index:
            arr[0:end] = cyclical_shift(current_max_position, last_index, arr[0:end])
            answers[0].append(current_max_position + 1)
            answers[1].append(last_index + 1)
        end -= 1
        last_index -= 1
    print(len(answers[0]))
    for i, item in enumerate(answers[0]):
        print(answers[0][i], answers[1][i], "1")

