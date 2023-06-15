from table_adapt import *

def query_update_record(conn):
    the_description = "Rating of 'Matrix Resurections' changed to 'PG' via: "
    the_query = """UPDATE films SET rating='PG' WHERE title='Matrix Resurections';"""
    table_adapt(conn, the_description, the_query)