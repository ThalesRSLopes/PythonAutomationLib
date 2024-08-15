import os
from email.message import EmailMessage
import ssl
import smtplib
import keyring


class SendSmtpEmail:

    def __init__(self, email_sender, email_credential_name):
        self.email_sender = email_sender
        self.email_password = keyring.get_password(email_credential_name,email_sender)
        self.context = ssl.create_default_context()

    def send_email(self, email_receiver, subject, body):
        em = EmailMessage()
        em['From'] = self.email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=self.context) as smtpSender:
            smtpSender.login(self.email_sender, self.email_password)
            smtpSender.sendmail(self.email_sender, email_receiver, em.as_string())


mail_sender = SendSmtpEmail("thalesrslopes@gmail.com","thalesrslopesgmail")
mail_sender.send_email("thalesrslopes@gmail.com","e-mail teste", "Testando o envio de e-mails com Python")
