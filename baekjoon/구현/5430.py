'''
[AC]
정수 배열에 연산을 하기 위함
R: 배열에 있는 수의 순서를 뒤집기
D: 첫 번째 수를 버림
배열이 비어있는데 D를 사용한 경우 에러!
'''
import re
"""
T = int(input())
for _ in range(T):
    p = input()  # RDD
    n = int(input())
    nlist = [int(i) for i in re.split('[^0-9]+', input()) if i.isdigit()]
    # 시간 초과 방지
    if p.count('D') > n:
        print('error')
        continue
    for o in p:  # order
        if o == 'R':
            nlist.reverse()
        else:  # o == 'D'
            if nlist:
                nlist.pop(0)
            else:
                flag = False  # get error
                break

    print('[' + ','.join([str(i) for i in nlist]) + ']') if flag else print('error')
"""
T = int(input())
for _ in range(T):
    p = input()  # RDD
    n = int(input())
    string = input()  # nlist string ver.
    nlist = list(map(int, string[1:-1].split(','))) if len(string) > 2 else []
    d = 0  # 0: 앞에서부터 / 1: 뒤에서부터
    flag = True
    for o in p:
        if o == 'R':
            d ^= 1  # 반대로 변경
        else:  # if o == 'D'
            if nlist:
                nlist.pop(-d)  # 0: 앞, -1: 뒤
            else:
                flag = False
                break
    
    if flag and d == 0:  # 앞에서부터 읽어야
        print('[' + ','.join([str(i) for i in nlist]) + ']') 
    elif flag and d == 1:  # 뒤에서부터 읽어야
        print('[' + ','.join([str(i) for i in reversed(nlist)]) + ']')
    else: 
        print('error')
