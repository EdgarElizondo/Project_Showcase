import os
import smtplib, ssl


def send_email(email, message):
    host = "smtp.gmail.com"
    port = 465

    user_email = os.getenv("EMAIL_SHOWCASE")
    password = os.getenv("PASSWORD_SHOWCASE")
    
    context = ssl.create_default_context()

    receiver = os.getenv("EMAIL_SHOWCASE")
    message = f"""\
Subject: Message from Showcase
{message}


from: {email}
"""

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(user_email, password)
        server.sendmail(user_email, receiver, message)
