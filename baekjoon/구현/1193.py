'''
[분수찾기]
x가 주어졌을 때, x번째 분수는?
1 <= x <= 1e7

1/1, 1/2, 2/1, 3/1, 2/2, 1/3, 1/4, 2/3, 3/2, 4/1, 5/1, 4/2 ...


'''

'''
x = int(input())   # 1번, 2번, ... 

array = []
n = 2       # 시작 지점

while len(array) <= x:    

    if n % 2 == 0:
        """
        for i in range(n-1, 0, -1):   # 분자 역순
            for j in range(1, n):
                if i+j == n and f'{i}/{j}' not in array:
                    array.append(f'{i}/{j}')
        """
        i = n-1
        j = 1
        while i > 0 and j < n:
            if len(array) > x:
                break
            array.append(f'{i}/{j}')
            i -= 1
            j += 1
    
    else:
        """
        for i in range(1, n):
            for j in range(n-1, 0, -1):   # 분모 역순
                if i+j == n and f'{i}/{j}' not in array:
                    array.append(f'{i}/{j}')
        """
        i = 1
        j = n-1
        while i < n and j > 0:
            if len(array) > x:
                break
            array.append(f'{i}/{j}')
            i += 1
            j -= 1

    n += 1  # 1씩 증가

print(array[x-1])   # 1-indexed
'''

x = int(input())    # 1, 2, 3 ...
n = 1

# 시작 지점 찾아 연산 횟수 줄이기
for n in range(1, 1000000):
    if x > ((n)*(n+1)/2):
        continue
    else:   # x <= ((n)*(n+1)/2)
        break


target = n+1    # 분모 분자 더한 값
mod = x - ((n-1)*(n)/2) -1   # 찾을 순서 -1 (index)

array = []
# target 값이 짝수면 분자가 더 큼
if target % 2 == 0:
    i = target-1
    j = 1
    while i > 0 and j < target:
        if len(array) > mod:
            break
        array.append(f'{i}/{j}')
        i -= 1
        j += 1
else:		# 홀수면 분모가 더 큼
    i = 1
    j = target-1
    while i < target and j > 0:
        if len(array) > mod:
            break
        array.append(f'{i}/{j}')
        i += 1
        j -= 1

print(array[-1])
