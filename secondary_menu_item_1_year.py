from user_input import *
from table_print_to_terminal import *

def secondary_menu_item_1_year(conn):
    year = get_year()
    print("")

    the_query = f"""SELECT * FROM films WHERE year={year};"""
    table_print_to_terminal(conn, the_query)