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

def create_filmflixDB_then_add_films_table_then_add_data_to_films_table():
    """Connects to the filmflix database."""
    # If DB already exists, delete it.
    db_name = "filmflix.db"
    try:
        if os.path.exists("db_name"):
            os.remove(db_name)
    except OSError as e:
        print("Warning: %s - %s." % (e.filename, e.strerror))
    try:
        # Attempting to connect to a non-existing DB will create it.
        conn = sqlite3.connect("filmflix.db")
    except BaseException as be:
        print(f"DB connection error: {be}")
    
    cursor = conn.execute("""DROP TABLE IF EXISTS films""")
    conn.commit()
    cursor = conn.execute   ("""CREATE TABLE films 
                                (   
                                    [id] INTEGER PRIMARY KEY, 
                                    [title] TEXT, 
                                    [year] INTEGER, 
                                    [rating] TEXT, 
                                    [duration] INTEGER,
                                    [genre] TEXT
                                )
                            """)
    cursor.execute("""
                        INSERT INTO
                        films(id, title, year, rating, duration, genre)
                        VALUES
                        (1, "The Muppets", 2022, "PG", 116, "Comedy"),
                        (2, "The Legend of Tarzan", 2016, "PG", 109, "Animation"),
                        (3, "Jason Bourne", 2015, "G", 123, "Action"),
                        (4, "The Nice Guys", 2016, "R", 116, "Action"),
                        (5, "The Secret Life of Pets", 2016, "G", 91, "Comedy"), 
                        (6, "Star Trek Beyond", 2015, "PG", 120, "Action"),
                        (7, "Batman v Superman", 2016, "PG", 151, "Action"),
                        (8, "Finding Dory", 2016, "G", 103, "Comedy"),
                        (9, "Zootopia", 2016, "G", 108,  "Animation"),
                        (10, "The BFG", 2016, "PG", 90, "Animation")
                    """)
    # Commit the changes.   
    conn.commit()
 
    cursor.close()
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
    table_print_all(conn, query, description)

def table_print_all(conn, query, description):
    """Performs a SQL query then writes the resultant view to the terminal.
       Uses pandas to better format the tables."""

    print(f"\n{bcolors.OKGREEN}{description}{bcolors.ENDC} via {bcolors.WARNING}{query}{bcolors.ENDC}\n")


    dql_query = pd.read_sql("SELECT * FROM films", conn)
    df = pd.DataFrame(dql_query)

    # Retro style: DataFrame to retro style markdown, row index count removed. 
    print(df.to_markdown(index=0)) 

    input(f"\n{bcolors.FAIL}Press Enter to continue...{bcolors.ENDC}\n")

def table_print_report(conn, query, description):
    """Performs a SQL query then writes the resultant view to the terminal.
       Uses pandas to better format the tables."""

    print(f"\n{bcolors.OKGREEN}{description}{bcolors.ENDC} via {bcolors.WARNING}{query}{bcolors.ENDC}\n")

    dql_query = pd.read_sql(the_query, conn)
    df = pd.DataFrame(dql_query)

    # Retro style: DataFrame to retro style markdown, row index count removed. 
    print(df.to_markdown(index=0)) 

    input(f"\n{bcolors.FAIL}Press Enter to continue...{bcolors.ENDC}\n")

if __name__ == "__main__":
    """Main function."""

    # Create a SQLite DB called "filmflix.db", create a table in this DB called
    # "films", populate the films table with film data.
    conn = create_filmflixDB_then_add_films_table_then_add_data_to_films_table()

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
    table_print_all(conn, """SELECT * FROM films;""", "The original films table obtained")

    # Add a film to the films table. 
    the_query = """INSERT INTO films(id, title, year, rating, duration, genre)
                                        VALUES(11,'Poopy Pants', 2020, 'PG', 129, 'Comedy');"""
    table_adapt(conn, the_query, "Added film 'Poopy Pants'")

    # Delete the film just added. 
    the_query = """DELETE FROM films WHERE id=11;"""
    table_adapt(conn, the_query, "Deleted film 'Poopy Pants'")

    # Update / change the genre of "The Nice Guys".
    the_query = """UPDATE films SET genre='Comedy' WHERE title='The Nice Guys';"""
    table_adapt(conn, the_query, "Genre of 'The Nice Guys' changed to 'Comedy'")

    #########################
    # Report generation.
    #########################

    # Report films that are in the "Comedy" genre.
    the_query = """SELECT * FROM films WHERE genre='Comedy';"""
    table_print_report(conn, the_query, "All films in the genre 'Comedy' selected")
    
    # Report which films were released in 2015.
    the_query = """SELECT * FROM films WHERE year=2015;"""
    table_print_report(conn, the_query, "All films released in 2015 selected")

    # Report all films that have a "PG" rating.
    the_query = """SELECT * FROM films WHERE rating='PG';"""
    table_print_report(conn, the_query, "All films rated 'PG' selected")

    # Close the DB connection.
    disconnect_from_database(conn)