'''
[세로읽기]
A A B C D D
a f z z 
0 9 1 2 1
a 8 E W g 6
P 5 h 3 k x

Aa0aPAf985Bz1EhCz2W3D1gkD6x

'A-Z', 'a-z', '0-9'
5줄 최대 15개의 글자
'''
def cleaning(S):
    answer = ''
    for j in range(15):
        for i in range(5):
            if S[i][j] == 0:
                continue
            answer += S[i][j]
    return answer
    
S = []
for _ in range(5):
    string = input()
    row = [s for s in string] + [0]*(15-len(string))
    S.append(row)

print(cleaning(S))
