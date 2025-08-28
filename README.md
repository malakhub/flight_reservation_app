# ✈️ OBE Sky Reservations – Flight Booking System

A **simple yet complete** desktop application for booking, viewing, editing, and deleting flight reservations.  
Built with **Python**, **Tkinter** for the GUI, and **SQLite** for the database.  

This project is structured into **multiple pages** for better organization, and supports **packaging into a Windows `.exe`** using PyInstaller.

---

## 📑 Table of Contents
- [📌 Features](#-features)
- [🛠️ Technologies Used](#️-technologies-used)
- [🗄️ Database Schema](#️-database-schema)
- [🚀 Installation](#-installation)
- [🖥️ Running the Application](#️-running-the-application)
- [📅 Booking a Flight](#-booking-a-flight)
- [📜 Viewing Reservations](#-viewing-reservations)
- [✏️ Editing a Reservation](#️-editing-a-reservation)
- [🗑️ Deleting a Reservation](#️-deleting-a-reservation)
- [📦 Creating a .exe for Windows](#-creating-a-exe-for-windows)
- [📝 Author](#-author)

---

## 📌 Features
- **Book Flights** – enter passenger details, flight number, departure/destination, date, and seat number.  
- **View Reservations** – see all bookings in a table.  
- **Edit Reservations** – modify existing reservations.  
- **Delete Reservations** – remove bookings from the database.  
- **Persistent Storage** – all data stored in an SQLite database (`flights.db`).  
- **Executable Build** – package into a standalone `.exe` for Windows.  
- **Modular Design** – each page is in its own file for maintainability.  

---

## 🛠️ Technologies Used

| Component          | Technology     |
|--------------------|----------------|
| **Language**       | Python ≥ 3.10  |
| **GUI Framework**  | Tkinter        |
| **Database**       | SQLite3        |
| **Packaging Tool** | PyInstaller    |

---

## 🗄️ Database Schema

**Table:** `reservations`

| Column          | Type      | Description                          |
|-----------------|-----------|--------------------------------------|
| `id`            | INTEGER PRIMARY KEY AUTOINCREMENT | Unique reservation ID |
| `name`          | TEXT      | Passenger's full name                |
| `flight_number` | TEXT      | Flight number (e.g., FS123)          |
| `departure`     | TEXT      | Departure city                       |
| `destination`   | TEXT      | Destination city                     |
| `date`          | TEXT      | Flight date (DD/MM/YYYY)             |
| `seat_number`   | TEXT      | Seat number (e.g., 12A)              |

---

## 🚀 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/malakhub/flight_reservation_app.git
cd flight_reservation_app
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🖥️ Running the Application

```bash
python main.py
```

---

## 📅 Booking a Flight

1. Click **Book a Flight** from the home page.
2. Fill in all fields:

   * Full Name
   * Flight Number
   * Departure
   * Destination
   * Date
   * Seat Number
3. Click **Submit** to save the booking to the database.

---

## 📜 Viewing Reservations

1. Click **View Reservations**.
2. All reservations will be shown in a table.
3. Use **Edit** or **Delete** to modify or remove bookings.

---

## ✏️ Editing a Reservation

1. From the **View Reservations** page, select a booking.
2. Click **Edit**.
3. Modify any fields.
4. Click **Update** to save changes.

---

## 🗑️ Deleting a Reservation

1. From the **View Reservations** page, select a booking.
2. Click **Delete**.
3. The booking will be permanently removed from the database.

---

## 📦 Creating a .exe for Windows

### Install PyInstaller

```bash
pip install pyinstaller
```

### Build the executable

```bash
pyinstaller --onefile --windowed main.py
```

### Locate the executable

* Found in the **dist/** folder as `main.exe`.

---

## 📝 Author

👩‍💻 Developed by **Malak Medhat**
🎓 Graduation Project – SprintUP Python Programming