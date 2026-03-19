soluongtest=int(input())
for _ in range(soluongtest):
    N=input()
    res=""
    i=0 
    for i in range(0,len(N),2):
        ktu= N[i]
        so=N[i+1]
        res= res+ktu*int(so)
    print(res)
        