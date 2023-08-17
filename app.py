from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://msh070809:pwpw@localhost:3306/Account'
db = SQLAlchemy(app)


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)  # 세션에서 사용자 정보 제거
    return redirect(url_for('index'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def login():
    return render_template('signup.html')

#id가 틀렸는지 pw가 틀렸는지 알려줘야 하지만 시간 관계상 생략
#로그인 검사 db에 데이터가 있으면 세션 추가 후 login화면 전환 ,없을경우 something출력
@app.route('/login_check', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        from model import User
        userid  = request.form['userid']
        userpw = request.form['userpw']

        result = User.query.fillter_by(userid=userid).first()
        if result and check_password_hash(result.userpw, userpw):
            session['user_id'] = result.userid
            return render_template('login.html')
    return "something, problem"


@app.route('/judge_signup', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        from model import User
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

        return render_template('signup_judge.html', userid=userid, userpw=userpw, lower=lower_letter, upper=upper_letter, num_end=num_end, report=report)
    
    # GET 요청일 경우, 폼을 보여줍니다.
    return render_template('signup_judge.html', userid='', userpw='', lower=False, upper=False, num_end=False, report=False)


if __name__ == '__main__':
    app.run(debug=True)