from privateclinic.models import NhanVien, ThoiGian, BacSi, Yta, DanhSachKhamBenh, ChiTietDSKham, BenhNhan, TaiKhoan
import hashlib
from urllib.parse import quote
from privateclinic import db, app
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:%s@localhost/privateclinic?charset=utf8mb4' % quote('lqt25092002'))


def list_doctor_and_nurse():
    sql = 'SELECT maNV, hoTen, email, ngaySinh, diaChi, dienThoai ' \
          'FROM privateclinic.nhan_vien as nv inner join privateclinic.bac_si as b ON nv.maNV = b.maBS ' \
          'UNION ' \
          'SELECT maNV, hoTen, email, ngaySinh, diaChi, dienThoai ' \
          'FROM privateclinic.nhan_vien as nv inner join privateclinic.yta as y ON nv.maNV = y.maYT'
    result = db.session.execute(sql).fetchall()

    return result


def list_doctor():
    return BacSi.query.all()


def list_nurse():
    return Yta.query.all()


def list_time():
    return ThoiGian.query.all()


def enroll_schedule_exam(name, phone, email, dob, gender, address, exam_date, time_id):
    bn = BenhNhan(hoTen=name, dienThoai=phone, email=email, ngaySinh=dob, gioiTinh=gender, diaChi=address)
    db.session.add(bn)
    db.session.commit()
    ds = DanhSachKhamBenh(ngayKham=exam_date)
    db.session.add(ds)
    db.session.commit()
    ctds = ChiTietDSKham(maDS=ds.maDS, maBN=bn.maBN, maTG=time_id)
    db.session.add(ctds)
    db.session.commit()


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    return TaiKhoan.query.filter(TaiKhoan.username.__eq__(username.strip()),
                                 TaiKhoan.password.__eq__(password)).first()


def get_staff_by_id(maNV):
    return NhanVien.query.get(maNV)
