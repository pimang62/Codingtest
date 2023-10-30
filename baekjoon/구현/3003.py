chess = {'k':1, 'q':1, 'l':2, 'b':2, 'n':2, 'p':8}

nlist = list(map(int, input().split()))
answer = []

for i, j in zip(chess.values(), nlist):
    answer.append(str(i-j))

print(' '.join(answer))
