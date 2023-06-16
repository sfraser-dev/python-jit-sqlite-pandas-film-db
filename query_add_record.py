from table_adapt import *
from user_input import *

def query_add_record(conn):
    """Add a record/row to the database"""
    
    title = get_title()
    year = get_year()
    rating = get_rating()
    duration = get_duration()
    genre = get_genre()

    the_description = f"Added film {title} via "
    # SQLite integer and primary key combo will auto increment, no need for the id.
    the_query = f"""INSERT INTO films(title, year, rating, duration, genre)
                    VALUES('{title}', {year}, '{rating}', {duration}, '{genre}');"""

    table_adapt(conn, the_description, the_query)

