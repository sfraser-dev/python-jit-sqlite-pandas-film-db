from table_print_to_terminal import *

def table_adapt(conn, description, query):
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    table_print_to_terminal(conn, description, query, "just-select-all")
