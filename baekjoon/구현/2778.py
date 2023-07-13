'''
[부녀회장이 될테야]
각 층의 사람들을 불러 모아 반상회 주최
“a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 
사람들의 수를 합한 만큼 데려와 살아야 한다”

아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다

양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지?
각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

입력)
t = int(input())

'''
t = int(input())

for _ in range(t):
    k = int(input())    # 1층
    n = int(input())    # 3호
    
    d = [ [0]*(n+1) for _ in range(k+1) ]      # +1
    d[0] = [ i for i in range(n+1) ]    # 초기화
    
    for i in range(1, k+1):
        for j in range(n+1):
            d[i][j] = sum(d[i-1][:j+1])
    
    print(d[k][n])

