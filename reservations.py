# View all reservations
import tkinter as tk
from tkinter import messagebox
from database import get_all_reservations, delete_reservation

class ReservationPage:
    def __init__(self, master):
        from home import HomePage
        from edit_reservation import EditReservationPage  

        self.master = master
        self.clear_window()

        title = tk.Label(master, text="All Reservations", font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        # Table
        table_frame = tk.Frame(master)
        table_frame.pack(pady=10)

        # Headers
        headers = ["ID", "Name", "Flight Number", "Departure", "Destination", "Date", "Seat", "Edit", "Delete"]

        for idx, h in enumerate(headers):
            tk.Label(table_frame, text=h, font=("Arial", 10, "bold"), 
                     bg="#e0e0e0", padx=10, pady=5).grid(row=0, column=idx, sticky="nsew")

        # Data rows
        self.reservations = get_all_reservations()

        for i, row in enumerate(self.reservations, start=1):
            bg_color = "#ffffff" if i % 2 == 0 else "#f9f9f9"  # alternate colors

            for j, val in enumerate(row):
                tk.Label(table_frame, text=val, bg=bg_color, padx=10, pady=5).grid(
                    row=i, column=j, sticky="nsew"
                )

            # Edit button
            edit_btn = tk.Button(table_frame, text="Edit", 
                                 command=lambda rid=row[0]: EditReservationPage(master, rid))
            edit_btn.grid(row=i, column=len(headers)-2, sticky="nsew", padx=2, pady=2)

            # Delete button
            delete_btn = tk.Button(table_frame, text="Delete",
                                   command=lambda rid=row[0]: self.confirm_delete(rid))
            delete_btn.grid(row=i, column=len(headers)-1, sticky="nsew", padx=2, pady=2)

        # Make all columns expand equally
        for col in range(len(headers)):
            table_frame.grid_columnconfigure(col, weight=1)

        # Back button
        back_btn = tk.Button(master, text="Back to Home", command=lambda: HomePage(master))
        back_btn.pack(pady=15)

    def confirm_delete(self, reservation_id):
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this reservation?"):
            delete_reservation(reservation_id)
            messagebox.showinfo("Deleted", "Reservation deleted.")
            ReservationPage(self.master)  # refresh page

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()
