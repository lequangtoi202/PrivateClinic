from datetime import date
from privateclinic.models import UserRole
from flask import render_template, request, redirect, url_for, flash, session, jsonify

from privateclinic import login, app, service
from privateclinic.admin import *
from flask_login import login_user, logout_user, login_required, current_user
import cloudinary.uploader

ITEMS_PER_PAGE = 6


# -----------CUSTOMER-------------- #
@app.route("/")
def index():
    return render_template('/customer/index.html')


@app.route('/about')
def cus_about():
    return render_template('/customer/about.html')


@app.route('/contact')
def cus_contact():
    return render_template('/customer/contact.html')


@app.route('/list_member')
def cus_list_member():
    return render_template('/customer/team.html')


@app.route('/appointment')
def cus_appointment():
    return render_template('/customer/appointment.html')


@app.route('/enroll_medical_exam', methods=['POST'])
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
@app.route('/employee/home')
@login_required
def home():
    return render_template("home.html")


@app.route('/employee/about')
def about():
    return render_template('about.html')


@app.route('/employee/contact')
def contact():
    return render_template('contact.html')


@app.route('/employee/list_member')
def list_member():
    return render_template('team.html')


@app.route('/employee/list_member/<id>')
def member_detail(id):
    member_info = service.get_staff_by_id(id)
    if member_info is None:
        return redirect(url_for('list_member'))

    role = service.check_role(id=member_info.maNV)
    return render_template("member_detail.html", member_info=member_info, role=str(role))


@app.context_processor
def common_attribute():
    list_times = service.get_list_times()
    list_members = service.get_all_doctor_and_nurse()
    list_medicine = service.get_all_medicine_paginate(1, ITEMS_PER_PAGE)
    return {
        'list_times': list_times,
        'list_members': list_members,
        'list_medicine': list_medicine
    }


@app.route('/employee/appointment')
def appointment():
    return render_template('appointment.html')


@app.route('/employee/enroll_medical_exam', methods=['POST'])
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


@app.route('/employee/login', methods=['POST', 'GET'])
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


@app.route('/employee/logout')
@login_required
def logout_my_user():
    logout_user()
    return redirect('/employee/login')


# NURSE
@app.route('/employee/create_list_medical_exam')
@login_required
def list_medical_exam():
    return render_template("list_medical_exam.html")


@app.route('/employee/filter', methods=['POST'])
@login_required
def filter_all_patients():
    err_msg = ''
    date = request.form['date']
    if date == '':
        return redirect(url_for("list_medical_exam"))

    list_patients = service.get_all_patients_by_date(date=date)
    if len(list_patients) <= 0:
        err_msg = "Không có thông tin bệnh nhân!"
    return render_template("list_medical_exam.html", list_patients=list_patients, err_msg=err_msg)


@app.route("/employee/account/<int:id>", methods=['POST', 'GET'])
@login_required
def account_page(id):
    err_user_msg = ''
    account_info = service.get_user_by_id(id)
    user_info = service.get_user_info_by_id(id)
    if request.method == 'POST':
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
            return redirect("/employee/account/" + maNV)
        except:
            err_user_msg = 'Đã có lỗi xảy ra! Vui lòng quay lại sau!'

    return render_template("account.html", account_info=account_info, user_info=user_info, err_user_msg=err_user_msg)


@app.route('/employee/update_acc/<int:id>', methods=['POST'])
@login_required
def update_account(id):
    user_info = service.get_user_info_by_id(id)
    account_info = service.get_user_by_id(id)
    name = request.form['name']
    username = request.form['username']
    import hashlib

    maNV = request.form['maNV']
    pwd = request.form['password']
    confirm = request.form['confirm']
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
            return redirect("/employee/account/" + maNV)
        except:
            err_msg = 'Đã có lỗi xảy ra! Vui lòng quay lại sau!'
    else:
        err_msg = 'Mật khẩu KHÔNG khớp!'
    return render_template("account.html", err_msg=err_msg, user_info=user_info, account_info=account_info)


@app.route('/employee/medicine', methods=['GET'])
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


@app.route('/employee/medicine/<int:maThuoc>')
@login_required
def medicine_detail_page(maThuoc):
    medicine = service.get_medicine_by_id(maThuoc)
    return render_template('medicine_detail.html', medicine=medicine)


@app.route('/employee/find-history-exam', methods=['POST', 'GET'])
@login_required
def find_history_exam():
    err_msg = ''
    if request.method == 'POST':
        maBN = request.form['maBN']
        if maBN != '':
            list_medical_reports = service.get_all_medical_reports_by_patient_id(id=maBN)
            if list_medical_reports is None:
                err_msg = "Không có phiếu khám nào!"
                list_medical_reports = None
            return render_template('medical_report.html',
                                   list_medical_reports=list_medical_reports,
                                   err_msg=err_msg)

    return render_template('medical_report.html')


@app.route('/employee/find-history-exam/<int:maPK>')
@login_required
def medical_report_detail(maPK):
    medical_report = service.get_medical_report_by_id(id=maPK)
    patient = service.get_patient_by_id(medical_report.maBN)
    medical_report_details = service.get_medical_report_detail_by_medical_report_id(id=maPK)
    return render_template('medical_report_detail.html',
                           medical_report=medical_report,
                           patient=patient,
                           medical_report_details=medical_report_details)


@app.route("/employee/patient-info", methods=['POST', 'GET'])
@login_required
def patient_info():
    if request.method == 'POST':
        id = request.form['maBN']
        patient = service.get_patient_by_id(id)
        return render_template("patient-info.html", patient=patient)
    return render_template("patient-info.html")


@app.route("/employee/create_medical_report", methods=['POST', 'GET'])
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
            service.save_medical_report(ngayKham=ngayKham, trieuChung=trieuChung, chuanDoan=chuanDoan, maBN=maBN, list_cach_dung=cachDung, list_so_luong=soLuong, list_thuoc=thuoc)
            flash("Lập phiếu khám thành công!", 'success')
            return redirect(url_for('create_medical_report'))
        except:
            flash("Lập phiếu khám thất bại", 'error')

    return render_template("create_medical_report.html", date=d1, medicines=medicines)


@app.route("/api/find_patient_by_id/<int:maBN>", methods=['GET'])
def find_patient_by_id(maBN):
    patient = service.get_patient_by_id(id=maBN)
    return jsonify(
        {'maBN': patient.maBN, 'hoTen': patient.hoTen}
    )


@app.route("/api/get_all_medicines", methods=['GET'])
def api_get_all_medicines():
    medicines = service.get_all_medicines()
    return jsonify([
        {'maThuoc': m.maThuoc, 'tenThuoc': m.tenThuoc} for m in medicines
    ])


@app.route("/employee/payment", methods=['POST', 'GET'])
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

            return render_template("payment.html", phieu_kham=phieu_kham, benh_nhan=benh_nhan, receipt_info=receipt_info, tien_kham=int(rule.giaTri), is_paid=is_paid)
    return render_template("payment.html")


@app.route("/api/employee/payment", methods=['POST'])
def pay():
    data = request.json
    try:
        service.create_receipt(data['tien_kham'], data['tien_thuoc'], data['tong_tien'], data['maPK'])
        return jsonify({'status': 200})
    except:
        return jsonify({'status': 400})


@login.user_loader
def load_user(user_id):
    return service.get_user_by_id(user_id)


if __name__ == '__main__':
    app.run(debug=True)
