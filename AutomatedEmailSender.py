from email.message import EmailMessage
import regex
import smtplib

def getsender():
    sender_email=str(input("Enter Your Email address: "))
    sender_pass=str(input("Enter your Password: "))
    return sender_email,sender_pass

def send_email(file):  
    with open(file) as f:
        emails = f.readlines()
        sender_email , password =getsender()
        subject = str(input("Enter Subject: "))
        message = str(input("Enter Message: "))
        for email in emails:
            email=email.strip()
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, password)
                
                msg = EmailMessage()
                msg['Subject'] = subject
                msg['From'] = sender_email
                msg['To'] = email
                msg.set_content(message)
                server.sendmail(sender_email, email, msg.as_string())
                server.quit()  # Close the connection to the SMTP server
                print("Email sent successfully! to : "+ email )
            except Exception as e:
                print("Error sending email:", e)

    

path = r"C:\Users\Malik-Talha\Desktop\Emails.txt"
send_email(path)