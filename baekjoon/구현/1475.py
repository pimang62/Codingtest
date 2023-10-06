'''
[방 번호]
한 세트 0~9번까지 하나씩
필요한 세트의 최솟값?
(6은 9를 뒤집어 사용, 9는 6을 뒤집어 사용 가능)
'''
from collections import Counter

# '9999', '122'
string = input()

n_dict = Counter(string)

sixornine = abs(n_dict['6']-n_dict['9'])
if n_dict['6'] > n_dict['9']:
    n_dict['6'] -= sixornine//2
else:
    n_dict['9'] -= sixornine//2

answer = 0
for v in n_dict.values():
    answer = max(answer, v)
print(answer)