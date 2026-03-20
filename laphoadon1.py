class hoadon:
    def __init__(self,mahoadon, hoten, cu, moi, dinhmuc):
        self.mahoadon = f"KH{mahoadon:02d}"
        self.hoten = hoten
        self.cu = cu
        self.moi = moi
        self.dinhmuc = self.moi - self.cu
        
        
    def tiennuoc(self):
        x = self.dinhmuc
        if x <= 50:
            tong = (x *100)*1.02
        elif x <=100:
            tong = ((50*100) + ((x - 50)*150))*1.03
        else: 
            tong = ((50*100)+(50*150)+(x -100)*200)*1.05
        return int(tong+0.5)
    def __xstr__(self):
        return f"{self.mahoadon} {self.hoten} {self.tiennuoc()}"
t = int(input())
ds=[]
for i in range(1, t+1):
    hoten = input().strip()
    cu = int(input())
    moi = int(input())
    dinhmuc = moi - cu
    ds.append(hoadon(i,hoten,cu,moi,dinhmuc))
ds.sort(key=lambda x: x.tiennuoc(), reverse=True)
for x in ds:
    print(x)
   