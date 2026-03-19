t=int(input())
for _ in range(t):
    a,b,c,d=map(float,input().split())
    p=((c-a)**2+(d-b)**2)**0.5
    print("{:.4f}".format(p))