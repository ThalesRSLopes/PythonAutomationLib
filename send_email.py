import os
from email.message import EmailMessage
import ssl
import smtplib


class SendSmtpEmail:

    def __init__(self, email_sender, email_password):
        self.email_sender = email_sender
        self.email_password = email_password
        self.context = ssl.create_default_context()

    def send_email(self, email_receiver, subject, body):
        em = EmailMessage()
        em['From'] = self.email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)
