'''
[임시 반장 정하기]
1~5학년까지 같은 반이었던 사람이 가장 많은 학생 -> 임시 반장
몇 반에 속했었는지를 표로 만듦

5
0) 2  3   1   7  3
1) 4  1   9  '6' 8
2) 5 '5' '2'  4  4
3) 6 '5' '2' '6' 7
4) 8  4  '2'  2  2
'''
n = int(input())

d = {}
for i in range(n):
    d[i] = list(map(int, input().split()))

answer = 0
cnt = 0
who = set()
for i in range(n):  # 0 1 2 3 4
    for ilist in zip(*d.values()):  # (2, 4, 5, 6, 8)
        for j in range(len(ilist)):
            if i != j and ilist[i] == ilist[j]:
                who.add(j)  # 0-indexed
        print(i, list(who))
        if len(who) > cnt:
            cnt = len(who)
            answer = i
    who = set()

print(answer+1)
