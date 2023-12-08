'''
[진법 변환 2]
'''
N, B = map(int, input().split())

# {15 : 'A'}
zinbub = {(i-55):chr(i) for i in range(65, 91)}
number = {i:str(i) for i in range(10)}

zinbub.update(number)

def transform(n, b):
    num = n
    s = ''
    while num != 0:
        num, d = divmod(num, b)
        s += zinbub[d]
    return s[::-1]

print(transform(N, B))