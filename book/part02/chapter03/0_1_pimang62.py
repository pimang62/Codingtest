def change(n) :
    count = 0
    coin_types = [500, 100, 50, 10]

    for coin in coin_types:
        count += n // coin      # 가장 큰 화폐 단위부터 몫 세기
        n %= coin               # 나머지 업데이트
    
    print(count)

change(1260)
