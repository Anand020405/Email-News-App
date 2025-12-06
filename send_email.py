import smtplib, ssl


def send_email(mail_id, message):
    host = "smtp.gmail.com"
    port = 465

    username = "destroyer02042005@gmail.com"
    password = "ebakdjvjcbiixvfa"

    receiver = "destroyer02042005@gmail.com"
    context = ssl.create_default_context()

    message = f"""\
Subject: Newsletter - Todays NEWS

{message}"""

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user=username, password=password)
        server.sendmail(username, receiver, message)