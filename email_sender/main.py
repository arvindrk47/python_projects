import smtplib
import ssl

#Setting Up the port number and server name


smtp_port =587
smtp_server = "smtp.gmail.com"

email_from = "arvindrk47@gmail.com"
email_to = "arvindrk47@outlook.com"

pswd = "ihghquhgftehdapf"



message = "New Message"

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

