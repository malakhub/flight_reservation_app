# Update/Delete functionality
# edit_reservation.py
import tkinter as tk
from tkinter import messagebox
from database import get_reservation_by_id, update_reservation

class EditReservationPage:
    def __init__(self, master, reservation_id):
        from home import HomePage
        from reservations import ReservationPage

        self.master = master
        self.reservation_id = reservation_id
        self.clear_window()

        data = get_reservation_by_id(reservation_id)
        if not data:
            messagebox.showerror("Error", "Reservation not found.")
            ReservationPage(master)
            return

        title = tk.Label(master, text="Edit Reservation", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        self.entries = {}
        fields = [
            ("Name", "name", data[1]),
            ("Flight Number", "flight_number", data[2]),
            ("Departure", "departure", data[3]),
            ("Destination", "destination", data[4]),
            ("Date (YYYY-MM-DD)", "date", data[5]),
            ("Seat Number", "seat_number", data[6])
        ]

        for label_text, key, value in fields:
            label = tk.Label(master, text=label_text)
            label.pack()
            entry = tk.Entry(master)
            entry.insert(0, value)
            entry.pack(pady=2)
            self.entries[key] = entry

        # Update Button
        update_btn = tk.Button(master, text="Update Reservation", command=self.update)
        update_btn.pack(pady=10)

        # Back
        back_btn = tk.Button(master, text="Back to Reservations", command=lambda: ReservationPage(master))
        back_btn.pack(pady=5)

    def update(self):
        from reservations import ReservationPage

        updated_data = {key: entry.get() for key, entry in self.entries.items()}

        if any(not val.strip() for val in updated_data.values()):
            messagebox.showwarning("Missing Data", "Please fill all fields.")
            return

        try:
            update_reservation(
                self.reservation_id,
                updated_data["name"],
                updated_data["flight_number"],
                updated_data["departure"],
                updated_data["destination"],
                updated_data["date"],
                updated_data["seat_number"]
            )
            messagebox.showinfo("Success", "Reservation updated successfully!")
            ReservationPage(self.master)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update reservation.\n{e}")

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()