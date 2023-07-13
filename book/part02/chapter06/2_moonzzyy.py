# 위에서 아래로


import time
import sys
input = sys.stdin.readline
start = time.time()

N = int(input())
arr = [ int(input()) for _ in range(N)]
arr.sort(reverse=True)
print(*arr, sep='\n')

end = time.time()
print('\ntime:', end-start)