from table_print_to_terminal import *

def query_view_specific_report(conn, column, value):
    """User select specific view of table."""
    the_description = "View report of: "
    the_query = f"""SELECT * FROM films WHERE {column}={value};"""
    table_print_to_terminal(conn, the_description, the_query)