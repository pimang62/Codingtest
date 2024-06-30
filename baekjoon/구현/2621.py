'''
[카드게임]
https://www.acmicpc.net/problem/2621

빨, 파, 노, 녹 4가지 색
색깔별로 1~9까지 숫자 쓰여짐 => 4*9 
36장에서 5장 뽑고 아래 규칙으로 계산

R, B, Y, G 
ex. Y8은 노란색 8, B5는 파란색 5

<규칙>
(1). 5장이 모두 같은 색이면서 연속적: 가장 높은 수+900
  ex. Y2, Y3, Y4, Y5, Y6 = 900+6 = 906
(2). 5장 중 4장이 같을 때 같은 숫자에 800 더함
  ex. B3, R3, B7, Y3, G3 = 800+3 = 803
(3). 5장 중 3장이 같고 2장도 같을 때, 3장에 *10, 2장 같은 수 더하고 +700
  ex. R5, Y5, G7, B5, Y7 = 5*10 + 7 + 700
(4). 5장의 색깔이 모두 같을 때(연속적이진 않음) 가장 높은 수 + 600
(5). 5장 숫자가 연속적일 때 가장 높은 수 + 500
  ex. B5, Y6, R7, R8, G9 = 500+9 = 509
(6). 5장 중 3장이 같을 때 같은 수 + 400
(7). 5장 중 2장이 같고 또 다른 2장이 같을 때 큰 숫자 *10, +작은 숫자 +300
  ex. R5, Y5, Y4, G9, B4 = 5*10 + 4 + 300
(8). 5장 중 2장이 같을 때 같은 수 + 200
(9). 어떤 경우도 해당하지 않을 때 가장 큰 수 +100

if 5장이 연속적:
    if 모두 같은 색
    else 
if 4장 숫자 같을 때:
if 3장 숫자 같고 2장도 같을 때:
if 3장이 같을 때:
if 2장 숫자 같고 2장도 같을 때:
if 2장이 같을 때:
if 5장 색깔이 같을 때:
else
'''
def score(cards):
    flag, stack = True, []  # 연속적인지?
    
    color, number = {}, {}
    for c, n in cards:  # str, str
        n = int(n)
        color[c] = color.get(c, 0) + 1
        number[n] = number.get(n, 0) + 1
        stack.append(n)
    
    stack.sort()
    
    if stack == list(range(stack[0], stack[0] + 5)):
        if len(color) == 1:
            return stack[-1] + 900
        else:
            return stack[-1] + 500
    
    if 4 in number.values():
        for key in number:
            if number[key] == 4:
                return 800 + key
    
    if 3 in number.values() and 2 in number.values():
        three = 0
        two = 0
        for key in number:
            if number[key] == 3:
                three = key
            if number[key] == 2:
                two = key
        return three * 10 + two + 700
    
    if len(color) == 1:
        return stack[-1] + 600
    
    if 3 in number.values():
        for key in number:
            if number[key] == 3:
                return 400 + key
    
    if list(number.values()).count(2) == 2:
        pairs = []
        for key in number:
            if number[key] == 2:
                pairs.append(key)
        return max(pairs) * 10 + min(pairs) + 300
    
    if 2 in number.values():
        for key in number:
            if number[key] == 2:
                return 200 + key
    
    return max(stack) + 100

cards = []
for _ in range(5):
    cards.append(input().split())

cards.sort(key=lambda x: x[1])  # ['R1', 'B2', 'B3', 'B7', 'Y7']

print(score(cards))
