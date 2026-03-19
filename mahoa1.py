t= int(input())
for _ in range(t):
    s=input().strip()
    
    res= ""
    count=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count+=1
        else:
            res+=str(count)+s[i-1]
            count=1
    res=res+str(count)+s[-1]
    print(res)