data = input()

# 좌표화
row_data = [_ for _ in range(1, 9)]
column_data = [_ for _ in 'abcdefg']

# 인덱스 주기
row = row_data.index(int(data[1])) + 1          # 1부터 시작
column = column_data.index(str(data[0])) + 1    # 1부터 시작

steps = [(2, -1), (2, 1), (-2, -1), (-2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

count = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        count += 1

print(count) 

