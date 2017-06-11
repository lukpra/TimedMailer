import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mailer():
    def __init__(self, log, adress, login, password, smpt_adress = 'smpt.gmail.com', smpt_port = '587'):
        self.log = log
        self.adress = adress
        self.login = login
        self.password = password
        self.smpt_adress = smpt_adress
        self.smpt_port = smpt_port

        self.msg = None
        self.to = None
        configure_message(message_headers):
        self.log.info("Mail sender has been sucessfully created for user: %s, for smpt server: %s : %s" % [self.login, self.smpt.adress, self.smpt.port])

    def configure_message(message_headers):
        if message_headers is None:
            log.error("Could not re-configure message for user: %s . Message headers are empty!" % self.login)
            break
        msg = MIMEMultipart()
        msg['From'] = message_headers.get(self.adress)
        msg['To'] = message_headers.get(to)
        msg['Subject'] = message_headers.get(subject)
        message = message_headers.get(message)
        msg.attach(MIMEText(message))
        self.msg = msg
        self.to = message_headers.get(to)

    def send():
        mailserver = smtplib.SMTP(self.smpt_adress, self.smpt_port)
        # identify ourselves to smtp client
        mailserver.ehlo()
        # secure our email with tls encryption
        mailserver.starttls()
        # re-identify ourselves as an encrypted connection
        mailserver.ehlo()
        mailserver.login(self.login, self.password)

        mailserver.sendmail(self.adress, self.to, self.msg.as_string())
                                          
        mailserver.quit()
                                          
