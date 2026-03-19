t=int(input())
for i in range(t):
    n=input().strip()
    tong =0
    for ch in n:
        tong = tong + int(ch)
    s=str(tong)  
    #nếu độ dài s lớn hơn 1 và s là chuỗi đối xứng
    #mã chuỗi[start:end:step]
    if len(s)>1 and s==s[::-1]:
        
        print("YES")
    else:
        print("NO")
            