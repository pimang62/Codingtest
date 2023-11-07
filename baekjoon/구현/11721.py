'''
[열 개씩 끊어 출력하기]
'''

string = input()

idx = 0
while True:
    # 리스트 슬라이싱은 정확한 인덱스 값이 
    # 존재하지 않아도 가능하다..
    print(string[idx:idx+10])
    if idx+10 >= len(string):
        break
    idx += 10

# print(string[idx:])
    