"""
부품의 번호가 담겨있는 길이가 N인 리스트 A가 있다. 사용자는 자신이 찾는 M개의 부품이 A에 있는지 확인해야 한다.
찾으려는 부품의 리스트 B를 받았을 때 A 내 해당 부품의 재고 존재여부를 알려주는 프로그램을 작성하라.

* 입력
N
[담긴 부품번호들]
M
[찾으려는 부품번호들]

* 예시 입력:
5
8 3 7 9 2
3
5 7 9

* 예시 출력:
no yes yes
"""



# 입력받기
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# 집합 자료구조를 이용한 풀이
# A를 집합자료형으로 초기화
# a = set(a)

# # 조건문 작성
# for i in b:
#     if i in a:
#         print("yes", end=' ')
#     else:
#         print("no", end=' ')


# 이진탐색을 사용한 풀이

# 이진탐색 함수 작성 (리스트, 목표, 시작인덱스, 끝인덱스)
def binary_search(array, target, start, end):
    # 만약 시작인덱스가 끝인덱스보다 뒤면 종료
    if start > end:
        return None
    # 중간인덱스 선정
    mid = (start + end) // 2
    # 목표가 중간인덱스의 원소보다 작으면 왼쪽 확인
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_search(array, target, start, mid-1)
    # 목표가 중간인덱스 원소보다 크면 오른쪽 확인
    elif target > array[mid]:
        return binary_search(array, target, mid+1, end)

for i in b:
    if binary_search(a, i, 0, n-1) == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')
