from email.mime.text import MIMEText
from subprocess import Popen, PIPE

def send_email(from_users,to_users,subject,body):
    msg = MIMEText(body)
    msg["From"] = from_users
    msg["To"] = to_users
    msg["Subject"] = subject
    p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE, universal_newlines=True)
    p.communicate(msg.as_string())