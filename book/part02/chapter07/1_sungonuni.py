"""
이진탐색코드 (재귀함수)

입력:
N K (N은 원소 개수, K는 타겟 원소)
원소 리스트

예시입력:
10 7
1 3 5 7 9 11 13 15 17 19

출력:
3
"""

# 입력받기

n, k = map(int, input().split())
array = list(map(int, input().split()))

def binary_search_recursion(array, target, start, end):
    # start가 end보다 크다면 무효
    if start > end:
        return None
    # mid 값 설정
    mid = (start + end) // 2
    # 목표가 mid 원소와 같으면 값 반환
    if target == array[mid]:
        return mid
    # 목표가 mid 원소보다 작으면 왼쪽 탐색
    elif target < array[mid]:
        return binary_search_recursion(array, target, start, mid-1)
    # 목표가 mid 원소보다 크면 오른쪽 탐색
    elif target > array[mid]:
        return binary_search_recursion(array, target, mid+1, end)
    
def binary_search_loop(array, target, start, end):
    # start가 end보다 작을때만 루프 실행
    while start <= end:
        # mid 계산
        mid = (start + end) // 2
        # 목표가 mid 원소와 같다면 mid 리턴
        if target == array[mid]:
            return mid
        # 목표가 mid 원소보다 작다면 end는 mid-1
        elif target < array[mid]:
            end = mid - 1
        # 목표가 mid 원소보다 크다면 start는 mid+1
        elif target > array[mid]:
            start = mid + 1
    # 루프 벗어나면 None 리턴
    return None

result = binary_search_recursion(array, k, 0, n-1)
if result == None:
    print("원소 없음")
else:
    print(result)

result = binary_search_loop(array, k, 0, n-1)
if result == None:
    print("원소 없음")
else:
    print(result)