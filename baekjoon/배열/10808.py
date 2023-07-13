'''
[알파벳 갯수]
chr(65) : 'A', chr(97) : 'a'
ord('A') : 65, ord('a') : 97
'''

s = str(input())

def solution(s):
    result = [0] * 26
    for i in s:
        result[ord(i)-97] += 1
    return " ".join(str(i) for i in result)
    
print(solution(s))