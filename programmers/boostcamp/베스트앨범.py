'''
1. 속한 노래가 많이 재생된 장르를 먼저 수록
2. 장르 내에서 많이 재생된 노래를 먼저 수록
3. 장르 내에서 재생 횟수가 같다면 고유 번호가 낮은 순서대로

베스트 앨범에 들어갈 노래의 고유 번호를 순서대로?

1 <= genres, plays <= 10000
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다
모든 장르는 재생된 횟수가 다릅니다

장르 별로 가장 많이 재생된 노래를 최대 두 개까지 모아!
'''
import heapq

def solution(genres, plays):
    best = {}
    data = []
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in best:
            best[g] = p
        else:
            best[g] += p
        data.append((i, g, p))
    # sort
    top = sorted(best.items(), key=lambda x: -x[1])
    data.sort(key=lambda x: (-x[2], x[0]))

    answer = []
    for t in top:  
        cnt = 0     # 장르 고르기
        for d in data:
            (i, g, p) = d
            if cnt == 2:
                break
            if g == t[0]:    # 노래 고르기
                answer.append(i)
                cnt += 1
    return answer


print(solution(genres=["classic", "pop", "classic", "classic", "pop"], plays=[500, 600, 150, 800, 2500]))
print(solution(genres=["classic"], plays=[500]))
print(solution(genres=["classic", "classic", "classic", "classic", "pop"], plays=[50, 60, 100, 30, 8000]))