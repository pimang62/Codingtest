'''
[DNA]

A T G C
길이가 같은 "두" DNA
각 위치의 뉴클리오타이드 문자가 다른 것의 "개수"

ex. AGCAT GGAAT : 1-3 = 2

s1, s2, ... sn과의 Hamming Distance 합 비교
Hamming Distance의 합이 가장 작은 DNA "s"(new)
'''
n, m = map(int, input().split())

DNAs = [input() for _ in range(n)]

ACGT = ['A', 'C', 'G', 'T']  # 사전 순(.index(max))

target = ''
distance = 0  # Hamming Distance
for j in range(m):
    a, c, g, t = 0, 0, 0, 0   
    for i in range(n):
        if DNAs[i][j] == ACGT[0]:
            a += 1
        elif DNAs[i][j] == ACGT[1]:
            t += 1
        elif DNAs[i][j] == ACGT[2]:
            g += 1
        else:  # DNAs[i][j] == ACGT[3]
            c += 1
    cnt_list = [a, t, g, c]  # [0, 1, 3, 1]
    most_value = ACGT[cnt_list.index(max(cnt_list))]
    target += most_value  # G
    
    distance += sum(cnt_list) - max(cnt_list)
    # for i in range(n):
    #     if DNAs[i][j] != most_value:
    #         distance += 1

print(target)
print(distance)