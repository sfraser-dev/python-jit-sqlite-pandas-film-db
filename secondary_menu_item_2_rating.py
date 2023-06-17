from user_input import *
from table_print_to_terminal import *

def secondary_menu_item_2_rating(conn):
    rating = get_rating()
    print("")

    the_query = f"""SELECT * FROM films WHERE rating='{rating}';"""
    table_print_to_terminal(conn, the_query)