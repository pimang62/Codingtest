'''
[바닥 장식]
몇 개의 나무 판자기 필요한지
'-', '|' 인접해 있으면 같은 판자
'''
n, m = map(int, input().split())

graph = []
for _ in range(n):
    row = input()
    graph.append(row)

def check(what):
    if what == '-':
        cnt = 0
        for i in range(n):
            tmp = False  # stack = []
            for j in range(m):
                if tmp and graph[i][j] != what:
                    cnt += 1
                    tmp = False # stack = []
                elif graph[i][j] == what:  # else => not tmp
                    tmp = True # stack.append(what)
            if tmp:
                cnt += 1
        return cnt
    else:  # '|'
        cnt = 0
        for j in range(m):
            tmp = False  # stack = []
            for i in range(n):
                if tmp and graph[i][j] != what:
                    cnt += 1
                    tmp = False # stack = []
                elif graph[i][j] == what:
                    tmp = True # stack.append(what)
            if tmp:
                cnt += 1
        return cnt  

answer = 0
answer += check('-')
answer += check('|')
print(answer)