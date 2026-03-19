n=input()
res= ""
count=0
for ch in reversed(n):
    if count==3:
        res="," +res
        count=0
    res=ch+res
    count+=1
print(res)
