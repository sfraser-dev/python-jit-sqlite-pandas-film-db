from table_print_to_terminal import *

def primary_menu_item_2_view_all_records(conn):
    """View the enire table via query 'SELECT * FROM films'."""
    the_query = """SELECT * FROM films;"""
    table_print_to_terminal(conn, the_query)