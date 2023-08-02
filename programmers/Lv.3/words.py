import sys
sys.setrecursionlimit(10**7)

def dfs(begin, target, words, visited, cnt):
    if begin == target:
        return cnt
    word = ''
    for i in range(len(begin)):
        for k in range(97, 123):
            word = begin.replace(begin[i], chr(k))
            if word in words and visited[words.index(word)] == 0:
                visited[words.index(word)] = 1
                dfs(word, target, words, visited, cnt+1)
                visited[words.index(word)] = 0
                return cnt

def solution(begin, target, words):
    if target not in words:
        return 0
    visited = [0] * len(words)
    result = dfs(begin, target, words, visited, 0)
    return result

print(solution(begin="hit", target="cog", words=["hot", "dot", "dog", "lot", "log", "cog"]))