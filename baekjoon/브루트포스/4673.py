'''
[셀프 넘버]
d(n) = n(ab) + a + b 
생성자가 없는 숫자를 셀프 넘버라 한다.
10000보다 작거나 같은 셀프 넘버?

ex. 2 = 1+1
'''

n_list = [i for i in range(1, 10001)]

for i in range(1, 10001):
    string = str(i)
    num = i + sum([int(s) for s in string])
    if num in n_list:
        n_list.remove(num)

for n in n_list:
    print(n)
    