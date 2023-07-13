n = int(input())

# 들어온 정보의 이름만 출력해주는 함수
def name(data):
    return data[0]

# 들어온 정보의 성적만 출력해주는 함수
def score(data):
    return int(data[1])

array = []
for i in range(n):
    info = input().split()
    array.append((name(info), score(info)))

# 점수(array[1])를 기준으로 정렬
result = sorted(array, key=lambda s : s[1])

for student in result:
    print(student[0], end=' ')