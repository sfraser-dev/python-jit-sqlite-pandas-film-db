from table_print_to_terminal import *

def query_view_all_records(conn):
    the_description = "The films table obtained via: "
    the_query = """SELECT * FROM films;"""
    table_print_to_terminal(conn,the_description, the_query)