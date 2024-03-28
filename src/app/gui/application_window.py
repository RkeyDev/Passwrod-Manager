import tkinter
from gui.frames.main_dashboard import  MainDashboard

## Window configurations ##
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800


class AppWindow(tkinter.Tk):

    def __init__(self) -> None:
        """
        Initialize  window.
        This object has all the attributes and functions from tkinter.Tk().
        """

        super().__init__()

        ## Window installation ##
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}") #Set the size of the window
        self.title("Password manager")
        
        ## Pack frames ##
        MainDashboard().pack()

    
        
        





    
    

        

        

