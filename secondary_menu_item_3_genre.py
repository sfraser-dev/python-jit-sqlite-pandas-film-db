from user_input import *
from table_print_to_terminal import *

def secondary_menu_item_3_genre(conn):
    genre = get_genre()
    print("")

    the_query = f"""SELECT * FROM films WHERE genre='{genre}';"""
    table_print_to_terminal(conn, the_query)