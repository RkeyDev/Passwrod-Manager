import tkinter
from encrypt_password import Password

class AddPasswordDashboard(tkinter.Frame):
    def __init__(self,app_window: tkinter.Tk) -> None:
        """
        The passwords frame.
        In this frame, there is a place to view the passwords and a place to add another password.
        This object has all the attributes and functions from tkinter.Frame().
        - This frame represent a page/window.
        """

        super().__init__(app_window)

        ## Create the components of the frame ##
        self.add_password_label = tkinter.Label(self,text="Enter Password") #Label
        self.password_entry = tkinter.Entry(self,textvariable="add password") #Entry (input)
        self.add_password_button = tkinter.Button(self,command=self.addPassword) #Button
        
        ## Configure components ##
        self.add_password_button.config(width=10,text="Add password")

        ## Pack everything ##
        self.add_password_label.pack()
        self.password_entry.pack()
        self.add_password_button.pack()

        
    
    def addPassword(self):
        """
        Adds the password to the data base after encryption
        """
        #Get the password from the entry (input)
        self.password = Password(self.password_entry.get())
          

    