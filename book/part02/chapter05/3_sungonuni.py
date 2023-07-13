"""
N X M의 얼음틀이 있다. 0인 부분에 음료가 들어갈 수 있고, 1인 부분은 막혀있는 칸이다.
0인 부분이 상하좌우로 붙어있다면 연결된 것으로 간주한다.
이때 얼음틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하라.

예시:
4 5
00110
00011
11111
00000

결과:
3
"""

# N, M 입력받기
n, m = map(int, input().split())

# 얼음틀 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input())))

# dfs 메서드 정의
def dfs(x,y):
    # 만약 범위를 벗어나거나 음료수를 넣을 수 없다면
    if x < 0 or y < 0 or x >= n or y >= m or array[x][y] == 1:
        # False 리턴
        return False
    # 음료수를 넣을 수 있다면
    elif array[x][y] == 0:
        # 음료수 넣을 수 없음 처리
        array[x][y] = 1
        # 상하좌우 순회
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        # True 리턴
        return True
    # 예외처리용 False 리턴
    return False

result = 0
# 얼음틀의 모든 칸을 순회
for i in range(n):
    for j in range(m):
    # 만약 해당 칸에서 dfs를 실행했을 때 True가 뜬다면
        if dfs(i, j) == True:
            # 카운트 하나 증가
            result += 1

print(result)

# dfs 메서드 정의
    # 만약 랜딩포인트가 범위를 벗어났거나 이미 음료가 차 있다면
        # False 리턴
    # 랜딩포인트가 비어있다면
        # 랜딩포인트 음료 넣기 처리
        # 상하좌우 순회
        # True 리턴
    # 예외처리용 False 리턴 