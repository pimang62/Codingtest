'''
[A와 B]
- 문자열 뒤에 A를 추가
- 문자열 뒤집고 뒤에 B 추가

S를 T로 만들 수 있는지? 1 or 0
'''
# S = input()
# T = input()

# answer = 0  # 시간 초과

# def dfs(string):
#     global answer
#     if len(string) == len(T):
#         if string == T:
#             print(1)
#             exit()
#         return
    
#     string += 'A'
#     dfs(string)
#     string = string[:-1]
    
#     string = string[::-1] + 'B'
#     dfs(string)
#     string[::-1]

# dfs(S)
# print(answer)

S = list(input().rstrip())
T = list(input().rstrip())

while T:
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T.reverse()
    if S == T:
        print(1)
        exit()

print(0)