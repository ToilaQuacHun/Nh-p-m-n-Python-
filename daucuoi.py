t=int(input())
for i in range(t):
    n=input()
    f2=n[:2]
    l2=n[-2:]
    if f2==l2:
        print("YES")
    else:
        print("NO")