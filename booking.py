# Flight booking form
from tkinter import *
from tkinter import messagebox, Canvas
from database import add_reservation
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class BookingPage:
    def __init__(self, master):
        self.master = master

        # Clear the past Window
        self.clear_window()

        # Path of Images
        if getattr(sys, 'frozen', False):
            # Running as .exe
            BASE_DIR = sys._MEIPASS
            IMG_DIR = os.path.join(BASE_DIR, "images")
        else:
            # Running as script
            BASE_DIR = os.path.dirname(__file__)
            IMG_DIR = os.path.join(BASE_DIR, "images")

        # Create Canvas
        canvas = Canvas(self.master,bg = "#FFFFFF",height = 720,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
        canvas.place(x=0, y=0)  
        
        # Background
        self.img = PhotoImage(file=resource_path("images/1.png"))
        canvas.create_image(640.0, 360.0, image=self.img)

        # Create input fields labels and keys
        fields = [
            ("Full Name", "name", 84, 189, 110.5, 220.0, 400.0,51.0 ),
            ("Flight Number", "flight_number", 86, 296, 110.5, 324.0, 400.0,51.0 ),
            ("Departure", "departure", 86, 398, 109.0, 431.0, 168.0, 48.0),
            ("Destination", "destination", 323, 398, 344.0, 431.0, 168.0, 48.0),
            ("Date", "date", 86, 501, 109.0, 534.0, 168.0, 48.0),
            ("Seat Number", "seat_number", 323, 501, 344.0, 534.0, 168.0, 48.0)
        ]
        
        # Dictionary to store input fields
        self.entries = {} 

        for label_text, key, lx, ly, ex, ey, ew, eh, in fields:
            
            # Text
            canvas.create_text(lx, ly,anchor="nw",text=label_text,fill="#303D7A",font=("Poppins Regular", -16))

            placeholders = {
                "name": "Enter your full name",
                "flight_number": "e.g. FS123",
                "departure": "e.g. New York",
                "destination": "e.g. London",
                "date": "dd/mm/yyyy",
                "seat_number": "e.g. 12A"
            }
            ph = placeholders.get(key, "")
            
            # Entries
            entry = Entry(font=("Arial", 14),bd=0,bg="#9ACFFF",fg="gray",highlightthickness=0)
            entry.place(x=ex, y=ey, width=ew, height=eh)
            entry.insert(0, ph)
    
            def clear_placeholder(e, ent=entry, ph=ph):
                if ent.get() == ph and ent.cget("fg") == "gray":
                    ent.delete(0, "end")
                    ent.config(fg="#030052")

            def add_placeholder(e, ent=entry, ph=ph):
                if ent.get().strip() == "":
                    ent.insert(0, ph)
                    ent.config(fg="gray")

            entry.bind("<FocusIn>", clear_placeholder)
            entry.bind("<FocusOut>", add_placeholder)

            self.entries[key] = entry
        
        # Submit button
        self.button_image_0 = PhotoImage(file=resource_path("images/7.png"))
        self.button_image_1 = PhotoImage(file=resource_path("images/8.png"))
        submitbt = Button(image=self.button_image_0,borderwidth=0,highlightthickness=0,command= self.submit,relief="flat")
        submitbt.bind("<Enter>", lambda e: self.bt_enter(e, self.button_image_1))
        submitbt.bind("<Leave>", lambda e: self.bt_leave(e, self.button_image_0))
        submitbt.place(x=84.0,y=600.0,width=127.0,height=38.0)

        # Cancel Button
        self.button_image_2 = PhotoImage(file=resource_path("images/9.png"))
        self.button_image_3 = PhotoImage(file=resource_path("images/10.png"))
        cancelbt = Button(image=self.button_image_2,borderwidth=0,highlightthickness=0,command= self.go_home,relief="flat")
        cancelbt.bind("<Enter>", lambda e: self.bt_enter(e, self.button_image_3))
        cancelbt.bind("<Leave>", lambda e: self.bt_leave(e, self.button_image_2))
        cancelbt.place(x=319.0,y=600.0,width=127.0,height=38.0)

    def submit(self):
        data = {key: entry.get() for key, entry in self.entries.items()}

        # Validation: ensure all fields are filled
        if any(not val.strip() for val in data.values()):
            messagebox.showwarning("Missing Data", "Please fill all fields.")
            return

        # Save to database
        try:
            add_reservation(**data)
            messagebox.showinfo("Success", "Reservation added successfully!")

            # Clear fields
            for entry in self.entries.values():
                entry.delete(0, END)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add reservation.\n{e}")

    def go_home(self):
        # Import here to avoid circular import
        from home import HomePage
        HomePage(self.master)

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def bt_enter(self, event, img_hover):
        #edit something i already did
        event.widget.config(image=img_hover)

    def bt_leave(self, event, img_normal):
        event.widget.config(image=img_normal)        