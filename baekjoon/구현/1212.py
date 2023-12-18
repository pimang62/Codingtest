'''
[8진수 2진수]
'''
"""시간 초과
n = input()  # '314'

orig = ''  # 11 001 100
for i in n:  # 3 1 4
    binn = bin(int(i))[2:]
    orig += '0'*(3-len(binn)) + binn

if orig == '0':
    print(orig)
elif orig[0:2] == '00':
    print(orig[2:])
elif orig[0] == '0':
    print(orig[1:])
else:
    print(orig)
------------------------
n = input()  # 314

d = {'0': '000',
     '1': '001',
     '2': '010',
     '3': '011',
     '4': '100',
     '5': '101',
     '6': '110',
     '7': '111'}

orig = ''
for i in n:  # '3', '1', '4'
    orig += d[i]
    
while orig.startswith('0'):
    orig = orig[1:]
    
print(orig)
"""
n = input()  # 314

d = int(n, 8)  # 8진수 -> 10진수 변환
print(bin(d)[2:])
# print(oct(d)[2:])  # 10진수 -> 8진수
# print(hex(d)[2:])  # 10진수 -> 16진수

# print(f'{int(input(),8):b}')  # 정답