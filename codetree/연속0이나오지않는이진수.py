'''
연속해서 0이 나오지 않는 n자리 이진수
사전순으로 가장 뒤에 있는 숫자부터 먼저
ex. 111
    110
    101
    ...
'''

n = int(input())

def func(res):
    if len(res) == n:
        print(*res)
        return
    
    func(res+[1])
    if len(res) == 0 or res[-1] == 1:
        func(res+[0])

func([])