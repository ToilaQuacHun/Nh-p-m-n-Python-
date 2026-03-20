class Tinhtiendien:
    def __init__(self, stt, hoten, loai, dau, cuoi):
        #giữ định dạng chuỗi dưới dạng KH01. 
        self.makh = f"KH{stt:02d}"
        self.hoten = hoten
        self.loai = loai 
        self.dau =dau
        self.cuoi = cuoi
        
        self.dinhmuc = self.laytinhmuc()
        self.sodien = self.cuoi - self.dau
        #chỗ min: nếu cái nào nhỏ hơn thì lấy cái đó
        self.tientrongdinhmuc = min(self.sodien, self.dinhmuc) * 450
        #chỗ max: nếu chưa vượt thì định mức là 0, còn nếu vượt thì định mức sẽ là số điện trừ định mức 
        self.tienvuotdinhmuc = max(self.sodien -self.dinhmuc, 0) *1000
        #tại sao chia 20 thay vì nhân 5% vì output ở đây cần số nguyên 
        self.vat = self.tienvuotdinhmuc // 20
        self.tongtien= self.tientrongdinhmuc + self.tienvuotdinhmuc + self.vat
        #s.strip() xoá khoảng trắng cuối và đầu
        #s.strip().split() tách chuỗi đồng thời xoá khoảng trắng thừa
        #x.captalize() hàm hỗ trợ viết hoá chữ cái đầu
        #' '.join() nối các phần tử loại và cách nhau bằng dấu cách 
    def chuanhoaten(self,s):
        return ' '.join(x.capitalize() for x in s.strip().split())
    def laytinhmuc(self):
        if self.loai =='A':
            return 100
        elif self.loai =='B':
            return 500
        else: 
            return 200
    def __str__(self):
        return f"{self.makh} {self.chuanhoaten(self.hoten)} {self.tientrongdinhmuc} {self.tienvuotdinhmuc} {self.vat} {self.tongtien}"
t = int(input())
ds = []
for i in range (1, t+1):
    hoten = input().strip()
    loai, dau, cuoi =input().split()
    dau = int(dau)
    cuoi = int(cuoi)
    ds.append(Tinhtiendien(i, hoten, loai, dau, cuoi))
ds.sort(key=lambda x: x.tongtien, reverse=True)
for x in ds:
    print(x)
    
        