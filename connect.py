import sqlite3

def connect_to_database():
    """Connect to the filmflix database."""
    try:
        conn = sqlite3.connect("filmflix.db")
    except BaseException as be:
        print(f"DB connection error: {be}")
    return conn

def disconnect_from_database(conn):
    """Disconnect from the filmflix database."""
    try:
        conn.close()
    except BaseException as be:
        print(f"DB disconnection error: {be}")

