s=input()
res=""
for ch in s:
    if ch != " ":
        res+=ch
    else:
        print(res,end="\n")
        res= ""
print(res)    
    
        