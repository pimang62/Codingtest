'''
[지능형 기차]
기차 안에 사람이 가장 많을 때의 사람 수?
'''
train = 0
answer = 0  # 최댓값
for _ in range(4):
    out, inn = map(int, input().split())
    train -= out
    train += inn
    answer = max(answer, train)

print(answer)