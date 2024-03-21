'''
[등수 구하기]
100 90 90 80
  1  2  2  4
  
- 등수: nlist.index(score) + count
  
10 9 8 7 6 5 4 3 2 1
 1 2 3 4 5 6 7 8 9 10
'''
n, score, p = map(int, input().split())

if n == 0:  # 0 0 50 예외!
    print(1)
    exit()

nlist = list(map(int, input().split()))

nlist.append(score)
nlist.sort(reverse=True)  # 내림차순

tmp = nlist.index(score)
# 나를 포함한 점수가 P명을 벗어나면
if tmp + nlist.count(score) > p:  
    print(-1)
else:  # 실제 등수
    print(tmp+1)