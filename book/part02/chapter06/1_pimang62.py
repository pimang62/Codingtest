
''' 선택 정렬 '''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i
    # 인덱스 바꾸기
    for j in range(i+1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
    # 값 바꾸기 : 스와프(swap)
    array[i], array[min_idx] = array[min_idx], array[i] 

print(array)



''' 삽입 정렬 '''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# i 1부터 시작
for i in range(1, len(array)):
    # i부터 역순으로 비교
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        # 자기보다 작은 숫자가 앞에 있으면 멈춤
        else :
            break
print(array)



''' 퀵 정렬 '''

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 함수로 들어오는 array 원소가 1개라면 
    # -> 정렬 마무리 된 상황
    if len(array) <= 1:
        return array
    
    pivot = array[0]    # pivot = 첫 번째 원소
    tail = array[1:]    # tail = pivot을 제외한 나머지

    left_side = [x for x in tail if x <= pivot]     # pivot보다 작은 원소들
    right_side = [y for y in tail if y > pivot]     # pivot보다 큰 원소들

    # 재귀문
    quick_sort(left_side)   # print(quick_sort(left_side)) -> return array !
    quick_sort(right_side)  # type(quick_sort()) -> list 

    result = quick_sort(left_side) + [pivot] + quick_sort(right_side)

    return result

print(quick_sort(array))



''' 계수 정렬 '''

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# array 안의 모든 범위를 담을 수 있는 list
# 0으로 초기화
count = [0] * (max(array)+1)

for i in range(len(array)):
    # array[0] -> 7, count[7]
    count[array[i]] += 1

# 각 숫자별 기록 정보 확인 -> 인덱스가 곧 값이 됨!
# count = [2, 1, 2, ...] -> 0이 2번, 1이 1번 ...
for j in range(len(count)):
    # 해당 인덱스(값)을 count에 적힌 횟수만큼 출력
    for k in range(count[j]):
        print(j, end=' ')
