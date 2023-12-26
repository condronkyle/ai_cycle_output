import sqlite3

# Establish a connection to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('friends.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create the friends table if it doesn't exist
def init_db():
    with get_db_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS friends (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone_number TEXT UNIQUE,
            address TEXT,
            birthdate TEXT
        );
        """)

# CRUD operations
def add_friend(name, email, phone_number, address, birthdate):
    with get_db_connection() as conn:
        conn.execute("""
        INSERT INTO friends (name, email, phone_number, address, birthdate)
        VALUES (?, ?, ?, ?, ?);
        """, (name, email, phone_number, address, birthdate))

def list_friends():
    with get_db_connection() as conn:
        friends = conn.execute("SELECT * FROM friends;").fetchall()
        for friend in friends:
            print({key: friend[key] for key in friend.keys()})

def update_friend(id, name, email, phone_number, address, birthdate):
    with get_db_connection() as conn:
        conn.execute("""
        UPDATE friends
        SET name = ?, email = ?, phone_number = ?, address = ?, birthdate = ?
        WHERE id = ?;
        """, (name, email, phone_number, address, birthdate, id))

def delete_friend(id):
    with get_db_connection() as conn:
        conn.execute("DELETE FROM friends WHERE id = ?;", (id,))

# TODO: Add CLI parsing to handle user input and call these functions accordingly

# Initialize the database
init_db()