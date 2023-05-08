from config.celery import app
from decouple import config
from django.core.mail import send_mail


@app.task
def send_user_activation_link(email, activation_code):
    full_link = f'http://{config("ALLOWED_HOSTS").split(",")[1]}:{config("MAIN_PORT")}/api/v1/account/activate/{activation_code}'
    send_mail(
        'from Neobis_E-Store',
        f'Your activation link {full_link}',
        config('EMAIL_HOST_USER'),
        [email]
    )


@app.task
def send_forgot_password_code(email, activation_code):
    send_mail(
        'from Neobis_E-Store',
        f'Your code to change password {activation_code}',
        config('EMAIL_HOST_USER'),
        [email]
    )
