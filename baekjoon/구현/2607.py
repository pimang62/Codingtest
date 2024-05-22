'''
[비슷한 단어]
알파벳 대문자, 2가지 조건
1. 같은 종류의 문자
2. 같은 개수만큼 있음

한 단어에서 한 문자 +, -, 바꿈
=> 같은 구성이면 비슷한 단어!

첫 번째 단어와 비슷한 단어 몇 개?

ex. {D:1, O:1, G:1}
    {G:1, O:1, D:1}
    {G:1, O:1} ok
    {G:1, O:2, D:1}
    {D:1, O:1, L:2}
'''
n = int(input())
target = list(input())

answer = 0

for _ in range(n-1):
    compare = target[:] 
    word = input()
    cnt = 0

    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(compare) < 2:
        answer += 1

print(answer)
