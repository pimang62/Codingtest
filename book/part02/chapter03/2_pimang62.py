n, m =map(int, input().split())

min_values = []

for i in range(n):
    data = list(map(int, input().split()))      # 매 행마다 입력받음
    min_values.append(min(data))                # data.min() 안 됨!

print(max(min_values))      # 가장 작은 수들 중 가장 큰 수
