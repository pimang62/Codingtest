def solution(my_string):
    result = []
    for i in my_string:
        if type(i) == int:
            result.append(i)
    return result.sort()

print(solution('ppi24p53i'))