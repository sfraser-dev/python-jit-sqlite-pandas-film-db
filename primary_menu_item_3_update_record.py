from table_adapt import *
from user_input import *

def primary_menu_item_3_update_record(conn):
    """Update a record/row in the database."""

    # enter id of film to update
    id = get_id()
    # what to update, title, year, rating, duration or genre?

    the_description = "Rating of 'Matrix Resurections' changed to 'PG' via: "
    the_query = """UPDATE films SET title='Shaolin Vs Lama' WHERE id=34;"""
    table_adapt(conn, the_description, the_query)