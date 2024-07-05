from collections import Counter

sentence = input().lower()
tokens = Counter(sentence)

sorted_tokens = sorted(tokens.items(), key=lambda x: -x[1])

candidate, cnt = sorted_tokens[0]

if len(sorted_tokens) >= 2 and cnt == sorted_tokens[1][1]:
    print("?")
else:
    print(candidate.upper())