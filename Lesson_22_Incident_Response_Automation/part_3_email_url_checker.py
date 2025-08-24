import email
import requests

def analyze_email(email_content):
    msg = email.message_from_string(email_content)
    subject = msg['subject']
    body = msg.get_payload(decode=True).decode()

    urls = extract_urls(body)  # hypothetical function to extract urls
    for url in urls:
        check_url(url)
        
def check_url(url):
    response = requests.get(url)
    if response.status_code != 200:
        notify_security_team(url)  # another hypothetical function
