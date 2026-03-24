# đã hoàn thành nhưng trên web lại để là WA
class NhanVien:
    def __init__(self, stt, ten, lt, th):
        self.manv = f"TS{stt:02}"
        self.ten = ten
        lt = self.chuanhoadiem(lt)
        th = self.chuanhoadiem(th)
        self.diemtb = (lt + th) / 2

    def chuanhoaten(self,s):
        return ' '.join(x.capitalize() for x in s.strip().split())
    
    def chuanhoadiem(self, s):
        if '.' in s:
            return float(s)
        if len(s) == 2:
            return float(s) / 10
        return float(s)

    def xeploai(self):
        if self.diemtb > 9.5:
            return "XUAT SAC"
        elif self.diemtb >= 8:
            return "DAT"
        elif self.diemtb >= 5:
            return "CAN NHAC"
        else:
            return "TRUOT"

    def __str__(self):
        return f"{self.manv} {self.ten} {self.diemtb:.2f} {self.xeploai()}"


t = int(input())
ds = []
for i in range(1, t + 1):
    ten = input().strip()
    lt = input().strip()
    th = input().strip()
    ds.append(NhanVien(i, ten, lt, th))

ds.sort(key=lambda x: -x.diemtb)

for x in ds:
    print(x)