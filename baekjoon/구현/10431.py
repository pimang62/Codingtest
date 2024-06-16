'''
[줄세우기]
키 순서대로 번호 부여
같은 키를 가진 학생은 없음

아무나 한 명 맨앞
한 명씩 줄의 맨 뒤에 섬
  - 앞에 큰 학생이 없으면 그 자리에
  - 앞에 큰 학생이 한 명 이상이라면 가장 앞에 있는 학생의 바로 앞에

학생들이 총 몇 번 뒤로 물러서게 될까?

1 <= p <= 1000
T, 20개의 양의 정수

1
1 19 20 17 18 15 16 13 14 11 12 9 10 7 8 5 6 3 4 1 2
1 189 => 180 *
'''
p = int(input())

for i in range(1, p+1):
    nlist = list(map(int, input().split()))[1:]

    cnt = 0  # 물러난 걸음 수
    for j in range(1, len(nlist)):
        key = nlist[j]
        k = j - 1
        while k >= 0 and nlist[k] > key:
            nlist[k + 1] = nlist[k]
            k -= 1
            cnt += 1
        nlist[k + 1] = key
    
    print(i, cnt)