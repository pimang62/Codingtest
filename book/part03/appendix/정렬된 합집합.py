'''
정렬되어 있는 2개의 리스트
모든 원소를 합집합으로 한 정렬 결과 계산

- 병합 정렬(Merge Sort) 알고리즘에 사용됨
- O(N+M)

'''
n, m = 3, 4
a = [3, 5, 1]
b = [6, 4, 8, 2]

# 정렬시키기
a.sort()
b.sort()

# 정렬된 배열을 담을 리스트
result = [0] * (n+m)

# index : a[i], b[j], result[k]
i = j = k = 0

while i < n or j < m or k < (n+m):
    # a 원소가 처리되어야 할 경우 
    # 1. b의 원소보다 작을 때
    # 2. b의 모든 원소는 이미 다 처리되었을 때
    if (i < n and a[i] <= b[j]) or j >= m:
        result[k] = a[i]
        i += 1
    # b 원소가 처리되어야 할 경우
    else:
        result[k] = b[j]
        j += 1
    # retult index 1씩 증가
    k += 1

print(*result)