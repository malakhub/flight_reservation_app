# Main application file
from tkinter import *
import os 
import sys

#import modules from my own files
from home import HomePage
from database import setup_database

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def main():
    
    #Database
    setup_database()
    
    # Main Window
    win = Tk() #make a window
    
    win.geometry("1280x720+130+50") #the size of window and where it will start
    win.resizable(False,False) #privent the user from resize the window
    win.title("Flight Reservation")
    
    # Icon
    win.iconbitmap(resource_path("plane.ico"))

    # first page is the home page
    HomePage(win)

    win.mainloop()

# Start the application    
if __name__ == "__main__":
    main()