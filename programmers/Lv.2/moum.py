def solution(word):
    result = []   # 완전 탐색 리스트
    w = 'AEIOU'    
    string = ''   # 문자열 초기화
    def dfs(cnt, string):
        if cnt == 3:
            #result.append(string)  # 길이가 5인 것만
            return
        for i in range(len(w)):
            # string += w[i] !! X
            result.append(string + w[i])
            dfs(cnt + 1, string + w[i])
    dfs(0, string = '')
    return result.index(word) + 1

solution(word="EIO")