*s = input()

for i in range(97, 123):
    if 'chr(i)' in s:
        s = s.replace('chr(i)', 's.index(chr(i)) ')
    else:
        s = s.replace('chr(i)', 's.index(chr(i)) ')

print(w.rstrip())