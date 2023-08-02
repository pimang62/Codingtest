answer = []

def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1 :
        answer.append([from_pos, to_pos])
        return
    hanoi(n-1, from_pos, aux_pos, to_pos)   # n-1번까지의 원반들은 from_pos에서 aux_pos로 옮기겠다
    answer.append([from_pos, to_pos])       # n번째 원반은 from_pos에서 to_pos에 옮기겠다
    hanoi(n-1, aux_pos, to_pos, from_pos)   # n-1번까지의 원반들은 aux_pos에서 to_pos로 옮기겠다
    
hanoi(4, 1, 3, 2)
print(answer)

def hanoi(n):
    
    def _hanoi(m, s, b, d):
        if m == 1:
            yield [s, d]
        else:
            yield from _hanoi(m-1, s, d, b)
            yield [s, d]
            yield from _hanoi(m-1, b, s, d)

    ans = list(_hanoi(n, 1, 2, 3))
    return ans  # 2차원 배열을 반환해 주어야 합니다.


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(hanoi(2))