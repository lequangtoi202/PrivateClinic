from privateclinic.models import NhanVien, ThoiGian, BacSi, Yta, DanhSachKhamBenh, ChiTietDSKham, BenhNhan, TaiKhoan
import hashlib
from urllib.parse import quote
from privateclinic import db, app
from sqlalchemy import create_engine

def register(hoTen, email, dienThoai, ngaySinh, gioiTinh, diaChi, ngayKham, time):

    bn = BenhNhan(hoTen=hoTen.strip(), email=email.strip(), dienThoai=dienThoai.strip(), ngaySinh=ngaySinh, gioiTinh=gioiTinh, diaChi=diaChi)
    pk = DanhSachKhamBenh(ngayKham = ngayKham)
    ct = ChiTietDSKham(maDS = pk.maDS, maBN = bn.maBN, maTG = time)
    db.session.add([bn, pk, ct])
    db.session.commit()