xs = range(1, 6)
xs = [x*2 for x in xs if x % 2 == 0]
print(xs)

from functools import partial
def add(x, y):
    return x+y

def outer(x):
    def inner(y):
        return x+y
    return inner

def partial(add, x):
    def inner(y):
        return x+y
    return inner

#print(outer(2)(4))
print(outer(2))
print(partial(add, 2)(4))

def f1(values: list[int]):
    return sum(x**2 for x in values if x%2 == 0)

print(f1(values=range(1, 10)))

def f2(values: list[int]):
    return sum(x*x if x%2 == 0 else 0 for x in values)

print(f2(values=range(1, 10)))

print(1+2.3)
#print("hello")*3
print([0, 1]*3)
print(None==False)  # 빈 값

def parse1():
    with open('C:/Users/yelin/codingtest/study/access.log', 'r') as f:
        for line in f:
            yield line.split()[1]

for b in parse1():
    print(b)

import re
def parse2():
    with open('C:/Users/yelin/codingtest/study/access.log', 'r') as f:
        for line in f:
            yield from re.findall(r'\d{2}:\d{2}:\d{2}', line)[:1]

for c in parse2():
    print(c)
    
def fill1(temperatures1):
    total, count = 0, 0
    for t1 in temperatures1:
        if t1 is not None:
            total += t1
            count += 1
    avg1 = total / count
    for t1 in temperatures1:
        if t1 is None:
            t1 = avg1
    return temperatures1

def fill3(temperatures3):
    good3 = [t3 for t3 in temperatures3 if t3]
    avg3 = sum(good3) / len(good3)
    for i, t3 in enumerate(temperatures3):
        temperatures3[i] = t3 or avg3
    print(temperatures3)    # 0과 None을 구별할 수 없음!

def fill4(temperatures4):
    good4 = [t4 for t4 in temperatures4 if t4]
    avg4 = sum(good4) / len(good4)
    temperatures4 = [t4 or avg4 for t4 in temperatures4]
    print(temperatures4)    # 원본 리스트 변경하지 않음!

def fill5(temperatures5):
    good4 = [t5 for t5 in temperatures5 if t5]
    avg5 = sum(good4) / len(good4)
    temperatures5[:] = [t5 if t5 is not None else avg5 for t5 in temperatures5]
    print(temperatures5)

#print(fill1([1, 2, 3, None, 5]))    #[1, 2, 3, None, 5]
fill3(temperatures3=[1, None, 3, None, 0])
fill4(temperatures4=[1, None, 3, None, 0])
fill5(temperatures5=[1, None, 3, None, 0])