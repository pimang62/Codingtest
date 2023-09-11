def solution(sequence, k):
    # 결과 : sorted(answer, key = lambda x : (len(x), x[0]))[0]
    answer = []     # 최종 리스트
    n = len(sequence)
    
    compare = sequence[0]
    i, j = 0, 0
    while i < n or j < n:
        if compare < k:
            j += 1
            compare += sequence[j]
            
        if compare > k:
            i += 1
            compare -= sequence[i]
            
        if compare == k:
            answer.append([i, j])
            j += 1
            compare += sequence[j]
    
    return answer
    return sorted(answer, key = lambda x : (len(x), x[0]))[0]

print(solution(sequence=[1, 1, 1, 2, 3, 4, 5], k=5))