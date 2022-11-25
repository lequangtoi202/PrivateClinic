from sqlalchemy import Column, BIGINT, Float, ForeignKey, Integer, String, Boolean,TIME, Text, Enum, DATE, Table, DATETIME
from sqlalchemy.orm import relationship, backref
from privateclinic import db, app
from enum import Enum as UserEnum
from flask_login import UserMixin


class UserRole(UserEnum):
    ADMIN = 1
    USER = 2
    NURSE = 3
    DOCTOR = 4
    CASHIER = 5


class QuiDinh(db.Model):
    maQD = Column(BIGINT, primary_key=True, autoincrement=True)
    tenQD = Column(String(100), nullable=False)
    giaTri = Column(String(50), nullable=False)

    def __str__(self):
        return self


class NhanVien(db.Model):
    maNV = Column(BIGINT, primary_key=True, autoincrement=True)
    hoTen = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    ngaySinh = Column(DATE, nullable=False)
    diaChi = Column(String(100), nullable=False)
    dienThoai = Column(String(11), nullable=False)
    taiKhoan = relationship('TaiKhoan', backref='nhanvien', lazy=True)
    bacSi = relationship('BacSi', backref='nhanvien', uselist=False)
    yta = relationship('Yta', backref='nhanvien', uselist=False)

    def __str__(self):
        return self.hoTen


class BacSi(NhanVien):
    maBS = Column(BIGINT, ForeignKey(NhanVien.maNV), primary_key=True, unique=True)
    chungChi = Column(String(100), nullable=False)
    chuyenMon = Column(String(100), nullable=False)


class Yta(NhanVien):
    maYT = Column(BIGINT, ForeignKey(NhanVien.maNV), primary_key=True, unique=True)
    bangCap = Column(String(100), nullable=False)


class TaiKhoan(db.Model, UserMixin):
    maTK = Column(BIGINT, primary_key=True, autoincrement=True)
    tenDN = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(150))
    is_active = Column(Boolean, default=True)
    user_role = Column(Enum(UserRole), default=UserRole.USER)
    maNV = Column(BIGINT, ForeignKey(NhanVien.maNV), nullable=False, unique=True)

    def __str__(self):
        return self.username


class Thuoc(db.Model):
    __tablename__ = 'thuoc'

    maThuoc = Column(BIGINT, primary_key=True, autoincrement=True)
    tenThuoc = Column(String(150), nullable=False)
    moTa = Column(Text, nullable=False)
    soLuong = Column(Integer, nullable=False)
    giaBan = Column(Float, nullable=False)
    is_active = Column(Boolean, nullable=False)
    donVi = Column(String(20), nullable=False)
    phieu_thuoc = relationship('PhieuKham_Thuoc', backref="thuoc", lazy=True)

    def __str__(self):
        return self.tenThuoc


class BenhNhan(db.Model):
    __tablename__ = 'benh_nhan'

    maBN = Column(BIGINT, primary_key=True, autoincrement=True)
    hoTen = Column(String(45), nullable=False)
    dienThoai = Column(String(11), nullable=False)
    email = Column(String(50), nullable=False)
    ngaySinh = Column(DATE, nullable=False)
    gioiTinh = Column(Boolean, nullable=False)
    diaChi = Column(String(100), nullable=False)
    phieu_kham = relationship('PhieuKham', backref='benhnhan', lazy=True)
    ctds = relationship('ChiTietDSKham', backref='benh_nhan', lazy=True)


class DanhSachKhamBenh(db.Model):
    __tablename__ = 'ds_kham_benh'
    maDS = Column(BIGINT, primary_key=True, autoincrement=True)
    ngayKham = Column(DATE, nullable=False)
    ctds = relationship('ChiTietDSKham', backref='ds_kham_benh', lazy=True)


class ThoiGian(db.Model):
    __tablename__ = 'thoi_gian'

    maTG = Column(BIGINT, primary_key=True, autoincrement=True)
    gio = Column(TIME, nullable=False)
    ctds_kham = relationship('ChiTietDSKham', backref='thoi_gian', lazy=True)


class ChiTietDSKham(db.Model):
    __tablename__ = 'ct_ds_kham'

    maCTDS = Column(BIGINT, primary_key=True, autoincrement=True)
    maBN = Column(BIGINT, ForeignKey(BenhNhan.maBN), nullable=False)
    maDS = Column(BIGINT, ForeignKey(DanhSachKhamBenh.maDS, ondelete='CASCADE'), nullable=False)
    maTG = Column(BIGINT, ForeignKey(ThoiGian.maTG), nullable=False)


class PhieuKham(db.Model):
    __tablename__ = 'phieu_kham'

    maPK = Column(BIGINT, primary_key=True, autoincrement=True)
    ngayKham = Column(DATE, nullable=False)
    trieuChung = Column(Text, nullable=False)
    chuanDoan = Column(Text, nullable=False)

    hoaDon = relationship('HoaDon', backref='phieu_kham', uselist=False)
    maBN = Column(BIGINT, ForeignKey(BenhNhan.maBN), nullable=False)
    phieu_thuoc = relationship('PhieuKham_Thuoc', backref="phieukham", lazy=True)


class PhieuKham_Thuoc(db.Model):
    __tablename__ = 'phieu_thuoc'
    maPK_Thuoc = Column(BIGINT, primary_key=True, autoincrement=True)
    soLuong = Column(Integer, nullable=True)
    cachDung = Column(String(300), nullable=True)
    maThuoc = Column(BIGINT, ForeignKey('thuoc.maThuoc', ondelete='CASCADE'), nullable=False)
    maPK = Column(BIGINT, ForeignKey('phieu_kham.maPK', ondelete='CASCADE'), nullable=False)


class HoaDon(db.Model):
    maHD = Column(BIGINT, primary_key=True, autoincrement=True)
    tienThuoc = Column(Float, nullable=False)
    tienKham = Column(Float, nullable=False)
    tongTien = Column(Float, nullable=False)
    maPK = Column(BIGINT, ForeignKey(PhieuKham.maPK), unique=True, nullable=False)


class BaoCaoDoanhThuThang(db.Model):
    __tablename__ = 'bc_doanh_thu'

    maBC = Column(BIGINT, primary_key=True, autoincrement=True)
    thoiGian = Column(DATE, nullable=False)
    tongCong = Column(Float, nullable=False)
    ctBaoCao = relationship('ChiTietBaoCaoDoanhThuThang', backref='bc_doanh_thu', lazy=True)


class ChiTietBaoCaoDoanhThuThang(db.Model):
    __tablename__ = 'ctbc_doanh_thu'

    maCTBC = Column(BIGINT, primary_key=True, autoincrement=True)
    ngayKham = Column(DATE, nullable=False)
    soBenhNhan = Column(Integer, nullable=False)
    doanhThu = Column(Float, nullable=False)
    tyLe = Column(Float, nullable=False)
    maBC = Column(BIGINT, ForeignKey(BaoCaoDoanhThuThang.maBC, ondelete='CASCADE'), nullable=False)


class BaoCaoSuDungThuoc(db.Model):
    __tablename__ = 'bc_sd_thuoc'

    maBC = Column(BIGINT, primary_key=True, autoincrement=True)
    thoiGian = Column(DATE, nullable=False)
    ctBaoCao = relationship('ChiTietBaoCaoSuDungThuoc', backref='bc_sd_thuoc', lazy=True)


class ChiTietBaoCaoSuDungThuoc(db.Model):
    __tablename__ = 'ctbc_sd_thuoc'

    maCTBC = Column(BIGINT, primary_key=True, autoincrement=True)
    tenThuoc = Column(String(50), nullable=False)
    soLanDung = Column(Integer, nullable=False)
    donVi = Column(String(10), nullable=False)
    soLuong = Column(Integer, nullable=False)
    maBC = Column(BIGINT, ForeignKey(BaoCaoSuDungThuoc.maBC, ondelete='CASCADE'), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        # t = Thuoc(tenThuoc='Paracetamol', soLuong=200, giaBan=12000, is_active=True, donVi='Vỷ', moTa='Paracetamol thường được chỉ định điều trị trong các trường hợp đau và sốt từ nhẹ đến vừa như đau đầu, đau cơ, đau khớp, đau lưng, đau răng, hạ sốt... Thuốc cũng có tác dụng giảm đau đối với người bị viêm khớp nhẹ, trường hợp viêm nặng hơn như viêm sưng khớp cơ thì việc sử dụng Paracetamol sẽ không hiệu quả.')
        # t1 = Thuoc(tenThuoc='Thuốc Farzincol 10Mg Pharmedic Hỗ Trợ Bổ Sung Kẽm Vào Chế Độ Ăn', soLuong=100, giaBan=580,
        #            is_active=True, moTa=' Farzincol của công ty cổ phần dược phẩm dược liệu Pharmedic, thành phần chính kẽm gluconat'
        #                                 ' 70 mg (tương đương 10 mg kẽm), là thuốc dùng để điều trị bổ sung kẽm vào chế độ ăn trong các trường hợp: Bệnh còi xương, chậm tăng trưởng ở trẻ em. Phụ nữ mang thai và bà mẹ đang cho con bú. Chế độ ăn thiếu cân bằng hoặc kiêng ăn. Nuôi ăn lâu dài qua đường tĩnh mạch. Tiêu chảy cấp và mãn tính. Điều trị thiếu kẽm: Thiếu kẽm nhẹ và vừa trong các trường hợp: Suy dinh dưỡng nhẹ và vừa. Rối loạn đường tiêu hóa: Chán ăn, chậm tiêu, táo bón nhẹ, buồn nôn và nôn khi mang thai. Khó ngủ, mất ngủ, trẻ khóc đêm, suy nhược, nhức đầu...', donVi='Viên')
        #
        # bn = BenhNhan(hoTen='Lê Quang Tới', dienThoai='0868832530', email='quangtoile@gmail.com', ngaySinh='2002/09/25', gioiTinh=True, diaChi='54, Dương Cát Lợi, thị trấn Nhà Bè')
        #
        # db.session.add_all([t, t1, bn])
        # db.session.commit()

        nv1 = NhanVien(hoTen='Phạm Văn C', email='cpham@gmail.com', diaChi='An Giang', ngaySinh='1999/12/24', dienThoai='0786955662')

        db.session.add_all(nv1)
        db.session.commit()
