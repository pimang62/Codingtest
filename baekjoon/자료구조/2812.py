'''
[크게 만들기]
N자리 숫자, 숫자 K개를 지움
얻을 수 있는 가장 큰 수?

앞 자리의 숫자가 클수록 큰 수!
따라서 그리디하게 지워 나감

반례)
6 2
999899

>>> 같은 숫자를 지우지 않게 만들었으면
9999가 아니라 99999가 stack에 쌓이고 cnt=1로 남아 있음
'''
N, K = map(int, input().split())
string = input()
A = [int(n) for n in string]

stack = []
cnt = 0  # 지운 개수
for i in range(N):
    if cnt >= K:
        break
    while stack and stack[-1] < A[i] and cnt < K:
        stack.pop()
        cnt += 1
    stack.append(A[i])

# for loop을 다 돌았으면(i==N-1) 길이가 N-K이어야 함!
print(''.join([str(s) for s in stack])+string[i:] \
    if i < N-1 else ''.join([str(s) for s in stack])[:N-K])