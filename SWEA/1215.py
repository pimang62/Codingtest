'''
[회문1]

'''
T = 10
for t in range(1, T+1):
    n = int(input())
    cnt = 0  # 회문의 개수

    def check(string):  # like pelindrom
        for k in range(len(string)//2):
            if string[k] != string[len(string)-1-k]:
                return False
        return True

    graph = []
    for i in range(8):  # 입력 받자마자 행별로 찾기
        row = input()
        for j in range(0, 8-n+1):
            if check(row[j:j+n]):
                cnt += 1
        graph.append(row)

    for j in range(8):  # 열별로 찾기
        candi = ''
        idx = 0  # 행 인덱스
        d = 0  # 0, 1, 2, 3
        while idx < (8-n+1):
            candi += graph[idx+d][j]
            if len(candi) == n:
                if check(candi):
                    cnt += 1
                candi = ''  # 초기화
                idx += 1
                d = 0
            else:
                d += 1

    print(f'#{t} ' + str(cnt))