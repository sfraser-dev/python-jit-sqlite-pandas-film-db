from table_print_to_terminal import *

def table_adapt(conn, description, query):
    """Perform SQL query upon the table and commit the changes."""
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    table_print_to_terminal(conn, description, query, "just-select-all")
