def check(string):
    
    pattern = {'[':']', '{':'}', '(':')'}
    str_list = [s for s in string]
    for k, v in pattern.items():
        if k in string and v in string:
            if string.index(k) < string.index(v):
                str_list.remove(k)
                str_list.remove(v)
        
    if len(str_list) > 0:
        return False
    return True

print(check(string='}}}'))