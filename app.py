from threading import Thread

from flask import Flask, request, render_template
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.qq.com',
    MAIL_PORT=465,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='2159039028@qq.com',
    MAIL_PASSWORD='',  # 授权码
)

mail = Mail(app)


def send_async_email(app, msg):
    mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)  # sender 发送方邮箱，recipients 接受方邮箱列表
    msg.body = text_body  # 纯文本信息
    msg.html = html_body  # HTML格式的信息
    Thread(target=send_async_email, args=(app, msg)).start()


@app.route('/confirm-rent/', methods=['GET', 'POST'])
def confirm_rent():
    error = None
    if request.method == 'POST':
        send_email('test subject', app.config['2159039028@qq.com'], ['317576256@qq.com'],
                   f"姓名：{request.form['name']}\n"
                   f"称谓：{request.form['title']}\n"
                   f"单位：{request.form['unit']}\n"
                   f"地址：{request.form['position']}\n"
                   f"电话：{request.form['tel']}\n"
                   f"邮件：{request.form['mail']}\n"
                   f"设备：{request.form['device']}\n"
                   f"目标海域：{request.form['tarOcean']}\n"
                   f"深度：{request.form['depth']}\n"
                   f"起始日期：{request.form['initdate']}\n"
                   f"归还日期：{request.form['findate']}\n")

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
                               findate=request.form['findate'])


@app.route('/confirm-present/', methods=['GET', 'POST'])
def confirm_present():
    error = None
    if request.method == 'POST':
        send_email('收到新的参会登记', app.config['MAIL_USERNAME'], ['xxx@qq.com'], 'text body', '<b>HTML</b> body')
        return render_template('confirm-present.html', error=error,
                               serial=request.form['serial'],
                               name=request.form['name'],
                               title=request.form['title'],
                               unit=request.form['unit'],
                               tel=request.form['tel'],
                               mail=request.form['mail'])


if __name__ == '__main__':
    app.run(debug=False)
