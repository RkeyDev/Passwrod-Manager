from cryptography.fernet import Fernet


"""
-WARNING-

This script will create a main key that encrypt password keys.

Activate this script only once! If you will activate this script more
than once, you might lose access to your key and you will no longer
be able to decrypt your passwords.
"""


key = Fernet.generate_key() #Generate the encryption key

#Create a file stores the encryption key
with open("data\\encryption_key.txt","w") as encrypted_key_file:
    encrypted_key_file.write(key.decode())