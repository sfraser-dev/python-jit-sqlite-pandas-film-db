from table_adapt import *

def query_delete_record(conn, id):
    the_description = "Deleted film 'Test Film' via: "
    the_query = f"""DELETE FROM films WHERE id={id};"""
    table_adapt(conn, the_description, the_query)