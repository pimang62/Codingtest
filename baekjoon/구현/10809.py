s = input()     # baekjoon

a = [-1] * 26   # a(97), b(98), c, d, ... z(122)

for i in range(len(s)):
    if a[ord(s[i])-97] == -1:   # 기록되어 있지 않은 경우만 기록
        a[ord(s[i])-97] = i  

print(' '.join(str(i) for i in a))
            