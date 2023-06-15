from table_adapt import *

def query_update_record(conn):
    the_description = "Rating of 'Matrix Resurections' changed to 'PG' via: "
    the_query = """UPDATE films SET genre='Action' WHERE id=2;"""
    table_adapt(conn, the_description, the_query)