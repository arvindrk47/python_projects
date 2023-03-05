import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os


smtp_port =587
smtp_server = "smtp.gmail.com"

email_from = input("Enter the sender Email id: ")
email_to = input("Enter the receiver email id")

pswd = input("Enter the password :- ")

subject = "Email with attachements"

def send_emails(email_to):
    for person in email_to:
        body = """"
           new message
           new message
           new message

        """
        msg = MIMEMultipart()
        msg['From']=  email_from
        msg['To'] = person
        msg['Subject']= subject

        msg.attach(MIMEText(body, 'plain'))
        filename =  "sample.csv"


        attachement = open(filename, 'rb')
        #Encode it as base64

        attachement_pack = MIMEBase('application', 'octet-stream')
        attachement_pack.set_payload((attachement).read())
        encoders.encode_base64(attachement_pack)
        attachement_pack.add_header('Content-Disposition', "attachment; filename= "+filename)
        msg.attach(attachement_pack)

        text=msg.as_string()


        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, email_to)
        print("Succesfully connected to server")

    TIE_server.quit()

send_emails(email_to)