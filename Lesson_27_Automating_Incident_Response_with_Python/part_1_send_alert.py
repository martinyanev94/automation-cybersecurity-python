import smtplib
from email.mime.text import MIMEText

def send_alert(email_recipient, issue_description):
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'your_email@example.com'
    smtp_password = 'your_password'

    msg = MIMEText(issue_description)
    msg['Subject'] = 'Security Incident Alert'
    msg['From'] = smtp_username
    msg['To'] = email_recipient

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, email_recipient, msg.as_string())
        server.quit()
        print(f"Alert sent to {email_recipient}")
    except Exception as e:
        print(f"Error sending alert: {e}")
