import smtplib
from twilio.rest import Client

class Notifier:
    def __init__(self, email_config, sms_config):
        self.email_config = email_config
        self.sms_config = sms_config

    def send_email(self, job_details):
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(self.email_config["email"], self.email_config["password"])
            message = f"Subject: New Job Found\n\nJob Title: {job_details['title']}\nLink: {job_details['link']}"
            server.sendmail(self.email_config["email"], self.email_config["to_email"], message)

    '''def send_sms(self, job_details):
        client = Client(self.sms_config["account_sid"], self.sms_config["auth_token"])
        message = client.messages.create(
            body=f"New Job: {job_details['title']}\nLink: {job_details['link']}",
            from_=self.sms_config["from_phone"],
            to=self.sms_config["to_phone"]
        )'''
