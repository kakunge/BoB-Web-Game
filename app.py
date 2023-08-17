from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import logging

# from objects import *
from database import *

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
app.secret_key = 'kldjfkdufuk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://msh070809:pwpw@localhost:3306/Account'
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "USER"
    userid = db.Column("userid",db.String(80), unique=True, nullable=False,primary_key=True)
    userpw = db.Column("userpw",db.String(120), nullable=False)

player = None

# @app.route('/')
# @app.route('/index')
    # return render_template("index.html")

@app.route('/')
@app.route('/index')
def print_index():
    global player
    player = Player(1, "Novice")
    return render_template("index.html")

@app.route('/1')
def print_1():
    return render_template("1.html")

@app.route('/battle')
def print_battle():
    monster = Monster("slime", 1, "Normal", "None", Reward(random.randint(1, 5), random.randint(1, 3)), pseudoslimestat_n)
    pve = BattlePVE(player, monster)
    pve.battle()
    return render_template("battle.html", player=player, monster=monster, pve=pve)

@app.route('/mypage')
def print_mypage():
    return render_template("mypage.html", player=player)

# ------------------


# def login():
#     return render_template('login.html')

# @app.route('/logout')
# def logout():
#     session.pop('user_id', None)  # 세션에서 사용자 정보 제거
#     return redirect(url_for('login'))
#
# @app.route('/signup')
# def signup():
#     return render_template('signup.html')
#
# # 로그인 검사
# @app.route('/login_check', methods=['POST'])
# def login_check():
#     if request.method == 'POST':
#         userid = request.form['userid']
#         userpw = request.form['userpw']
#         result = User.query.filter_by(userid=userid).first()
#         if result and result.userpw == userpw:
#             session['user_id'] = result.userid
#             app.logger.info("Login success")
#             return render_template('login.html', message='로그인 성공')
#         else:
#             app.logger.warning("Login failed")
#             return render_template('login.html', message='로그인 실패')
#
# # 회원가입 평가
# @app.route('/judge_signup', methods=['POST'])
# def judge_signup():
#     if request.method == 'POST':
#         userid = request.form['userid']
#         userpw = request.form['userpw']
#
#         lower_letter = any(c.islower() for c in userpw)
#         upper_letter = any(c.isupper() for c in userpw)
#         num_end = userid[-1].isdigit()
#         report = lower_letter & upper_letter & num_end
#
#         if report:
#             new_user = User(userid=userid, userpw=userpw)
#             db.session.add(new_user)
#             db.session.commit()
#             app.logger.info("Signup success")
#             return render_template('login.html', message='회원가입 성공')
#         else:
#             app.logger.warning("Signup failed")
#             return render_template('signup_judge.html', userid=userid, userpw=userpw, lower=lower_letter, upper=upper_letter, num_end=num_end, report=report)

# ...

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True, host='0.0.0.0', port=9990)
