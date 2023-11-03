'''
2007년 1월 1일 : MON!!
8일 MON
2007년 x월 y일?

1 15
1 22
1 29 
2 1 -> 32 -> 
59 : 3
'''
x, y = map(int, input().split())

int_to_day = {1:'MON', 2:'TUE', 3:'WED', 4:'THU', 5:'FRI', 6:'SAT', 0:'SUN'}  # 나머지
day_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

days = 0  # 합친 날짜
for i in range(1, x):  # x 전까지
    days += day_in_month[i]
days += y  # 남은 날짜

print(int_to_day[days%7])
