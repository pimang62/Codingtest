from collections import Counter

def solution(k, tangerine):
    
    # t_dict = {t : tangerine.count(t) for t in tangerine} 
    t_dict = Counter(tangerine)
    t_dict = dict(sorted(t_dict.items(), key=lambda x: -x[1]))
    
    ans = 0
    for i, (key, value) in enumerate(t_dict.items(), 1):
        if ans + value < k:
            ans += value
            continue
        else:
            break
        
    
    return i

print(solution(k=6, tangerine=[1, 3, 2, 5, 4, 5, 2, 3]))