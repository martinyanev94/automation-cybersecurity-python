import smtplib
from email.mime.text import MIMEText

email_alert = True  # Set to True to enable email alerts
email_config = {
    'smtp_server': 'smtp.example.com',
    'smtp_port': 587,
    'from_email': 'alert@example.com',
    'to_email': 'admin@example.com',
    'username': 'smtp_user',
    'password': 'smtp_password'
}

def send_email_alert(message):
    if not email_alert:
        return

    msg = MIMEText(message)
    msg['Subject'] = 'Security Alert'
    msg['From'] = email_config['from_email']
    msg['To'] = email_config['to_email']

    try:
        with smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port']) as server:
            server.starttls()
            server.login(email_config['username'], email_config['password'])
            server.send_message(msg)
        print("Alert email sent successfully.")
    except Exception as e:
        print(f"Failed to send email alert: {e}")
