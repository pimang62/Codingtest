"""
떡 자르기
N개의 떡이 다양한 정수 길이로 존재한다. 여기서 절단기의 높이 h를 조정하고 잘라서 길이 M만큼의 떡을 얻고 싶다. 이때 떡은 반드시 하나로 이어질 필요는 없다.
절단기의 위에서 아래로 떡이 내려오게 된다. 이때 맞춰야 하는 절단기 길이 h를 구하는 프로그램을 작성하시오

입력:
N M
[떡 길이 리스트]

예시:
4 6
19 15 10 17

출력:
15
"""

# 이진탐색으로 적절한 길이 찾기 (파라메트릭 서치)

# 입력받기
n, m = map(int, input().split())
array = list(map(int, input().split()))

# 이진탐색 함수 작성
def binary_search(array, target, start, end):
    # start가 end보다 작을때만 루프 순회
    while start <= end:
        # mid (떡 자를 길이) 구하기
        mid = (start + end) // 2
        total_dduck_len = 0
        for i in array:
            total_dduck_len += (i - mid) if (i - mid) > 0 else 0
        # mid 만큼 잘라서 M을 얻었다면 mid 리턴
        if total_dduck_len == target:
            return mid
        # mid만큼 잘랐는데 M보다 길게 잘렸다면 오른쪽으로 진입 (start = mid + 1)
        elif total_dduck_len > target:
            start = mid + 1
        # mid만큼 잘랐는데 M보다 덜 잘렸다면 왼쪽 진입 (end = mid - 1)
        elif total_dduck_len < target:
            end = mid - 1
    # 루프 빠져나오면 None 출력
    return None

result = binary_search(array, m, 0, max(array))
print(result)