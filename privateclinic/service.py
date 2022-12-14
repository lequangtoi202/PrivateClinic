import datetime

from privateclinic import dao, app
import csv
import os


def export_csv(date):
    list_patients = dao.get_all_patients_by_date(date=date)
    p = os.path.join(app.root_path, "list_patients.csv")
    listP = [
    ]
    for pa in list_patients:
        listP.append({
            "maBN": pa.maBN,
            'hoTen': pa.hoTen,
            'dienThoai': '\'' + pa.dienThoai,
            'email': pa.email,
            'ngaySinh': pa.ngaySinh,
            'gioiTinh': pa.gioiTinh,
            'diaChi': pa.diaChi
        })
    with open(p, "w", encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['maBN', 'hoTen', 'dienThoai', 'email', 'ngaySinh', 'gioiTinh', 'diaChi'])
        writer.writeheader()
        for patient in listP:
            writer.writerow(patient)
    return p


def get_list_times():
    list_times = dao.list_time()

    return list_times


def get_staff_by_id(id):
    bac_si = dao.get_doctor_by_id(id)
    if bac_si is None:
        return dao.get_nurse_by_id(id)
    return bac_si


def get_all_staff():
    return dao.get_all_staff()


def check_role(id):
    return dao.get_role(id).user_role


def get_all_role():
    return dao.get_all_role()


def get_all_doctor_and_nurse():
    list_doctor_and_nurse = dao.list_doctor_and_nurse()

    return list_doctor_and_nurse


def get_user_by_id(maNV):
    return dao.get_user_by_id(maNV)


def enroll_medical_exam(name, phone, email, dob, gender, address, date_schedule, time_id):
    if dao.get_time_by_date_by_id(ngayKham=date_schedule, time_id=time_id):
        return "Tgian đã đc đặt trc"
    elif dao.count_total_patients_in_date(ngayKham=date_schedule).soLuong >= 40:
        return "Số lượng người đăng ký khám đã đạt giới hạn. Vui lòng đặt ngày khác!"
    else:
        return dao.enroll_schedule_exam(name=name, phone=phone, email=email, dob=dob, gender=gender, address=address, date_schedule=date_schedule, time_id=time_id)


def get_all_patients_by_date(date):
    return dao.get_all_patients_by_date(date=date)


def update_user_info(maNV, hoTen, ngaySinh, email, dienThoai, diaChi, hinhAnh):
    return dao.update_user_info(maNV, hoTen, ngaySinh, email, dienThoai, diaChi, hinhAnh)


def update_account_info(maNV, name, username, password, avatar):
    return dao.update_acc_info(maNV=maNV, name=name, username=username, password=password, avatar=avatar)


def get_all_medicine_paginate(page, per_page):
    return dao.get_all_medicine_paginate(page=page, per_page=per_page)


def get_medicine_by_id(id):
    return dao.get_medicine_by_id(id=id)


def create_new_medicine(tenThuoc, moTa, soLuong, giaBan, is_active, donVi, hinhAnh):
    return dao.create_new_medicine(tenThuoc, moTa, soLuong, giaBan, is_active, donVi, hinhAnh)


def create_new_acc(name, username, password, is_active, avatar, user_role, maNV):
    return dao.create_new_acc(name=name, username=username, password=password, is_active=is_active, avatar=avatar, user_role=user_role, maNV=maNV)


def find_medicine_by_name(kw, page, per_page):
    return dao.find_medicine_by_name(kw=kw, page=page, per_page=per_page)


def auth_user(username, password):
    return dao.auth_user(username=username, password=password)


def get_user_info_by_id(id):
    return dao.get_user_info(user_id=id)


def get_user_by_id(id):
    return dao.get_user_by_id(user_id=id)


def get_patient_by_id(id):
    return dao.get_patient_by_id(id=id)


def get_all_medical_reports_by_patient_id(id, page, per_page):
    return dao.get_all_medical_reports_by_patient_id(id=id, page=page, per_page=per_page)


def get_all_medical_reports_by_patient_id(id):
    return dao.get_all_medical_reports_by_patient_id(id=id)


def get_medical_report_detail_by_medical_report_id(id):
    return dao.get_medical_report_detail_by_medical_report_id(id=id)


def get_medical_report_by_id(id):
    return dao.get_medical_report_by_id(id=id)


def get_patient_by_id(id):
    return dao.get_patient_by_id(id=id)


def get_all_medicines():
    return dao.get_all_medicines()


def save_medical_report(ngayKham, trieuChung, chuanDoan, maBN, list_cach_dung, list_so_luong, list_thuoc):
    return dao.save_medical_report(ngayKham, trieuChung, chuanDoan, maBN, list_cach_dung, list_so_luong, list_thuoc)


def get_receipt_info(id):
    phieu_thuoc = dao.get_all_medical_report_details_by_medical_report_id(id=id)
    total_quan, total_amount = 0, 0
    list_thuoc = []
    for item in phieu_thuoc:
        thuoc = dao.get_medicine_by_id(item.maThuoc)
        list_thuoc.append({
            'ten_thuoc': thuoc.tenThuoc,
            'so_luong': item.soLuong,
            'don_vi': thuoc.donVi,
            'gia_ban': thuoc.giaBan,
            'tong': thuoc.giaBan * item.soLuong
        })
        total_quan += item.soLuong
        total_amount += thuoc.giaBan * item.soLuong

    return {
        'thuoc': list_thuoc,
        'total_amount': total_amount,
        'total_quan': total_quan
    }


def get_rule_by_id(id):
    return dao.get_rule_by_id(id)


def create_receipt(tien_kham, tien_thuoc, tong_tien, maPK, created_date):
    return dao.create_receipt(tien_kham, tien_thuoc, tong_tien, maPK, created_date)


def get_receipt_by_medical_report_id(maPK):
    return dao.get_receipt_by_medical_report_id(maPK=maPK)


def medical_exam_frequency_stats(month, year1):
    if month == '':
        month = datetime.datetime.now().month
    if year1 == '':
        year1 = datetime.datetime.now().year
    return dao.medical_exam_frequency_stats(month, year1)


def revenue_by_month(year, month):
    if month == '':
        month = datetime.datetime.now().month
    if year == '':
        year = datetime.datetime.now().year
    return dao.revenue_by_month(year=year, month=month)


def medicine_using_stats(year, month):
    if month == '':
        month = datetime.datetime.now().month
    if year == '':
        year = datetime.datetime.now().year
    return dao.medicine_using_stats(year, month)

