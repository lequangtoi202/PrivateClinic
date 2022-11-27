from privateclinic import app, service, db
from privateclinic.models import NhanVien, ThoiGian, BacSi, Yta, DanhSachKhamBenh, \
    ChiTietDSKham, BenhNhan, TaiKhoan, Thuoc, PhieuKham, PhieuKham_Thuoc, QuiDinh, HoaDon, UserRole
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose
from flask import redirect
from flask_login import logout_user, current_user

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


class ThuocView(AuthenticatedModelView):
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


class QuiDinhView(AuthenticatedModelView):
    can_export = True
    column_filters = ['tenQD', 'giaTri']
    column_searchable_list = ['tenQD', 'giaTri']
    page_size = 6
    column_labels = {
        'tenQD': 'Tên qui định',
        'giaTri': 'Giá trị'

    }


class PhieuKhamView(AuthenticatedModelView):
    can_export = True
    column_filters = ['trieuChung', 'chuanDoan']
    column_searchable_list = ['trieuChung', 'chuanDoan']
    page_size = 6
    column_labels = {
        'ngayKham': 'Ngày khám',
        'trieuChung': 'Triệu chứng',
        'chuanDoan': 'Chuẩn đoán'

    }


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
        return self.render('admin/stats.html')


# admin.add_view(QuiDinhView(QuiDinh, db.session, name='Qui định'))
# admin.add_view(AuthenticatedModelView(ThoiGian, db.session, name='Thời gian làm việc'))
admin.add_view(NhanVienView(NhanVien, db.session, name='Nhân viên'))
admin.add_view(TaiKhoanView(TaiKhoan, db.session, name='Tài khoản'))
admin.add_view(BenhNhanView(BenhNhan, db.session, name='Bệnh nhân'))
admin.add_view(ThuocView(Thuoc, db.session, name='Thuốc'))
admin.add_view(PhieuKhamView(PhieuKham, db.session, name='Phiếu khám bệnh'))
admin.add_view(AuthenticatedModelView(DanhSachKhamBenh, db.session, name='Danh sách khám bệnh'))
admin.add_view(HoaDonView(HoaDon, db.session, name='Hóa đơn'))
admin.add_view(AuthenticatedModelView(BacSi, db.session, name='Bác sĩ'))
admin.add_view(AuthenticatedModelView(Yta, db.session, name='Y tá'))
admin.add_view(AuthenticatedModelView(PhieuKham_Thuoc, db.session, name='Chi tiết phiếu khám'))
admin.add_view(StatsView(name='Thống kê'))
admin.add_view(LogoutView(name='Đăng xuất'))
