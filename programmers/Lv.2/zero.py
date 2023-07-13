def solution(s):
    
    try_cnt = 0
    zero_cnt = 0
    
    # s가 '1'과 같지 않으면! 반복문 시작
    while s != '1':
        
        # 제거할 '0'의 갯수
        zero = s.count('0')
        zero_cnt += zero
        
        # 남은 문자열 길이
        num = len(s) - zero
        
        # '0b' 삭제
        s = str(bin(num))[2:]
        try_cnt += 1
    
    return [try_cnt, zero_cnt]

print(solution('10001100'))