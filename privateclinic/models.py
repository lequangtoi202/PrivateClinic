from sqlalchemy import Column, BIGINT, Float, ForeignKey, Integer, String, Boolean,TIME, Text, Enum, DATE, Table, DATETIME
from sqlalchemy.orm import relationship, backref
from privateclinic import db, app
from enum import Enum as UserEnum
from flask_login import UserMixin


class UserRole(UserEnum):
    ADMIN = 1
    NURSE = 2
    DOCTOR = 3
    STAFF = 4


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
    hinhAnh = Column(String(200))

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
    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(150))
    is_active = Column(Boolean, default=True)
    user_role = Column(Enum(UserRole), default=UserRole.STAFF)
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
    hinhAnh = Column(String(200), nullable=False)
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
    ngayKham = Column(DATE)
    trieuChung = Column(Text)
    chuanDoan = Column(Text)

    hoaDon = relationship('HoaDon', backref='phieu_kham', uselist=False)
    maBN = Column(BIGINT, ForeignKey(BenhNhan.maBN))
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
    created_date = Column(DATETIME, nullable=False)
    maPK = Column(BIGINT, ForeignKey(PhieuKham.maPK), unique=True, nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()