print("""        
         _            _   *
	|_  /\  /\   /_\  |  |
	|_ /  \/  \ /   \ |  |___ spammer
	""")
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
From = "bankriyad440@gmail.com"
password = '999888000'
To = input("\nEmail $ ")
msg = MIMEMultipart()
msg['From'] = From
msg['To'] = To
msg['Subject'] = input("\nTitle $ ")
body = input("\nSubject $ ")

X = input("\nLoop Y/N $ ")

if X == "Y":
    x = int(input("\nMany $ "))
    w = x + 1
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(From, password)
    text = msg.as_string()
    server.sendmail(From, To, text)
    y = [msg.attach(MIMEText(body, 'plain')), server.sendmail(From, To, text)]
    for i in range(1,w):
        server.sendmail(From, To, text)
        print(f'success spam {To}')
    server.quit()
elif X == "N":
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(From, password)
    text = msg.as_string()
    server.sendmail(From, To, text)
    print(f'success spam {To}')
    server.quit()
else:
    exit()