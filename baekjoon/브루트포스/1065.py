'''
[한수]
양의 정수 x 각 자리가 등차수열 : 한수
1보다 크거나 같고 n보다 작거나 같은 한수의 개수?
n <= 1000

'''
num = int(input())
result = 0

# 1부터 num까지 모든 번호에 대하여
for n in range(1, num+1):
    string = str(n)

    # 초기화
    check = [False for i in range(len(string))]   # '123' : 012

    # 초깃값
    sub = 1e9
    for i in range(len(string)-1):
        tmp = int(string[i]) - int(string[i+1])
        if sub == 1e9: sub = tmp	# 초기 차이 기록
        if sub == tmp: check[i] = True
        else: break
    
    # 한 자리 숫자라면 
    if sub == 1e9: check[0] = True

    flag = True
    for i in range(len(check)-1):   # 맨 마지막 check 제외
        if check[i] == False:
            flag = False
            break
    
    if flag:
        result += 1

print(result)