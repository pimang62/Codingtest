d = {'A':1, 'C':2, 'G':3, 'T':4}
 
def solution(S, P, Q):  # 'CAGCCTA', [2, 5, 0], [4, 5, 6]
    sequence = [[0, 0, 0, 0]]  # [[], ...]
    concat = [0, 0, 0, 0]  # ACGT
    for i in range(len(S)):
        concat[d[S[i]]-1] += 1  # index : d['A']-1
        sequence += [concat[:]]  # concat의 복사본을 넣어야 함!
    
    answer = []  # 정답 레이블
    for a, b in zip(P, Q):  # 2, 4 -> 2(이전), 5 (1-indexed)
        A_prev, C_prev, G_prev, T_prev = sequence[a]
        A_now, C_now, G_now, T_now = sequence[b+1]
        if A_prev != A_now:  # 우선 순위대로!
            answer.append(1)  # 'A'
        elif C_prev != C_now:
            answer.append(2)
        elif G_prev != G_now:
            answer.append(3)
        else:
            answer.append(4)
    return answer