import bcrypt

password = input('Password')
newpassword = bcrypt.hashpw(password, 10)

print(newpassword)
