import smtplib
from config import *


server = smtplib.SMTP_SSL(mail_srv, port)
server.set_debuglevel(1)
server.login(fromaddr, password)
server.sendmail(fromaddr, toaddrs, 'test')
server.quit()

