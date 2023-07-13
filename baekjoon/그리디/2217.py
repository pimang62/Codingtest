'''
[로프]
n개의 로프가 주어진다.
각 로프가 버틸 수 있는 최대 중량이 주어진다.
여러 개의 로프를 병렬로 연결하면 각 로프에 걸리는 중량을 나눌 수 있다.
ex. k개의 로프로 중량 w를 들어올릴 때, 모두 고르게 w/k만큼 중량이 걸린다.
이 로프들을 이용하여 들어올릴 수 있는 최대 중량?
모든 로프를 사용해야 할 필요는 없다.
'''

n = int(input())

ropes = []
for _ in range(n):
    ropes.append(int(input()))

ropes.sort(reverse=True)

mass = 0
for i in range(len(ropes)):
    if mass <= ropes[i]*(i+1):
        mass = ropes[i]*(i+1)

print(mass)
    

    