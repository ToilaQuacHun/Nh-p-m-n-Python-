t=int(input())
for _ in range(t):
    n=int(input())
    b=10
    while n>=b:
        if n%b>=b//2:
            n=n+b
        n-=n%b
        b*=10
    print(n)