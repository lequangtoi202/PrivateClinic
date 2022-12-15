from datetime import date, datetime
from privateclinic.models import UserRole
from flask import render_template, request, redirect, url_for, flash, session, jsonify, send_file, make_response
from privateclinic.admin import *
from privateclinic import login, app, service, admin, controllers
from flask_login import login_user, logout_user, login_required, current_user
import cloudinary.uploader
import pdfkit
import hashlib

ITEMS_PER_PAGE = 8


# -----------CUSTOMER-------------- #

app.add_url_rule("/", 'index', controllers.index)
app.add_url_rule('/about', 'cus_about', controllers.cus_about)
app.add_url_rule('/contact', 'cus_contact', controllers.cus_contact)
app.add_url_rule('/list_member', 'cus_list_member', controllers.cus_list_member)
app.add_url_rule('/appointment', 'cus_appointment', controllers.cus_appointment)
app.add_url_rule('/enroll_medical_exam', 'cus_enroll_medical_exam', controllers.cus_enroll_medical_exam, methods=['POST'])
# -----------ALL STAFF-------------- #
app.add_url_rule('/employee/home', 'home', controllers.home)
app.add_url_rule('/employee/about', 'about', controllers.about)
app.add_url_rule('/employee/contact', 'contact', controllers.contact)
app.add_url_rule('/employee/list_member', 'list_member', controllers.list_member)
app.add_url_rule('/employee/list_member/<id>', '/employee/list_member/<id>', controllers.member_detail)
app.add_url_rule('/employee/appointment', 'appointment', controllers.appointment)
app.add_url_rule('/employee/enroll_medical_exam', 'enroll_medical_exam', controllers.enroll_medical_exam, methods=['POST'])
app.add_url_rule('/employee/login', 'login_page', controllers.login_page, methods=['POST', 'GET'])
app.add_url_rule('/employee/logout', 'logout_my_user', controllers.logout_my_user)
# NURSE
app.add_url_rule('/employee/create_list_medical_exam', 'list_medical_exam', controllers.list_medical_exam)
app.add_url_rule('/employee/filter', 'filter_all_patients', controllers.filter_all_patients, methods=['POST'])
app.add_url_rule('/employee/list_medical_exam/export/<string:date>', '/employee/list_medical_exam/export/<string:date>',
                 controllers.export_list_medical_exam)
app.add_url_rule("/employee/account/<int:id>", 'account_page', controllers.account_page, methods=['POST', 'GET'])
app.add_url_rule('/employee/update_acc/<int:id>', '/employee/update_acc/<int:id>', controllers.update_account, methods=['POST'])
app.add_url_rule('/employee/medicine', 'find_medicine', controllers.find_medicine, methods=['GET'])
app.add_url_rule('/employee/medicine/<int:maThuoc>', '/employee/medicine/<int:maThuoc>', controllers.medicine_detail_page)
app.add_url_rule('/employee/find-history-exam', 'find_history_exam', controllers.find_history_exam, methods=['POST', 'GET'])
app.add_url_rule('/employee/find-history-exam/<int:maPK>', '/employee/find-history-exam/<int:maPK>',
                 controllers.medical_report_detail)
app.add_url_rule("/employee/patient-info", 'patient_info', controllers.patient_info, methods=['POST', 'GET'])
app.add_url_rule("/employee/create_medical_report", 'create_medical_report', controllers.create_medical_report,  methods=['POST', 'GET'])
app.add_url_rule("/api/find_patient_by_id/<int:maBN>", '/api/find_patient_by_id/<int:maBN>',
                 controllers.find_patient_by_id, methods=['GET'])
app.add_url_rule("/api/get_all_medicines", 'api_get_all_medicines', controllers.api_get_all_medicines, methods=['GET'])
app.add_url_rule("/employee/payment", 'payment', controllers.payment, methods=['POST', 'GET'])
app.add_url_rule("/employee/get_pdf/<maPK>", 'get_pdf', controllers.get_pdf)
app.add_url_rule("/api/employee/payment", 'pay', controllers.pay, methods=['POST'])
app.add_url_rule("/admin/thuoc/new", 'ad_new_medicine', controllers.ad_new_medicine, methods=['POST'])
app.add_url_rule("/admin/taikhoan/new", 'ad_new_tai_khoan', controllers.ad_new_tai_khoan, methods=['POST'])


@login.user_loader
def load_user(user_id):
    return service.get_user_by_id(user_id)


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


if __name__ == '__main__':
    app.run(debug=True)
