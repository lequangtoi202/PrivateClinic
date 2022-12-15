from datetime import date, datetime
from privateclinic.models import UserRole
from flask import render_template, request, redirect, url_for, flash, session, jsonify, send_file, make_response
from privateclinic import login, app, service
from privateclinic.admin import *
from flask_login import login_user, logout_user, login_required, current_user
import cloudinary.uploader
import pdfkit
import hashlib

ITEMS_PER_PAGE = 8


# -----------CUSTOMER-------------- #
def index():
    return render_template('/customer/index.html')


def cus_about():
    return render_template('/customer/about.html')


def cus_contact():
    return render_template('/customer/contact.html')


def cus_list_member():
    return render_template('/customer/team.html')


def cus_appointment():
    return render_template('/customer/appointment.html')


def cus_enroll_medical_exam():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        dob = request.form['dob']
        gender = True if request.form['gender'] == '1' else False
        address = request.form['address']
        date_schedule = request.form['date_schedule']
        time_id = request.form['time']
        rs = service.enroll_medical_exam(name=name, phone=phone, email=email, dob=dob, gender=gender, address=address,
                                         date_schedule=date_schedule, time_id=time_id)
        if type(rs) == str:
            flash("Đăng ký không thành công!", 'error')
        else:
            flash("Đăng ký lịch khám thành công!", 'success')
    return redirect(url_for("index"))


# -----------ALL STAFF-------------- #
@login_required
def home():
    return render_template("home.html")


def about():
    return render_template('about.html')


def contact():
    return render_template('contact.html')


def list_member():
    return render_template('team.html')


def member_detail(id):
    member_info = service.get_staff_by_id(id)
    if member_info is None:
        return redirect(url_for('list_member'))

    role = service.check_role(id=member_info.maNV)
    return render_template("member_detail.html", member_info=member_info, role=str(role))


def appointment():
    return render_template('appointment.html')


def enroll_medical_exam():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        dob = request.form['dob']
        gender = True if request.form['gender'] == '1' else False
        address = request.form['address']
        date_schedule = request.form['date_schedule']
        time_id = request.form['time']
        rs = service.enroll_medical_exam(name=name, phone=phone, email=email, dob=dob, gender=gender, address=address,
                                         date_schedule=date_schedule, time_id=time_id)
        if type(rs) == str:
            flash("Đăng ký không thành công!", 'error')
        else:
            flash("Đăng ký lịch khám thành công!", 'success')
    return redirect(url_for("home"))


def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        tai_khoan = service.auth_user(username=username, password=password)
        if tai_khoan:
            login_user(user=tai_khoan)
            session['roles'] = str(current_user.user_role)
            if current_user.user_role == UserRole.ADMIN:
                return redirect("/admin")
            return redirect(url_for('home'))
        else:
            err_msg = 'Tài khoản hoặc mật khẩu không trùng khớp'
            return render_template("login.html", err_msg=err_msg)

    return render_template("login.html")


@login_required
def logout_my_user():
    logout_user()
    return redirect('/employee/login')


# NURSE
@login_required
def list_medical_exam():
    return render_template("list_medical_exam.html")


@login_required
def filter_all_patients():
    err_msg = ''
    date = request.form['date']
    if date == '':
        return redirect(url_for("list_medical_exam"))

    list_patients = service.get_all_patients_by_date(date=date)
    if len(list_patients) <= 0:
        err_msg = "Không có thông tin bệnh nhân!"
    return render_template("list_medical_exam.html", list_patients=list_patients, err_msg=err_msg, date=date)


def export_list_medical_exam(date):
    l = service.export_csv(date=date)
    return send_file(l)


@login_required
def account_page(id):
    err_user_msg = ''
    account_info = service.get_user_by_id(id)
    if account_info:
        user_info = service.get_user_info_by_id(id=account_info.maNV)
    else:
        user_info = None
    if request.method == 'POST':
        ma = id
        maNV = request.form['maNV']
        hoTen = request.form['hoTen']
        ngaySinh = request.form['ngaySinh']
        email = request.form['email']
        dienThoai = request.form['dienThoai']
        diaChi = request.form['diaChi']
        hinhAnh = ''

        if request.files:
            res = cloudinary.uploader.upload(request.files['hinhAnh'])
            hinhAnh = res['secure_url']

        try:
            service.update_user_info(maNV=maNV, hoTen=hoTen, ngaySinh=ngaySinh, email=email,
                                     dienThoai=dienThoai, diaChi=diaChi, hinhAnh=hinhAnh)
            flash("Cập nhật thành công!")
            return redirect("/employee/account/" + str(ma))
        except:
            err_user_msg = 'Đã có lỗi xảy ra! Vui lòng quay lại sau!'

    return render_template("account.html", id=id, account_info=account_info, user_info=user_info, err_user_msg=err_user_msg)


@login_required
def update_account(id):
    account_info = service.get_user_by_id(id)
    user_info = service.get_user_info_by_id(id=account_info.maNV)
    name = request.form['name']
    username = request.form['username']

    maNV = request.form['maNV']
    pwd = request.form['password']
    confirm = request.form['confirm']
    ma = id
    password = ''
    if pwd.__eq__(confirm):
        password = str(hashlib.md5(pwd.strip().encode('utf-8')).hexdigest())
        avatar = ''
        if request.files:
            res = cloudinary.uploader.upload(request.files['avatar'])
            print(res)
            avatar = res['secure_url']

        try:
            service.update_account_info(maNV=maNV, name=name, username=username, password=password, avatar=avatar)
            flash("Cập nhật thành công!")
            return redirect("/employee/account/" + str(ma))
        except:
            err_msg = 'Đã có lỗi xảy ra! Vui lòng quay lại sau!'
    else:
        err_msg = 'Mật khẩu KHÔNG khớp!'
    return render_template("account.html",id=id, err_msg=err_msg, user_info=user_info, account_info=account_info)


@login_required
def find_medicine():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', ITEMS_PER_PAGE, type=int)
    list_medicine = service.get_all_medicine_paginate(page=page, per_page=per_page)
    kw = request.args.get('kw')
    if kw is not None:
        list_medicine = service.find_medicine_by_name(kw=kw, page=page, per_page=per_page)
        return render_template('medicine.html', list_medicine=list_medicine)

    return render_template('medicine.html', list_medicine=list_medicine)


@login_required
def medicine_detail_page(maThuoc):
    medicine = service.get_medicine_by_id(maThuoc)
    return render_template('medicine_detail.html', medicine=medicine)


@login_required
def find_history_exam():
    if request.method == 'POST':
        maBN = request.form['maBN']
        if maBN != '':
            list_medical_reports = service.get_all_medical_reports_by_patient_id(id=maBN)
            if len(list_medical_reports) <= 0:
                flash("Không có phiếu khám nào!", 'error')
            return render_template('medical_report.html',
                                   list_medical_reports=list_medical_reports)

    return render_template('medical_report.html')


@login_required
def medical_report_detail(maPK):
    medical_report = service.get_medical_report_by_id(id=maPK)
    patient = service.get_patient_by_id(medical_report.maBN)
    medical_report_details = service.get_medical_report_detail_by_medical_report_id(id=maPK)
    return render_template('medical_report_detail.html',
                           medical_report=medical_report,
                           patient=patient,
                           medical_report_details=medical_report_details)


@login_required
def patient_info():
    if request.method == 'POST':
        id = request.form['maBN']
        patient = service.get_patient_by_id(id)
        if patient is None:
            flash("Không có thông tin bệnh nhân " + id, 'error')
        return render_template("patient-info.html", patient=patient)
    return render_template("patient-info.html")


@login_required
def create_medical_report():
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")
    medicines = service.get_all_medicines()
    if request.method == 'POST':
        maBN = request.form['maBN']
        ngayKham = request.form['ngayKham']
        trieuChung = request.form['trieuChung']
        chuanDoan = request.form['chuanDoan']
        cachDung = request.form.getlist('cachDung')
        soLuong = request.form.getlist('soLuong')
        thuoc = request.form.getlist('thuoc')
        try:
            service.save_medical_report(ngayKham=ngayKham, trieuChung=trieuChung, chuanDoan=chuanDoan, maBN=maBN,
                                        list_cach_dung=cachDung, list_so_luong=soLuong, list_thuoc=thuoc)
            flash("Lập phiếu khám thành công!", 'success')
            return redirect(url_for('create_medical_report'))
        except:
            flash("Lập phiếu khám thất bại", 'error')

    return render_template("create_medical_report.html", date=d1, medicines=medicines)


def find_patient_by_id(maBN):
    patient = service.get_patient_by_id(id=maBN)
    return jsonify(
        {'maBN': patient.maBN, 'hoTen': patient.hoTen}
    )


def api_get_all_medicines():
    medicines = service.get_all_medicines()
    return jsonify([
        {'maThuoc': m.maThuoc, 'tenThuoc': m.tenThuoc} for m in medicines
    ])


@login_required
def payment():
    if request.method == 'POST':
        id = request.form['maPK']
        is_paid = False
        if id != '':
            receipt = service.get_receipt_by_medical_report_id(id)
            if receipt:
                is_paid = True
                return render_template("payment.html", is_paid=is_paid)
            else:
                is_paid = False
            benh_nhan = None
            phieu_kham = service.get_medical_report_by_id(id=id)
            if phieu_kham is not None:
                benh_nhan = service.get_patient_by_id(id=phieu_kham.maBN)
            receipt_info = service.get_receipt_info(id)
            rule = service.get_rule_by_id(1)

            return render_template("payment.html", phieu_kham=phieu_kham, benh_nhan=benh_nhan,
                                   receipt_info=receipt_info, tien_kham=int(rule.giaTri), is_paid=is_paid)
    return render_template("payment.html")


@login_required
def get_pdf(maPK):
    receipt = service.get_receipt_by_medical_report_id(maPK=maPK)
    phieu_kham = service.get_medical_report_by_id(id=maPK)
    benh_nhan = None
    if phieu_kham is not None:
        benh_nhan = service.get_patient_by_id(id=phieu_kham.maBN)
    receipt_info = service.get_receipt_info(id=maPK)
    rule = service.get_rule_by_id(1)
    rendered = render_template("pdf.html", phieu_kham=phieu_kham, benh_nhan=benh_nhan,
                               receipt_info=receipt_info, tien_kham=int(rule.giaTri), created_date=datetime.now())
    pdf = pdfkit.from_string(rendered, False)
    response = make_response(pdf)
    response.headers['content-Type'] = 'application/pdf'
    response.headers['content-Disposition'] = 'inline; filename=invoice.pdf'
    return response


def pay():
    data = request.json
    try:
        service.create_receipt(data['tien_kham'], data['tien_thuoc'], data['tong_tien'], data['maPK'],
                               created_date=data['created_date'])
        return jsonify({'status': 200})
    except:
        return jsonify({'status': 400})


def ad_new_medicine():
    tenThuoc = request.form['tenThuoc']
    moTa = request.form['moTa']
    soLuong = int(request.form['soLuong'])
    giaBan = float(request.form['giaBan'])
    donVi = request.form['donVi']
    is_active = True if request.form['is_active'] == 'y' else False
    hinhAnh = ''
    if request.files:
        res = cloudinary.uploader.upload(request.files['hinhAnh'])
        hinhAnh = res['secure_url']

    try:
        service.create_new_medicine(tenThuoc, moTa, soLuong, giaBan, is_active, donVi, hinhAnh)
        flash("Create new medicine successfully!")

    except:
        flash("Create new medicine failed!", "error")
    return redirect("/admin/thuoc")


def ad_new_tai_khoan():
    name = request.form['name']
    username = request.form['username']
    pwd = request.form['password']
    password = str(hashlib.md5(pwd.strip().encode('utf-8')).hexdigest())
    is_active = True if request.form['is_active'] == 'y' else False
    maNV = int(request.form['maNV'])
    user_role = UserRole[request.form['user_role']]
    avatar = ''
    if request.files:
        res = cloudinary.uploader.upload(request.files['avatar'])
        avatar = res['secure_url']

    try:
        service.create_new_acc(name=name, username=username, password=password, is_active=is_active, avatar=avatar,
                               user_role=user_role, maNV=maNV)
        flash("Create new account successfully!")
    except:
        flash("Create new account failed!", "error")
    return redirect("/admin/taikhoan")
