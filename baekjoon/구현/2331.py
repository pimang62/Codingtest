'''
[반복수열]
- D[1] = A
- D[n] = D[n-1]의 각 자리수 ** P

예를 들어 A=57, P=2일 때, 
수열 D는 [57, 74(=5^2+7^2=25+49), 65, 61, 37, 58, 89, 145, 42, 20, 4, 16, 37, …]

반복되는 걸 제외한 수열 반환 [57, 74, 65, 61]
'''
A, P = map(int, input().split())

answer = [A] 
while True:
    num = 0
    for s in str(answer[-1]):
        num += int(s)**P
    if num in answer:
        idx = answer.index(num)
        break
    answer.append(num)

print(len(answer[:idx]))