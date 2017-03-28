import smtplib

from email.mime.text import MIMEText

USER = 'user'
PASS = 'password'

sender = 'yitz.dash@mail.ru'
receivers = ['yitzhak@razorgrip.com']

message ="""From: Yechezkel <idashevsky@gmail.com>
To: Yitzhak <yitzhak@razorgrip.com>
Subject: SMTP e-mail test

This is a test e-mail message.
""" 
# yechezkelp@bet-el.muni.il
try:
	smtpObj = smtplib.SMTP('smtp.mail.ru:587')
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login(USER,password)
	smtpObj.sendmail(sender, receivers, message)
	print "Successfully sent email"
#except SMTPException:
	#print "Error: unable to send email"
except Exception:
	print "some error"
	raise

