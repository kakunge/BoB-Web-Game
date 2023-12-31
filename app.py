from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import logging

# from objects import *
from database import *

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
app.secret_key = 'kldjfkdufuk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test:1234@localhost:3306/Game'
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "User"
    userid = db.Column("userid",db.String(80), unique=True, nullable=False,primary_key=True)
    userpw = db.Column("userpw",db.String(120), nullable=False)

player = None

@app.route('/')
@app.route('/start')
def start():
    global player
    player = Player(1, "Novice")
    # return render_template("index.html")

    if 'user_id' in session:
        # 세션에 user_id가 있으면 로그인 상태로 간주하여 로그인 이후의 동작을 수행합니다.
        user_id = session['user_id']
        return render_template('start.html', flag=1)
    # 세션에 user_id가 없으면 비로그인 상태로 간주하여 로그인 이전의 동작을 수행합니다.
    return render_template('start.html', flag=0)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/battle')
def print_battle():
    monster = Monster("slime", 1, "Normal", "None", Reward(random.randint(1, 5), random.randint(1, 3)), pseudoslimestat_n)
    pve = BattlePVE(player, monster)
    pve.battle()
    return render_template("battle.html", player=player, monster=monster, pve=pve)

@app.route('/mypage')
def print_mypage():
    return render_template("mypage.html", player=player)

@app.route('/revive')
def print_revive():
    player.revive()
    return render_template("revive.html")

@app.route('/equipexc')
def print_equipexc():
    player.EquipExc()
    return render_template("equipexc.html")

@app.route('/unequip')
def print_unequip():
    player.unequip(1)
    return render_template("unequip.html")

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
            return render_template('start.html', flag=1)
        else:
            app.logger.warning("Login failed")
            return render_template('start.html', flag=0)

# # 회원가입 평가
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
