'''
[16진수]
'''

sixteen_to_ten = {chr(i):(i-55) for i in range(65, 71)}
number = {str(i):i for i in range(10)}

sixteen_to_ten.update(number)

answer = 0  # 10진수
string = input().rstrip()
for i in range(len(string)):
    answer += sixteen_to_ten[string[i]]*16**(len(string)-1-i)
    
print(answer)