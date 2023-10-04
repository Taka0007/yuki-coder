import random

def is_prime_miller_rabin(n, k=10):
    if n <= 1:
        return False
    if n <= 3:
        return True

    # n - 1を (2^r) * d に分解する
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # ミラーラビンテストをk回繰り返す
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
    
N = int(input())

for i in range(N):
    num = int(input())
    if is_prime_miller_rabin(num):
        ans = 1
    else:
        ans = 0
        
    print(num,ans,sep=' ')