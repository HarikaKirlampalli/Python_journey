import smtplib
import ssl
from email.message import EmailMessage
sender_email = "kirlampalliharika@gmail.com"
password = "dmtf seju gfru ckzo"
receiver_email = "layatrimurakada@gmail.com"
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["subject"] = "Welcome Mail"
message.set_content(f""""
Hello Layatri..
Welcome welcome welcome..

Regards,
Harika
""")
context = ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com",port =587) as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.ehlo()
    smtp.login(sender_email,password)
    smtp.send_message(message)
