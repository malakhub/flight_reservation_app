# Main application file
from tkinter import *
import os 

#import modules from my own files
from home import HomePage
from database import setup_database

def main():
    
    #Database
    setup_database()
    
    # Main Window
    win = Tk() #make a window
    
    win.geometry("1280x720+130+50") #the size of window and where it will start
    win.resizable(False,False) #privent the user from resize the window
    win.title("Flight Reservation")
    
    # Icon
    BASE_DIR = os.path.dirname(__file__)
    ICON_PATH = os.path.join(BASE_DIR, "plane.ico")
    win.iconbitmap(ICON_PATH)

    # first page is the home page
    HomePage(win)

    win.mainloop()

# Start the application    
if __name__ == "__main__":
    main()