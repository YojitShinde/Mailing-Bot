import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

print("Enter Receiver's Email:")
receiver_mail = input()
sender_mail = ''
sender_password = ''

html_file = open('email.html', 'r')
mail_content = html_file.read()
message = MIMEMultipart('alternative')
message['From'] = sender_mail
message['To'] = receiver_mail
message['Subject'] = 'Software Developer Application'
message.attach(MIMEText(mail_content, 'html'))

filename = "YojitShinde-Resume.pdf"
resume = MIMEApplication(open(filename, 'rb').read())
resume.add_header('Content-Disposition','attachment', filename = 'YojitShinde-Resume.pdf')
message.attach(resume)

session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender_mail, sender_password)
text = message.as_string()
session.sendmail(sender_mail, receiver_mail, text)
session.quit()
print('Mail Sent')
