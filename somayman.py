n=input()
res=0
for x in n:
    if x=='4' or x=='7':
        res+=1
if res==4 or res==7:
    print("YES")
else:
    print("NO")