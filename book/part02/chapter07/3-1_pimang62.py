""" 오늘은 떡볶이 떡을 만드는 날이다.
    떡볶이 떡의 길이는 일정하지 않다.

    절단기의 높이(H)를 리스트 내에서 지정한다.
    자르고 남은 떡의 총합이 M이 되는 H의 최댓값을 찾는다.
"""

# 재귀 함수를 이용한 이진 탐색
def binary_research(array, start, end):
    mid = (start + end) // 2  # (0 + 19) // 2 -> 9
    result = []
    for i in range(n):
        if array[i] > mid:
            result.append(array[i] - mid)
        else:
            continue
    if sum(result) == m:
        print(mid)
    # 더한 값이 타겟보다 크면 높이(H) 높여야
    elif sum(result) > m:
        binary_research(array, mid+1, end)
    # 더한 값이 타겟보다 작으면 높이(H) 낮춰야
    else:
        binary_research(array, start, mid-1)

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

start, end = 0, max(array)

binary_research(array, start, end)