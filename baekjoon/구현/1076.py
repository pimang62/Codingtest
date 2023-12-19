value = {'black':0,  # 1
         'brown':1,  # 10
         'red':2,    # 100
         'orange':3,
         'yellow':4,
         'green':5,
         'blue':6,
         'violet':7,
         'grey':8,
         'white':9}

answer = ''
for _ in range(2):
    c = input()
    answer += str(value[c])  # '47'

last = input()
answer += '0'*value[last]
print(answer)