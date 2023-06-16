from table_adapt import *
from user_input import *

def query_delete_record(conn):
    """Delete a record/row from the database."""
    
    id = get_id()

    the_description = f"Deleted film with id={id} via: "
    the_query = f"""DELETE FROM films WHERE id={id};"""
    table_adapt(conn, the_description, the_query)