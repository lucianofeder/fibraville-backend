from flask import Flask
from flask_mail import Mail


mail = Mail()

def init_app(app: Flask) -> None:
    mail.init_app(app)
    app.mail = mail