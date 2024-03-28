import tkinter
from gui.frames.add_password_page import AddPasswordDashboard

class MainDashboard(tkinter.Frame):

    def __init__(self) -> None:
        """
        The main dashboard frame.
        
        This object has all the attributes and functions from tkinter.Frame().
        - This frame represent a page/window.
        """
        super().__init__()
        
        

        self.create_password_button = tkinter.Button(self,text="New password",command=self.passwordStage)

        ## Pack everything ##
        self.create_password_button.pack()
        
    def passwordStage(self):
        """
        This method changes the frame to the passwords frame.
        """
        
        self.pack_forget() #Unpack the main dashboard frame
        AddPasswordDashboard(self.master).pack() #Show the password dashboard frame on the screen
        
        
        
    
 