from privateclinic import app, service, db
from privateclinic.models import NhanVien, BenhNhan, TaiKhoan, Thuoc, HoaDon, UserRole
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose
from flask import redirect, request
from flask_login import logout_user, current_user
from datetime import datetime

admin = Admin(app=app, name='MEDINOVA', template_mode='bootstrap4')


class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN


class AuthenticatedView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class NhanVienView(AuthenticatedModelView):
    can_export = True
    column_filters = ['hoTen']
    column_searchable_list = ['hoTen', 'diaChi', 'dienThoai', 'email']
    page_size = 6
    column_labels = {
        'hoTen': 'Họ và tên',
        'diaChi': 'Địa chỉ',
        'dienThoai': 'Điện thoại',
        'ngaySinh': 'Ngày sinh',
        'hinhAnh': 'Hình ảnh'
    }


class TaiKhoanView(AuthenticatedModelView):
    can_export = True
    column_filters = ['username']
    column_searchable_list = ['username', 'name', 'user_role']
    page_size = 6
    column_labels = {
        'name': 'Tên hiển thị'
    }

    create_template = '/admin/create_acc.html'

    @expose('/new/')
    def create_view(self):
        self._template_args['staffs'] = service.get_all_staff()
        self._template_args['user_role'] = service.get_all_role()
        return super(TaiKhoanView, self).create_view()


class BenhNhanView(AuthenticatedModelView):
    can_export = True
    column_filters = ['hoTen', 'dienThoai']
    column_searchable_list = ['hoTen', 'dienThoai', 'diaChi']
    page_size = 6
    column_labels = {
        'hoTen': 'Họ tên',
        'dienThoai': 'Điện thoại',
        'diaChi': 'Địa chỉ',
        'gioiTinh': 'Giới tính',

    }


class ThuocView(AuthenticatedModelView, BaseView):
    can_export = True
    column_filters = ['tenThuoc', 'moTa']
    column_searchable_list = ['tenThuoc', 'moTa']
    page_size = 6
    column_labels = {
        'tenThuoc': 'Tên thuốc',
        'moTa': 'Mô tả',
        'soLuong': 'Số lượng',
        'giaBan': 'Giá bán',
        'donVi': 'Đơn vị',
        'hinhAnh': 'Hình Ảnh'

    }
    create_template = '/admin/create_me.html'


class HoaDonView(AuthenticatedModelView):
    can_export = True
    page_size = 6
    column_labels = {
        'tienThuoc': 'Tiền thuốc',
        'tienKham': 'Tiền khám',
        'tongTien': 'Tổng tiền'

    }


class LogoutView(AuthenticatedView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/employee/login')


class StatsView(AuthenticatedView):
    @expose('/')
    def index(self):
        year = request.args.get('year', default=datetime.now().year)

        year1 = request.args.get('year1', default=datetime.now().year)

        month = request.args.get('month', default=datetime.now().month)

        year2 = request.args.get('year2', default=datetime.now().year)

        month2 = request.args.get('month2', default=datetime.now().month)

        return self.render('admin/stats.html',
                           month_stats=service.revenue_stats(year=year),
                           exam_frequancy=service.medical_exam_frequency_stats(month=month, year1=year1),
                           revenue_by_month=service.revenue_by_month(year=year1, month=month),
                           medicine_using=service.medicine_using_stats(year=year2, month=month2)
                           )


admin.add_view(NhanVienView(NhanVien, db.session, name='Nhân viên'))
admin.add_view(TaiKhoanView(TaiKhoan, db.session, name='Tài khoản'))
admin.add_view(BenhNhanView(BenhNhan, db.session, name='Bệnh nhân'))
admin.add_view(ThuocView(Thuoc, db.session, name='Thuốc'))
admin.add_view(HoaDonView(HoaDon, db.session, name='Hóa đơn'))
admin.add_view(StatsView(name='Thống kê'))
admin.add_view(LogoutView(name='Đăng xuất'))
