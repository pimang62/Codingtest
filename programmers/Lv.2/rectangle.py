def solution(board):
    n = len(board)
    m = len(board[0])
    
    #dp = [ [0]*m for _ in range(n) ]

    answer = 1
    for i in range(n):
        for j in range(m):

            if board[i][j]:
                a = min(board[i-1][j], board[i][j-1], board[i-1][j-1])
                board[i][j] = a + 1
    
            answer = max(answer, board[i][j])
    
    return answer**2

# print(solution(board=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])) 
# -> a = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) : 0
# -> a = min(board[i-1][j], board[i][j-1], board[i-1][j-1] if i-1 < n and j-1 < m else 0) : 0
# -> a = max(board[i-1][j], board[i][j-1], board[i-1][j-1]) : 1 ??
print(solution(board=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution(board=[[0,0,1,1],[1,1,1,1]]))
print(solution(board = [
    [0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1]
]))