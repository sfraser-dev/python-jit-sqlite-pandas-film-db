from table_adapt import *
from user_input import *

def primary_menu_item_4_delete_record(conn):
    """Delete a record/row from the database."""
    
    print(f"{bcolors.WARNING}Deleting film from database{bcolors.ENDC}")
    id = get_id()

    the_query = f"""DELETE FROM films WHERE id={id};"""
    table_adapt(conn, the_query)
    print(f"\n{bcolors.FAIL}Film with id {id} deleted{bcolors.ENDC}")