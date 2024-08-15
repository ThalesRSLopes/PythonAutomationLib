import os
from email.message import EmailMessage
import ssl
import smtplib
import keyring
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendSmtpEmail:

    def __init__(self, email_sender, email_credential_name):
        # Define o endereço de email que será utilizado para enviar as mensagens
        self.email_sender = email_sender

        # Obtém a senha salva no Gerenciador de Credenciais do Windows
        # O primeiro argumento é o nome da credencial salva e o segundo é o usuário salvo na credencial
        self.email_password = keyring.get_password(email_credential_name,email_sender)

        # Cria e configura um contexto SSL/TLS com as configurações padrão seguras
        self.context = ssl.create_default_context()

    def send_email(self, email_receiver, subject, body):
        # Criação da variável email message, que é do tipo MIMEMultipart
        # A classe MIMEMultipart permite que se possa construir e manipular mensagens de e-mail complexas que incluem várias seções de dados
        em = MIMEMultipart("alternative")

        # Define o remetente, destinatário, assunto e o corpo da mensagem de e-mail, no formato HTML
        em['From'] = self.email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.attach(MIMEText(body,"html"))

        # Se conecta ao servidor de e-mail, realiza o login e envia a mensagem
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=self.context) as smtpSender:
            smtpSender.login(self.email_sender, self.email_password)
            smtpSender.sendmail(self.email_sender, email_receiver, em.as_string())


if __name__ == "__main__":
    mail_body = """
        <html>
            <body>
                <p>Olá,<br>
                    Acesse o site abaixo:</p>
                <p><a href="https://www.youtube.com/">Youtube</a></p>
                <p> Atenciosamente, <strong>PythonBot</strong></p>
            </body>
        </html>
    """
    mail_sender = SendSmtpEmail("thalesrslopes@gmail.com", "thalesrslopesgmail")
    mail_sender.send_email("thalesrslopes@gmail.com", "e-mail teste", mail_body)
