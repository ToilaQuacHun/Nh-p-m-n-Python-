n=input()
while len(n)%3!=0:
    n="0"+n
res = ""
for i in range(0,len(n),3):
    group=n[i:i+3]
    res+=str(int(group,2))
print(res)