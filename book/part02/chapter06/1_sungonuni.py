
"""
선택정렬: 가장 작은 원소를 선택하여 맨 앞으로 배치한다.
시간복잡도: O(n^2)
"""

array = [7,5,9,0,3,1,6,2,4,8]

# 리스트의 각 원소 순회, i는 최소 원소의 인덱스라고 가정
for i in range(len(array)):
    min_idx = i
    # i 이후 원소 순회, j의 원소가 i의 원소보다 작다면, j는 최소 원소의 인덱스임.
    for j in range(i+1, len(array)):
        if array[j] < array[min_idx]:
            min_idx = j
    # 가장 최소값인 array[min_idx]를 array[i]와 바꿈 
    array[min_idx], array[i] = array[i], array[min_idx]

print(array)

"""
삽입정렬: 정렬이 안 된 부분의 가장 왼쪽에 위치한 원소를 정렬 된 부분의 적절한 곳에 삽입한다.
시간복잡도: O(n^2)
"""

array = [7,5,9,0,3,1,6,2,4,8]

# 좌측 1개 원소를 정렬이 된 부분, 나머지 원소들을 정렬이 안 된 부분으로 가정
# 정렬이 된 부분의 윈도우 크기를 1부터 늘려감
for i in range(1, len(array)):
# 정렬이 된 부분의 원소를 끝에서부터 순회함
    for j in range(i, 0, -1):
        # 정렬이 된 부분의 가장 마지막 원소가 그 전 원소보다 작다면 스와프 (왼쪽으로 이동시킴)
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        # 만약 크다면 멈춤
        else:
            break
    
print(array)

"""
퀵정렬: 피벗과 포인터 두개가 있다. 피벗은 가장 좌측 원소이고, 포인터 두 개는 나머지 원소들의 가장 좌-우측 원소를 가르키고 있다.
1. 좌측 포인터는 피벗보다 큰 원소를 가르키도록 오른쪽으로 이동하고, 우측 포인터는 피벗보다 작은 원소를 가르키도록 왼쪽으로 이동한다.
만약 해당 조건이 만족한다면, 두 포인터가 가르키고 있는 원소들을 스와프 한다.
2. 좌측 포인터와 우측 포인터가 교차한다면, 해당 과정을 종료하고 그 사이에 피벗을 이동시킨다.
시간복잡도: O(NlogN)
"""

array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):

    # 만약 리스트 길이가 1보다 작거나 같다면 탈출
    if len(array) <= 1:
        return array
    
    # 피벗은 리스트의 가장 좌측 원소
    pivot = array[0]
    # 테일은 리스트의 피벗을 제외한 원소 리스트
    tail = array[1:]

    # 포인터 교환 및 교차 완료, 왼쪽에 피벗보다 작은 원소들이 배열됨
    left_side = [x for x in tail if x <= pivot]
    # 포인터 교환 및 교차 완료, 오른쪽에 피벗보다 큰 원소들이 배열됨
    right_side = [x for x in tail if x > pivot]

    # 좌측부분 + 피벗 + 우측부분으로 토탈 배열 어레이 구하기
    return (quick_sort(left_side) + [pivot] + quick_sort(right_side))

print(quick_sort(array))


"""
계수정렬: 빈도수 리스트에 각 원소 별 빈도수를 기록하고, 빈도수 리스트를 순회하며 해당 빈도수만큼 원소를 순차출력
시간복잡도: O(N)
"""

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7,5,9,0,3,1,6,2,4,8]

# 모든 범위를 포함하는 빈도수 리스트 선언
count = [0] * (max(array) + 1)

# 빈도수 리스트에 빈도수 기록
for i in range(len(array)):
    count[array[i]] += 1

# 빈도수 리스트를 순회하며 해당 빈도수 만큼 원소를 출력
sorted_list = []
for i in range(len(count)):
    for j in range(count[i]):
        sorted_list.append(i)

print(sorted_list)