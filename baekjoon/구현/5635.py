'''
[생일]

'''
n = int(input())

d = {}
for _ in range(n):
    info = input().split()
    count = int(info[3])+int(info[2])*0.1+int(info[1])*0.01
    d[info[0]] = count

d_count = sorted(d.items(), key=lambda x: x[1])

print(d_count[-1][0])
print(d_count[0][0])
