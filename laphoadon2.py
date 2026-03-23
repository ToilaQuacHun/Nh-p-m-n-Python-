from datetime import datetime

class KhachHang:
    def __init__(self, stt, ten, sophong, ngaynhan, ngaytra, phatsinh):
        self.makh = f"KH{stt:02d}"
        self.ten = ten
        self.sophong = sophong
        self.songayo = (ngaytra - ngaynhan).days + 1
        self.thanhtien = self.songayo * self.don_gia() + phatsinh

    def don_gia(self):
        tang = self.sophong // 100
        if tang == 1:
            return 25
        elif tang == 2:
            return 34
        elif tang == 3:
            return 50
        else:
            return 80

    def __str__(self):
        return f"{self.makh} {self.ten} {self.sophong} {self.songayo} {self.thanhtien}"

n = int(input())
ds = []

for i in range(1, n + 1):
    ten = input().strip()
    sophong = int(input().strip())
    ngaynhan = datetime.strptime(input().strip(), "%d/%m/%Y")
    ngaytra = datetime.strptime(input().strip(), "%d/%m/%Y")
    phatsinh = int(input().strip())

    ds.append(KhachHang(i, ten, sophong, ngaynhan, ngaytra, phatsinh))

ds.sort(key=lambda x: x.thanhtien, reverse=True)

for x in ds:
    print(x)