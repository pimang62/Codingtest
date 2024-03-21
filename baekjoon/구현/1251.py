'''
[단어 나누기]

arrested
  i   j 
[:i][i:j][j:]
'''
string = input()
n = len(string)

def in_range(a):
    return 0 < a < n

candidate = []
for i in range(n):
    for j in range(n):
        if i == j or i > j or not in_range(i) or not in_range(j):
            continue
        tmp = string[:i][::-1] + \
            string[i:j][::-1] + string[j:][::-1]
        candidate.append(tmp)

candidate.sort()
print(candidate[0])