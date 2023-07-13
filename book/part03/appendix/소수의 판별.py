import math

def is_prime_number(n):
    # 2 ~ 제곱근(n)까지만 확인
    # int(math.sqrt(n)) : 정수형으로!
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

print(is_prime_number(4))  # False
print(is_prime_number(7))  # True