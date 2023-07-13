n = 5  # list 원소의 수
m = 5  # 찾고자 하는 부분합

n_list = [1, 2, 3, 2, 5]

cnt = 0 
num = 0

# end 지점 0으로 초기화
ed = 0

# num >= m 이 되면 st가 하나씩 증가
for st in range(n):
    # 부분합 num이 m을 넘어설 떄까지
    while num < m and ed < n:
        num += n_list[ed]
        ed += 1
    if num == m:
        cnt += 1
    # 제일 첫 번째 들어간 값 빼기
    num -= n_list[st]
        
print(cnt)
