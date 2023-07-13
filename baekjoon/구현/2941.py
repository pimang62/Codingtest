'''
[크로아티아 알파벳]
입력 문자열 내에서 크로아티아 알파벳은 몇 개?

'''

string = input()
# word_dict = { 2 : ["c=", "c-", "d-", "lj", "nj" "s=", "z="], 3 : ["dz="]}
word_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=","z="]
# word_dict = {'c' : ["c=", "c-"], 'd' : ["d-", "dz="], 'l':["lj"], 'n':["nj"] 's':["s="], 'z':["z="]}


cnt = 0
for word in word_list:
    string = string.replace(word, '*')

print(len(string))



            





