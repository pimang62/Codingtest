'''
[별 찍기 - 19]
1
*  1

2
*****  5
*   *
* * *
*   *
*****

3
*********  9
*       *
* ***** *
* *   * *
* * * * *
* *   * *
* ***** *
*       *
*********

4
*************  13 (0, 0)
*           *
* ********* *  (2, 2)
* *       * *
* * ***** * *  (4, 4)
* * *   * * *
* * * * * * *  (6, 6)
* * *   * * *
* * ***** * *
* *       * *
* ********* *
*           *
*************

4n-3
'''
n = int(input())

graph = [[' ']*(4*n-3) for _ in range(4*n-3)]
N, M = len(graph), len(graph[0])

idx = 0
for _ in range(n):

    for i in range(idx, N-idx):
        graph[i][idx] = '*'
        graph[i][M-1-idx] = '*'
    
    for j in range(idx, M-idx):
        graph[idx][j] = '*'
        graph[N-1-idx][j] = '*'
    
    idx += 2

for i in range(N):
    print(''.join(graph[i]))
