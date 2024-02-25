'''
[성적 통계]
각 반의 수학 시험 성적의 통계 내기

각 반 학생들의 수학 시험 성적이 주어짐
최대, 최소, 점수 차이를 구하기

입력:
반의 수 k
학생 수 N과 각 학생의 수학 성적

출력:
Class x
Max, Min, Largest gap
'''
k = int(input())

for i in range(k):
    line = list(map(int, input().split()))
    n, nlist = line[0], line[1:]

    nlist.sort(reverse=True)

    largest_gap = 0
    for j in range(n-1):
        largest_gap = max(largest_gap, abs(nlist[j]-nlist[j+1]))
    
    print("Class %d" %(i+1))
    print("Max %d, Min %d, Largest gap %d" %(nlist[0], nlist[-1], largest_gap))