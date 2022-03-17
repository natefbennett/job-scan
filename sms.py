# idea from u/ForsakenOn3 https://www.reddit.com/r/Python/comments/8gb88e/free_alternatives_to_twilio_for_sending_text/

import secrets as s
import smtplib

carriers = {
	'att':    '@mms.att.net',
	'tmobile':' @tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com'
}

def send(message):
    # Replace the number with your own, or consider using an argument\dict for multiple people.
    to_number = f'{s.PHONE_NUMBER}{carriers[s.CARRIER]}'
    auth = (s.EMAIL, s.APP_PASSWORD)

    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP( "smtp.gmail.com", 587 )

    server.starttls()
    server.login(auth[0], auth[1])

    # Send text message through SMS gateway of destination number
    server.sendmail( auth[0], to_number, message)