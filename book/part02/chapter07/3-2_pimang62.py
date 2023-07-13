""" 오늘은 떡볶이 떡을 만드는 날이다.
    떡볶이 떡의 길이는 일정하지 않다.

    절단기의 높이(H)를 리스트 내에서 지정한다.
    자르고 남은 떡의 총합이 M이 되는 H의 최댓값을 찾는다.
"""

# 반복문을 이용한 이진 탐색
n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

start, end = 0, array[-1]

result = 0  # 최종 답안 기록
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in array:
        if i > mid :
            # 자른 떡의 길이
            total += (i-mid)
    # 더한 값이 타겟보다 크면 높이(H) 높여야!
    if total > m :
        start = mid + 1
    else:
        result = mid  # 최대 mid 답안 기록
        end = mid - 1

print(result)







