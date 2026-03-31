def giaithua(x):
    gt = 1
    for i in range(1, x + 1):
        gt *= i
    return gt

t = int(input())

for _ in range(t):
    n = int(input())
    temp = n
    tong = 0

    while temp > 0:
        digit = temp % 10
        tong += giaithua(digit)
        temp //= 10

    if tong == n:
        print("Yes")
    else:
        print("No")