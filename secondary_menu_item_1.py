from user_input import *
from table_print_to_terminal import *

def secondary_menu_item_1(conn):
    selected_field = get_field()

    the_description = f"View of {selected_field} field via: "
    the_query = f"""SELECT {selected_field} FROM films;"""
    table_print_to_terminal(conn, the_description, the_query)