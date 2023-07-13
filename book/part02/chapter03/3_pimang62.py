N, K = map(int, input().split())

count = 0

# N이 K와 크거나 같다면 계속 나누기
while N >= K :
    while N % K != 0:       # ex. 24 / 5
        N -= 1              # ex. 24 -> 23 -> 22 -> 20
        count += 1          # count +4 update
    N //= K                 # ex. 20 / 5 -> N = 4 update
    count += 1              # count +1 update

# N이 K보다 작아진다면 1씩 빼기
while N > 1 :               
    N -= 1                  # ex. 4 -> 3 -> 2 
    count += 1              # N = 1로 남음

print(count)                
