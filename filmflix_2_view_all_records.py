from table_print_to_terminal import *

def filmflix_2_view_all_records(conn):
    """View the enire table via query 'SELECT * FROM films'."""
    the_description = "The films table obtained via: "
    the_query = """SELECT * FROM films;"""
    table_print_to_terminal(conn,the_description, the_query)