from cryptography.fernet import Fernet as fernet

key = fernet.generate_key()
print(key)
file = open('key.key', 'wb')
file.write(key)
file.close()
