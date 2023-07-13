# 성적이 낮은 순서로 학생 출력하기
# sort의 key를 사용


import time
import sys
input = sys.stdin.readline
start = time.time()

N = int(input())
arr = [ list(input().split()) for _ in range(N)]
arr.sort(key=lambda x:x[1])
for name, score in arr:
    print(name, end=' ')

end = time.time()
print('\ntime:', end-start)