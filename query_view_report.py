from table_print_to_terminal import *

def query_view_report(conn, column, value):
    the_description = "View report of: "
    the_query = f"""SELECT * FROM films WHERE {column}={value};"""
    table_print_to_terminal(conn, the_description, the_query)