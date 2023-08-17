from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import logging

# from objects import *
from database import *

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
app.secret_key = 'kldjfkdufuk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://msh070809:pwpw@localhost:3306/Game'
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "User"
    userid = db.Column("userid",db.String(80), unique=True, nullable=False,primary_key=True)
    userpw = db.Column("userpw",db.String(120), nullable=False)

player = None
monster = None

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    if 'user_id' in session:
        # 세션에 user_id가 있으면 로그인 상태로 간주하여 로그인 이후의 동작을 수행합니다.
        user_id = session['user_id']
        return f'로그인된 사용자: {user_id}'
    # 세션에 user_id가 없으면 비로그인 상태로 간주하여 로그인 이전의 동작을 수행합니다.
    return '로그인되지 않은 상태'

@app.route('/logout')
def logout():
    session.pop('user_id', None)  # 세션에서 사용자 정보 제거
    return redirect(url_for('login'))

@app.route('/signup')
def signup():
    return render_template('signup.html')

# 로그인 검사
@app.route('/login_check', methods=['POST'])
def login_check():
    if request.method == 'POST':
        userid = request.form['userid']
        userpw = request.form['userpw']
        result = User.query.filter_by(userid=userid).first()
        if result and result.userpw == userpw:
            session['user_id'] = result.userid
            app.logger.info("Login success")
            return render_template('login.html', message='로그인 성공')
        else:
            app.logger.warning("Login failed")
            return render_template('login.html', message='로그인 실패')

# 회원가입 평가
@app.route('/judge_signup', methods=['POST'])
def judge_signup():
    if request.method == 'POST':
        userid = request.form['userid']
        userpw = request.form['userpw']

        lower_letter = any(c.islower() for c in userpw)
        upper_letter = any(c.isupper() for c in userpw)
        num_end = userid[-1].isdigit()
        report = lower_letter & upper_letter & num_end

        if report:
            new_user = User(userid=userid, userpw=userpw)
            db.session.add(new_user)
            db.session.commit()
            app.logger.info("Signup success")
            return render_template('login.html', message='회원가입 성공')
        else:
            app.logger.warning("Signup failed")
            return render_template('signup_judge.html', userid=userid, userpw=userpw, lower=lower_letter, upper=upper_letter, num_end=num_end, report=report)


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True, host='0.0.0.0', port=9990)
