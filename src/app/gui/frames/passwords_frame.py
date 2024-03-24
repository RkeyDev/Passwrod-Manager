import tkinter

class PasswordsFrame(tkinter.Frame):
    def __init__(self,app_window) -> None:
        """
        The passwords frame.
        In this frame, there is a place to view the passwords and a place to add another password.
        This object has all the attributes and functions from tkinter.Frame().
        - This frame represent a page/window.
        """

        super().__init__(app_window)

        self.passwrods_label = tkinter.Label(self,text="New Frame")

        self.passwrods_label.pack()