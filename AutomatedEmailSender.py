from email.message import EmailMessage
import regex
import smtplib

def getsender():
    """Get email and password from user and returns same."""
    sender_email=str(input("Enter Your Email address: "))
    sender_pass=str(input("Enter your Password: "))
    return sender_email,sender_pass

def send_email(file):  
    """ Takes a text file as input (contains one email per line). Scan the file and asks user to enter email and password. Then user enters
    subject and Body of email. A confirmation is received after email sent."""
    with open(file) as f:
        emails = f.readlines()
        sender_email , password =getsender()
        subject = str(input("Enter Subject: "))
        message = str(input("Enter Message: "))
        recipients = [email.strip() for email in emails if email.strip()]
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
                
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = sender_email
            msg['To'] = ', '.join(recipients)
            msg.set_content(message)
            server.sendmail(sender_email, recipients, msg.as_string())
            server.quit()  # Close the connection to the SMTP server
            print("Email sent successfully! " )
        except Exception as e:
            print("Error sending email:", e)

    

path = r"path/to/text file that contain emails(one per line)"
send_email(path)