from itertools import permutations

pron = ["aya", "ye", "woo", "ma"]

per_2 = list(map(''.join, permutations(pron, 2)))
per_4 = list(map(''.join, permutations(pron, 4)))

per_list = per_2 + per_4

print(per_list)