from math import isqrt

# Hàm sàng nguyên tố
def sieve(n):
    is_prime = [True] * (n + 1)
    if n >= 0:
        is_prime[0] = False
    if n >= 1:
        is_prime[1] = False

    for i in range(2, isqrt(n) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
    return primes


N = int(input())

# Ta chỉ cần nguyên tố đến sqrt(N)
limit = isqrt(N)
primes = sieve(limit)

ans = 0

# 1) Đếm số dạng p^8
for p in primes:
    if p ** 8 <= N:
        ans += 1
    else:
        break

# 2) Đếm số dạng p^2 * q^2
# <=> (p*q)^2 <= N
# <=> p*q <= sqrt(N)
for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        if primes[i] * primes[j] <= limit:
            ans += 1
        else:
            break

print(ans)