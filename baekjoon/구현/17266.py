'''
[어두운 굴다리]
0~N을 밝히게 가로등 설치
가로등 개수 M개, 위치 x
높이만큼 주위를 비출 수 있음

최소한의 높이로 0~N을 밝히고자
모든 가로등 높이 같음, 정수

높이가 H라면 왼쪽 H, 오른쪽 H 비춤
x는 오름차순, 위치는 중복되지 않음

1 <= N <= 1e5
1 <= M <= N
0 <= x <= N
'''
N = int(input())
M = int(input())
xlist = list(map(int, input().split()))

prev, h = xlist[0], xlist[0]

for x in xlist:
    tmp = x - prev
    if tmp % 2 == 0:  # 절반 높이
        tmp = tmp // 2
    else:
        tmp = tmp // 2 + 1  # 전부 덮어야 하므로 +1
    h = max(h, tmp)
    prev = x

h = max(h, N - xlist[-1])  # 마지막 거리

print(h)

# Binary Search

N, M = int(input()), int(input())
xlist = list(map(int, input().split()))

def binary_search(mid):
    if (xlist[0]-0) > mid:
        return False
    if (N-xlist[-1]) > mid:
        return False
    for i in range(1, len(xlist)):
        if (xlist[i] - xlist[i-1])/2 > mid:
            return False
    return True
    
answer = 0

# def main():
#     global answer
start, end = 0, N
while start <= end:
    mid = (start+end) // 2
    if binary_search(mid):
        end = mid - 1
        answer = mid
    else:
        start = mid + 1
            
# main()

print(answer)