import sqlite3

def connect_db(): 
    conn = sqlite3.connect('expense_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    return conn

def add_transaction(conn, transaction):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions (date, category, amount, description)
        VALUES (?, ?, ?, ?)
    ''', (transaction.date, transaction.category, transaction.amount, transaction.description))
    conn.commit()