import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = 'ram.chan7796@gmail.com'
email_password = '**********'
email_send = raw_input('Email : ')

subject = 'subject'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hi there, sending this email from Python!'
msg.attach(MIMEText(body,'plain'))

#filename='filename'
#attachment  =open(filename,'rb')

#part = MIMEBase('application','octet-stream')
#part.set_payload((attachment).read())
#encoders.encode_base64(part)
#part.add_header('Content-Disposition',"attachment; filename= "+filename)

#msg.attach(part)
try:
	text = msg.as_string()
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login(email_user,email_password)


	server.sendmail(email_user,email_send,text)
	server.quit()
except Exception as e:
	print(e)
