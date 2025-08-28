#SQLite database connection and setup
import sqlite3

def setup_database():
    ## Create Database And Connect
    db = sqlite3.connect("flights.db")
    
    # Setting Up The Cursor
    cr = db.cursor()

    # Create The Tables and Fields with proper data types
    cr.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            flight_number TEXT NOT NULL,
            departure TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            seat_number TEXT NOT NULL
        )
    """)
    # Save (Commit) Changes
    db.commit()

    # Close Database
    db.close()

def add_reservation(name, flight_number, departure, destination, date, seat_number):
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, flight_number, departure, destination, date, seat_number))
    conn.commit()
    conn.close()

def get_all_reservations():
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    data = cursor.fetchall()
    conn.close()
    return data

def delete_reservation(reservation_id):
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reservations WHERE id = ?", (reservation_id,))
    conn.commit()
    conn.close()

def get_reservation_by_id(reservation_id):
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations WHERE id = ?", (reservation_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def update_reservation(reservation_id, name, flight_number, departure, destination, date, seat_number):
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE reservations
        SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
        WHERE id = ?
    """, (name, flight_number, departure, destination, date, seat_number, reservation_id))
    conn.commit()
    conn.close()