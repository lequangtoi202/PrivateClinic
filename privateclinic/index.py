from flask import render_template, request, redirect
from privateclinic import db, login, app, dao
from flask_login import login_user


@app.route("/")
def index():
    list_times = dao.list_time()
    # dao.enroll_schedule_exam(name='Lê Quang Tới', phone='0868832530', email='quangtoile@gmail.com', dob='2002/09/25', gender=True, address='54, Dương Cát Lợi, thị trấn Nhà Bè', exam_date='2022-11-11', time_id=1)
    return render_template('index.html', list_times=list_times)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/list_member')
def list_member():
    list_members = dao.list_doctor_and_nurse()
    return render_template('team.html', list_members=list_members)


@app.route('/appointment')
def appointment():
    list_times = dao.list_time()
    return render_template('appointment.html', list_times=list_times)


@login.user_loader
def load_user(maNV):
    return dao.get_staff_by_id(maNV)


if __name__ == '__main__':
    app.run(debug=True)