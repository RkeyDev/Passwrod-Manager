from cryptography.fernet import Fernet

class Password:
    def __init__(self,password:str) -> None:
        """
        This class represents the password itself. it's includes methods like encrypt/decrypt the password,
        and other methods you can perform on the password.
        """

        self.password = password #Get the password from the user

        self.key = Fernet.generate_key() #Generate the encryption key


        #Create a cypher object with the key
        self.cypher = Fernet(self.key)

    
    def getGeneralEncryptionKey(self):
        """
        Get the general encryption key from the encryption key file.

        return: general_encryption_key <bytes>
        """

        with open("data\\encryption_key.txt","r") as encryption_key_file:
            #Get the general encryption key from the encrypted key file
            general_encryption_key = encryption_key_file.read()
        
        return general_encryption_key

        


    def encryptKey(self):
        """
        Encrypt the encryption key.

        return: encrypted_key <bytes>
        """

        general_encryption_key = self.getGeneralEncryptionKey()
        encrypted_key = Fernet(general_encryption_key).encrypt(self.key)

        return encrypted_key




    def decryptKey(self,encrypted_key:bytes):
        """
        Decrypt the encryption key.

        return: encryption_key <bytes>
        """

        general_encryption_key = self.getGeneralEncryptionKey()

        encryption_key = Fernet(general_encryption_key).decrypt(encrypted_key)

        return encryption_key




    def encryptPassword(self):
        """
        Encrypt the password.

        return: encrypted_password <bytes>
        """
        encrypted_password = self.cypher.encrypt(self.password.encode())

        return encrypted_password



    def decryptPassword(self,encrypted_password:bytes):
        """
        Decrypt the password.

        return: decrypted_password <str>
        """
        decrypted_password = self.cypher.decrypt(encrypted_password).decode()
        
        return decrypted_password