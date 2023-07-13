def solution(n, lost, reserve):
    student = [_ for _ in range(1, n+1)]
    array = [1] * n
    for i in student :
        if i in reserve and i in lost :
            array[i-1] = 1
        elif i in lost:
            array[i-1] = 0
        elif i in reserve :
            array[i-1] = 2

    for j in range(len(array)):
        if array[j] == 0:
            if array[j-1] == 2 :
                array[j-1], array[j] = 1, 1
                if array[j] == 0:
                    if array[j+1] == 2 :
                        array[j], array[j+1] = 1, 1

    count = 0
    for k in array:
        if k != 0:
            count += 1

    return count

print(solution(5, [2, 4], [1, 3, 5]))       # 5
print(solution(5, [2, 4], [3]))             # 4
print(solution(3, [3], [1]))                # 2
print(solution(4, [1, 3], [1, 2]))          # 4
print(solution(4, [2, 3], [1, 2]))          # 3
        