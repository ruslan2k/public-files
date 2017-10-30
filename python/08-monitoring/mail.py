import smtplib
from email.mime.text import MIMEText
from config import *

msg = MIMEText('test')
msg['Subject'] = '- test -'
msg['From'] = fromaddr

server = smtplib.SMTP_SSL(mail_srv, port)
server.set_debuglevel(1)
server.login(fromaddr, password)
server.sendmail(fromaddr, toaddrs, msg.as_string())
server.quit()

