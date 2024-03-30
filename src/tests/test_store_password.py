import pyodbc
from test_password_encryption import PasswordEncryption


class DataBase:


    def __init__(self,password_type,password) -> None:
            
        """
        This class represents the DataBase.

        It is used to store and read data from the DataBase.
        """
        #Get the database configuration data
        self.getDatabaseConfigurations()

        try:
            #Database configuration
            self.DRIVER = self.database_configurations.get("Driver")
            self.SERVER = self.database_configurations.get("Server")
            self.DATABASE = self.database_configurations.get("Database")

            #The connection string to connect to the sql server
            connection_string = (f"""
            DRIVER={self.DRIVER};
            SERVER={self.SERVER};
            DATABASE={self.DATABASE};
            Trust_Connection=yes;
            """)

            #Get the password and the password type from the user
            self.password = password
            self.password_type = password_type
            
            #Establish a connection to the DataBase
            self.conn = pyodbc.connect(connection_string)

            #Create a cursor object to execute SQL commands
            self.cursor = self.conn.cursor()
        except Exception as database_exception:
            print("Could not connect to the database:")
            print(database_exception)
            print()

    @classmethod
    def getDatabaseConfigurations(cls):
        try:
            ## Get database configuration data from the database_configuration file ##
            with open("data\\database_configurations.txt","r") as database_config_file:

                #Read data from the database configuration file
                fileData = database_config_file.read()
                lines = fileData.split("\n")
                
                #Initialize a dictonary that stores the database configuration data
                cls.database_configurations = {}

                #Iterate each line 
                for line in lines:
                    if ":" in line:
                        #Add the key and the value to the dictionary if the line contains colons ":"
                        key,value = line.split(":")
                        cls.database_configurations[key.strip()] = value.strip()

        except Exception as file_exception:
            print("File doesnt exist or empty:")
            print(file_exception, file_exception)
            print()


    def addPassword(self) -> None:
        """
        Store the password in the Database.
        """

        try:
            #Create password encryption object to encrypt the password
            password_encryption = PasswordEncryption(self.password)
            
            #Encrypt the password and the key
            encrypted_password = password_encryption.encryptPassword().decode()
            encrypted_key = password_encryption.encryptKey().decode()
            
            
            #Execute a SQL command to store the data in the database
            self.cursor.execute("INSERT INTO dbo.Passwords (PasswordType, Password,EncryptionKey) VALUES (?,?,?)",(self.password_type,encrypted_password,encrypted_key))
            
            #Push the data to the database
            self.cursor.commit() 

        except Exception as add_password_exception:
            print("Cannot add password to database:")
            print(add_password_exception)
            print()


    def getPassword(self,password_type:str):
        """
        Get the password from the database.

        return: password <str>
        
        if the password didn't retrieve - 
        return: 0 <int>
        """

        try:
            #Execute a SQL command to retrieve the encrypted password from the database
            self.cursor.execute(f"SELECT Password, EncryptionKey FROM Passwords WHERE PasswordType =?",password_type)

            #Execute a SQL command to retrieve the encryption key from the database
            encrypted_password,encrypted_key = self.cursor.fetchone()

            #Initialize password encryption object to decrypt the password and the key
            password_encryption = PasswordEncryption()
            
            #Decrypt the encrypted key and the encrypted password
            encryption_key = password_encryption.decryptKey(encrypted_key)
            password = password_encryption.decryptPassword(encrypted_password,encryption_key)

            return password
        
        except Exception as retrieve_password_exception:
            print("Cannot retrieve password from database:")
            print(retrieve_password_exception)
            print() 

            #Return 0 if the password didnt retrieve
            return 0 



