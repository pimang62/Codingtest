n = 5
data = [10, 20, 30, 40, 50]

prefix_sum = [0]

sum_value = 0
for i in range(len(data)):
    # 매 index마다 data 값을 더함
    sum_value += data[i]
    # index 1부터 구간 합을 추가시킴
    prefix_sum.append(sum_value)

l, r = 1, 3
print(prefix_sum[r]-prefix_sum[l-1])