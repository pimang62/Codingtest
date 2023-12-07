'''
[하얀 칸]
.F.F...F
F...F.F.
...F.F.F
F.F...F.
.F...F..
F...F.F.
.F.F.F.F
..FF..F.

(i+j)
0 1 2 3 4 5 6 7
1 2 3 4 5 6 7 8
2 3 4 5 6 7 8 9
...
'''
graph = [[s for s in input()] for _ in range(8)]

cnt = 0
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0 and graph[i][j] == 'F':  # even
            cnt += 1
print(cnt)  

