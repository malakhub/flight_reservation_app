# Home page UI
import os
import sys
from tkinter import *
from booking import BookingPage
from reservations import ReservationPage

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class HomePage():
    def __init__(self, win):
        self.master = win
        
        # Clear the past Window
        self.clear_window()
        
        # Path of Images
        IMG_DIR = resource_path("images")
        
        # Background
        self.img = PhotoImage(file=resource_path("images/0.png"))
        bg = Label(self.master, image=self.img)
        bg.place(x=0,y=0)

        # Book a Flight Button
        self.img_book1 = PhotoImage(file=resource_path("images/3.png"))
        self.img_book2 = PhotoImage(file=resource_path("images/4.png"))
        bt = Button(self.master, image=self.img_book1, relief='flat', bd=0, command=self.booking)
        bt.bind("<Enter>", lambda e: self.bt_enter(e, self.img_book2))
        bt.bind("<Leave>", lambda e: self.bt_leave(e, self.img_book1))
        bt.place(x=55,y=490)

        # View Reservation Button
        self.img_res1 = PhotoImage(file=resource_path("images/5.png"))
        self.img_res2 = PhotoImage(file=resource_path("images/6.png"))
        bt2 = Button(self.master, image=self.img_res1, relief='flat', bd=0, command=self.reservation)
        bt2.bind("<Enter>", lambda e: self.bt_enter(e, self.img_res2))
        bt2.bind("<Leave>", lambda e: self.bt_leave(e, self.img_res1))
        bt2.place(x=300,y=490)

    def bt_enter(self, event, img_hover):
        #edit something i already did
        event.widget.config(image=img_hover)

    def bt_leave(self, event, img_normal):
        event.widget.config(image=img_normal)        

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def booking(self):
        BookingPage(self.master)

    def reservation(self):
        ReservationPage(self.master)