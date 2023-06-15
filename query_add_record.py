from table_adapt import *

def query_add_record(conn):
    the_description = "Added film 'Test Film' via "
    # sqlite integer and primary key will auto increment, no need to give the id.
    the_query = """INSERT INTO films(title, year, rating, duration, genre)
                    VALUES('Test Film', 2020, 'PG', 129, 'Comedy');"""
    table_adapt(conn, the_description, the_query)

