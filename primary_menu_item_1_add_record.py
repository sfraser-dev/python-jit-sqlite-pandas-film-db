from table_adapt import *
from user_input import *

def primary_menu_item_1_add_record(conn):
    """Add a record/row to the database"""

    print(f"{bcolors.WARNING}Adding new film to database{bcolors.ENDC}")
    title = get_title()
    year = get_year()
    rating = get_rating()
    duration = get_duration()
    genre = get_genre()

    # SQLite integer and primary key combo will auto increment, no need for the id.
    the_query = f"""INSERT INTO films(title, year, rating, duration, genre)
                    VALUES('{title}', {year}, '{rating}', {duration}, '{genre}');"""

    table_adapt(conn, the_query)
    print(f"\n{bcolors.OKGREEN}Film '{title}' added{bcolors.ENDC}")

