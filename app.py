# coding=utf-8/gbk

from flask import Flask, request, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = '2844724493@qq.com'
app.config['MAIL_PASSWORD'] = 'PWD'
app.config['MAIL_DEFAULT_SENDER'] = 'SENDER'

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/confirm-rent/', methods=['GET', 'POST'])
def confirm_rent():
    error = None
    if request.method == 'POST':
        try:
            content = "姓名：" + request.form['name'] \
                      + "\n称谓：" + request.form['title'] \
                      + "\n单位：" + request.form['unit'] \
                      + "\n地址：" + request.form['position'] \
                      + "\n电话：" + request.form['tel'] \
                      + "\n邮件：" + request.form['mail'] \
                      + "\n设备：" + request.form['device'] \
                      + "\n目标海域：" + request.form['tarOcean'] \
                      + "\n深度：" + request.form['depth'] \
                      + "\n起始日期：" + request.form['initdate'] \
                      + "\n归还日期：" + request.form['findate'] \
                      + "\n备注：" + request.form['comment']

            msg = Message(subject='收到新租赁设备请求',
                          body=content,
                          recipients=["RECIPIENT"])
            mail.send(msg)
            return render_template('confirm-rent.html', error=error,
                                   name=request.form['name'],
                                   title=request.form['title'],
                                   unit=request.form['unit'],
                                   position=request.form['position'],
                                   tel=request.form['tel'],
                                   mail=request.form['mail'],
                                   device=request.form['device'],
                                   tarOcean=request.form['tarOcean'],
                                   depth=request.form['depth'],
                                   initdate=request.form['initdate'],
                                   findate=request.form['findate'],
                                   comment=request.form['comment'] if request.form['comment'] != '' else '（无）')
        except Exception as e:
            return render_template('fail-rent.html')
    else:
        return render_template('fail-rent.html')


@app.route('/confirm-present/', methods=['GET', 'POST'])
def confirm_present():
    error = None
    if request.method == 'POST':
        try:
            content = "姓名：" + request.form['name'] \
                      + "\n称谓：" + request.form['title'] \
                      + "\n单位：" + request.form['unit'] \
                      + "\n电话：" + request.form['tel'] \
                      + "\n邮件：" + request.form['mail'] \
                      + "\n场次：" + request.form['serial'] \
                      + "\n备注：" + request.form['comment']
            msg = Message(subject='收到新参会报名信息',
                          body=content,
                          recipients=["RECIPIENT"])
            mail.send(msg)
            return render_template('confirm-present.html', error=error,
                                   serial=request.form['serial'],
                                   name=request.form['name'],
                                   title=request.form['title'],
                                   unit=request.form['unit'],
                                   tel=request.form['tel'],
                                   mail=request.form['mail'],
                                   comment=request.form['comment'] if request.form['comment'] != '' else '（无）')
        except Exception as e:
            return render_template('fail-present.html')
    else:
        return render_template('fail-rent.html')


if __name__ == '__main__':
    app.run(debug=False)
