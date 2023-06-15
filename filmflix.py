# NB: Can use SQLite Viewer extension in vscode to view the DB.
import sqlite3
import pandas as pd
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def connect_to_database():
    conn = sqlite3.connect("filmflix.db")
    cursor = conn.cursor()
    try:
        # Attempting to connect to a non-existing DB will create it.
        conn = sqlite3.connect("filmflix.db")
    except BaseException as be:
        print(f"DB connection error: {be}")
    return conn

def disconnect_from_database(conn):
    """Disconnect from the filmflix database."""
    try:
        conn.close()
    except BaseException as be:
        print(f"DB disconnection error: {be}")

def table_adapt(conn, query, description):
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    table_print_report(conn, query, description, "just-select-all")

def table_print_report(conn, query, description, query_to_read_db="use-query-argument"):
    """Performs a SQL query then writes the resultant view to the terminal.
       Uses pandas to better format the tables."""

    print(f"\n{bcolors.OKGREEN}{description}{bcolors.ENDC} via {bcolors.WARNING}{query}{bcolors.ENDC}\n")

    if query_to_read_db == "use-query-argument": 
        dql_query = pd.read_sql(query, conn)
    elif query_to_read_db == "just-select-all":
        dql_query = pd.read_sql("""SELECT * FROM films""", conn)
    else: 
        print("error: 'query_to_use' unknown")
    df = pd.DataFrame(dql_query)

    # Retro style: DataFrame to retro style markdown, row index count removed. 
    print(df.to_markdown(index=0)) 

    input(f"\n{bcolors.FAIL}Press Enter to continue...{bcolors.ENDC}\n")

if __name__ == "__main__":
    """Main function."""

    # Create a SQLite DB called "filmflix.db", create a table in this DB called
    # "films", populate the films table with film data.
    #conn = create_filmflixDB_then_add_films_table_then_add_data_to_films_table()

    conn = connect_to_database()

    cursor = conn.cursor()
    # cursor.execute("""ALTER TABLE tblFilms RENAME COLUMN yearReleased TO year;""")
    cursor.execute("""ALTER TABLE tblFilms RENAME TO films;""")
    conn.commit()
    cursor.close()

    # Tasks: 
    # 1. Perform CRUD operations (Create (INSERT), Read (SELECT), Update (UPDATE), Delete (DELETE)). 
    # 2. Print a selection of reports.

    #########################
    # CRUD operations.
    #########################

    # Code methodology.
    # adapt_table_sql_query():
    #   is for Create/INSERT, Update/UPDATE and Delete/DELETE queries, SQL table altered, report file unchanged.
    # generate_report_sql_query():
    #   is for read/SELECT queries, SQL table unaltered, view added to report file.
    
    # Report the state of the films table immediately after creation.
    # table_print_report(conn, """SELECT * FROM films;""", "The original films table obtained")

    # # Add a film to the films table. 
    # the_query = """INSERT INTO tblFilms(id, title, year, rating, duration, genre)
    #                 VALUES(101,'Poopy Pants', 2020, 'PG', 129, 'Comedy');"""
    # table_adapt(conn, the_query, "Added film 'Poopy Pants'")

    # # Delete the film just added. 
    # the_query = """DELETE FROM films WHERE id=101;"""
    # table_adapt(conn, the_query, "Deleted film 'Poopy Pants'")

    # # Update / change the genre of "The Nice Guys".
    # the_query = """UPDATE films SET genre='Comedy' WHERE title='The Nice Guys';"""
    # table_adapt(conn, the_query, "Genre of 'The Nice Guys' changed to 'Comedy'")

    # #########################
    # # Report generation.
    # #########################

    # # Report films that are in the "Comedy" genre.
    # the_query = """SELECT * FROM films WHERE genre='Animation';"""
    # table_print_report(conn, the_query, "All films in the genre 'Animation' selected")
    
    # # Report which films were released in 2015.
    # the_query = """SELECT * FROM films WHERE year=2015;"""
    # table_print_report(conn, the_query, "All films released in 2015 selected")

    # # Report all films that have a "PG" rating.
    # the_query = """SELECT * FROM films WHERE rating='PG';"""
    # table_print_report(conn, the_query, "All films rated 'PG' selected")

    # Close the DB connection.
    disconnect_from_database(conn)