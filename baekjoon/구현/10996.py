n = int(input())

for i in range(2*n):
    if i % 2 == 0:  # 0, 2, ...
        str1 = '* '*(n//2+1)
        print(str1[:n])
    else:  # 1, 3, ...
        str2 = ' *'*(n//2+1)
        print(str2[:n])