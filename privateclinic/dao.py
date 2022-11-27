from privateclinic.models import NhanVien, ThoiGian, BacSi, Yta, DanhSachKhamBenh, \
    ChiTietDSKham, BenhNhan, TaiKhoan, Thuoc, PhieuKham, PhieuKham_Thuoc, QuiDinh, HoaDon
import hashlib
from privateclinic import db, app


def list_doctor_and_nurse():
    sql = 'SELECT maNV, hoTen, email, ngaySinh, diaChi, dienThoai, hinhAnh ' \
          'FROM privateclinic.nhan_vien as nv inner join privateclinic.bac_si as b ON nv.maNV = b.maBS ' \
          'UNION ' \
          'SELECT maNV, hoTen, email, ngaySinh, diaChi, dienThoai, hinhAnh ' \
          'FROM privateclinic.nhan_vien as nv inner join privateclinic.yta as y ON nv.maNV = y.maYT'
    result = db.session.execute(sql).fetchall()

    return result


def get_staff_by_id(id):
    return NhanVien.query.get(id)


def get_doctor_by_id(id):
    sql = 'SELECT * FROM privateclinic.nhan_vien as n ' \
          'INNER JOIN privateclinic.bac_si as nv ' \
          'ON n.maNV=nv.maBS ' \
          'where n.maNV = ' + id
    result = db.session.execute(sql).first()
    return result


def get_role(id):
    return TaiKhoan.query.filter(TaiKhoan.id.__eq__(id)).first()


def get_nurse_by_id(id):
    sql = 'SELECT * FROM privateclinic.nhan_vien as n ' \
          'INNER JOIN privateclinic.yta as y ' \
          'ON n.maNV=y.maYT ' \
          'where n.maNV = ' + id
    result = db.session.execute(sql).first()
    return result


def list_doctor():
    return BacSi.query.all()


def list_nurse():
    return Yta.query.all()


def get_date_exam(ngayKham):
    query = DanhSachKhamBenh.query.filter(DanhSachKhamBenh.ngayKham.__eq__(ngayKham))
    return query.first()


def list_time():
    return ThoiGian.query.all()


def get_time_by_date_by_id(ngayKham, time_id):
    sql = 'select ngayKham, maTG ' \
          'from privateclinic.ds_kham_benh as d ' \
          'inner join privateclinic.ct_ds_kham as c ' \
          'on d.maDS=c.maDS where d.ngayKham = \'' + ngayKham + \
          '\' and c.maTG =' + time_id
    result = db.session.execute(sql).first()
    return result


def count_total_patients_in_date(ngayKham):
    sql = 'select count(privateclinic.d.maDS) as soLuong ' \
          'from privateclinic.ds_kham_benh as d ' \
          'inner join privateclinic.ct_ds_kham as c ' \
          'on d.maDS=c.maDS where d.ngayKham = \'' + ngayKham + \
          '\''
    result = db.session.execute(sql).first()

    return result


def enroll_schedule_exam(name, phone, email, dob, gender, address, date_schedule, time_id):
    bn = BenhNhan(hoTen=name, dienThoai=phone, email=email, ngaySinh=dob, gioiTinh=gender, diaChi=address)
    db.session.add(bn)
    db.session.commit()
    if get_date_exam(ngayKham=date_schedule):
        ds = get_date_exam(ngayKham=date_schedule)
    else:
        ds = DanhSachKhamBenh(ngayKham=date_schedule)
        db.session.add(ds)
        db.session.commit()
    ctds = ChiTietDSKham(maDS=ds.maDS, maBN=bn.maBN, maTG=time_id)
    db.session.add(ctds)
    db.session.commit()


def get_all_patients_by_date(date):
    sql = 'SELECT ct.maBN, hoTen, dienThoai, email, ngaySinh, gioiTinh, diaChi ' \
          'FROM (privateclinic.ds_kham_benh as d ' \
          'INNER JOIN privateclinic.ct_ds_kham as ct ON d.maDS = ct.maDS)  ' \
          'INNER JOIN privateclinic.benh_nhan as b ' \
          'ON b.maBN = ct.maBN ' \
          'where d.ngayKham = \'' + date + '\''

    result = db.session.execute(sql).fetchall()
    return result


def update_user_info(maNV, hoTen, ngaySinh, email, dienThoai, diaChi, hinhAnh):
    nhanVien = NhanVien.query.filter_by(maNV=maNV).first()
    nhanVien.hoTen = hoTen
    nhanVien.email = email
    nhanVien.ngaySinh = ngaySinh
    nhanVien.diaChi = diaChi
    nhanVien.hinhAnh = hinhAnh
    nhanVien.dienThoai = dienThoai
    db.session.commit()


def update_acc_info(maNV, name, username, password, avatar):
    taiKhoan = TaiKhoan.query.filter_by(maNV=maNV).first()
    taiKhoan.name = name
    taiKhoan.username = username
    taiKhoan.password = password
    taiKhoan.avatar = avatar
    db.session.commit()


def get_all_medicine_paginate(page, per_page):
    return Thuoc.query.paginate(page=page, per_page=per_page)


def find_medicine_by_name(kw, page, per_page):
    list_medicine = Thuoc.query.filter(Thuoc.tenThuoc.contains(kw)).paginate(page=page, per_page=per_page)
    return list_medicine


def get_medicine_by_id(id):
    return Thuoc.query.get(id)


def get_patient_by_id(id):
    return BenhNhan.query.get(id)


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    return TaiKhoan.query.filter(TaiKhoan.username.__eq__(username.strip()),
                                 TaiKhoan.password.__eq__(password)).first()


def get_user_info(user_id):
    return NhanVien.query.get(user_id)


def get_user_by_id(user_id):
    return TaiKhoan.query.get(user_id)


def get_all_medical_reports_by_patient_id(id, page, per_page):
    list_medical_reports = PhieuKham.query.filter(PhieuKham.maBN.__eq__(id)).paginate(page=page, per_page=per_page)
    return list_medical_reports


def get_all_medical_reports_by_patient_id(id):
    list_medical_reports = PhieuKham.query.filter(PhieuKham.maBN.__eq__(id))
    return list_medical_reports


def get_medical_report_by_id(id):
    return PhieuKham.query.get(id)


def get_medical_report_detail_by_medical_report_id(id):
    medical_report_detail = PhieuKham_Thuoc.query.filter(PhieuKham_Thuoc.maPK.__eq__(id)).all()
    return medical_report_detail


def get_patient_by_info(id):
    return BenhNhan.query.get(id)


def save_medical_report(ngayKham, trieuChung, chuanDoan, maBN, list_cach_dung, list_so_luong, list_thuoc):
    phieu_kham = PhieuKham(ngayKham=ngayKham, trieuChung=trieuChung, chuanDoan=chuanDoan, maBN=maBN)
    db.session.add(phieu_kham)
    for x in range(len(list_thuoc)):
        phieu_thuoc = PhieuKham_Thuoc(maThuoc=list_thuoc[x], soLuong=list_so_luong[x], cachDung=list_cach_dung[x], phieukham=phieu_kham)
        db.session.add(phieu_thuoc)
    db.session.commit()


def get_all_medicines():
    return Thuoc.query.all()


def get_rule_by_id(id):
    return QuiDinh.query.get(id)


def get_all_medical_report_details_by_medical_report_id(id):
    return PhieuKham_Thuoc.query.filter_by(maPK=id).all()


def create_receipt(tien_kham, tien_thuoc, tong_tien, maPK):
    hoa_don = HoaDon(tienThuoc=tien_thuoc, tienKham=tien_kham, tongTien=tong_tien, maPK=maPK)
    db.session.add(hoa_don)
    db.session.commit()


def get_receipt_by_medical_report_id(maPK):

    hoaDon = HoaDon.query.filter(HoaDon.maPK.__eq__(maPK)).all()
    return hoaDon