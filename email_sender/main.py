import smtplib
import ssl

#Setting Up the port number and server name


smtp_port =587
smtp_server = "smtp.gmail.com"

print("Hi, This script works on gmail webservice (which means sender mail id should be an gmail )")

email_from = input("Enter the send mail id: ")
email_to = input("Enter the receiver email id:- ")

pswd = input("Enter the password")



message = input("Enter the message ")

context = ssl.create_default_context()


try:
    print("Connecting to server ....")
    TIE_server = smtplib.SMTP(smtp_server,smtp_port)
    TIE_server.starttls(context=context)
    TIE_server.login(email_from, pswd)
    print("Connected to server :-")

    print()
    print(f"Sending email to -{email_to}")

    TIE_server.sendmail(email_from,email_to,message)

    print(f"Email sent to {email_to}")

except Exception as e:
    print(e)

finally:
    TIE_server.quit()

