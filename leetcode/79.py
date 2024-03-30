'''
[Word Search]

'''
from typing import List
from copy import deepcopy

"""
class Solution:  # 시간 초과
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        L = len(word)

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        def in_range(x, y):
            return 0 <= x < m and 0 <= y < n
    
        def dfs(idx, path):
            if idx >= L:
                return True

            x, y = path[-1]
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if not in_range(nx, ny) or board[nx][ny] != word[idx] \
                    or (nx, ny) in path:
                    continue
                path.append((nx, ny))
                if dfs(idx+1, path):  # 이렇게 해야 빠져나감
                    return True
                path.pop()
        

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(1, [(i, j)]):
                        return True
        return False
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        L = len(word)

        path = set()  # not list
        
        def in_range(x, y):
            return 0 <= x < m and 0 <= y < n
    
        def dfs(idx, x, y):
            if idx >= L:
                return True

            if not in_range(x, y) or board[x][y] != word[idx] or (x, y) in path:
                return False
            
            path.add((x, y))

            if dfs(idx+1, x, y+1) or \
                dfs(idx+1, x+1, y) or \
                dfs(idx+1, x, y-1) or \
                dfs(idx+1, x-1, y):
                return True
            
            path.remove((x, y))

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    path.add((i, j))  # 첫번째 값 추가
                    if dfs(1, i, j):  # 다음 인덱스 찾으러
                        return True
        
        return False

sol = Solution()
print(sol.exist(
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
))
print(sol.exist(
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
))
print(sol.exist(
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
))