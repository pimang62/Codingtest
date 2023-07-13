n, m, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort(reverse=True)      # 내림차순 
first = num[0]              # 가장 큰 수 
second = num[1]             # 두 번째로 큰 수

result = 0 

while True :                # 계속 반복
    for i in range(k) :     # 더할 수 있는 최대 횟수 동안
        if m == 0 :         # 제어문
            break
        result += first     # 가장 큰 수 더하기
        m -= 1              # 더할 횟수 차감
    if m == 0 :             # 제어문 
        break
    result += second        # 두 번째로 큰 수 한 번 더하기
    m -= 1                  # 더할 횟수 차감

print(result)
