'''
[학생 번호]
https://www.acmicpc.net/problem/1235

학생 번호는 0~9, 번호는 다르지만 길이는 같음
뒤에 세 자리만 남겨도 서로 다르게 만들 수 있음

뒤에 k자리만 추려서 남길 때 모든 학생이 서로 다를 최소 k?

2 <= N <= 1000
1 <= 문자열 길이 <= 100
'''
N = int(input())

nlist = []
for _ in range(N):
    nlist.append(input())

length = len(nlist[0])

k = 0
for i in range(length-1, -1, -1):
    flag = True
    bucket = set()
    for num in nlist:
        if num[i:] not in bucket:
            bucket.add(num[i:])
        else:
            flag = False
            break
    if flag:
        break
    k += 1

print(k+1)