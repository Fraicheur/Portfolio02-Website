import smtplib
import os
from flask import Flask, render_template, request, redirect, url_for

MAIL_ADDRESS = os.environ.get('EMAIL_FROM')
MAIL_APP_PW = os.environ.get('EMAIL_PASSWORD')

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        data = request.form
        name = data['name']
        name_utf8 = name.encode('utf-8')
        email_utf8 = data['email'].encode('utf-8')
        message_utf8 = data['message'].encode('utf-8')
        send_email(name_utf8, email_utf8, message_utf8)
        return render_template("index.html", message_sent=True, name=name)
    return render_template("index.html", message_sent=False)


def send_email(name, email, message):
    email_message = f"Subject:New Message from Portfolio website contact form\n\nName: {name}\nEmail: {email}\n\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MAIL_ADDRESS, MAIL_APP_PW)
        connection.sendmail(MAIL_ADDRESS, MAIL_ADDRESS, email_message)


if __name__ == '__main__':
    app.run(debug=False)
