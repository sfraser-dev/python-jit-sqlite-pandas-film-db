from connect import *
from queries import *

# if __name__ == "__main__":
    
    # table_print_report(conn, """SELECT * FROM films;""", "The original films table obtained")
    # the_query = """INSERT INTO films(id, title, year, rating, duration, genre)
    #                 VALUES(101,'Test Film', 2020, 'PG', 129, 'Comedy');"""
    # table_adapt(conn, the_query, "Added film 'Test Film'")
    # the_query = """DELETE FROM films WHERE id=101;"""
    # table_adapt(conn, the_query, "Deleted film 'Test Film'")
    # the_query = """UPDATE films SET genre='Comedy' WHERE title='The Nice Guys';"""
    # table_adapt(conn, the_query, "Genre of 'The Nice Guys' changed to 'Comedy'")
    # the_query = """SELECT * FROM films WHERE genre='Animation';"""
    # table_print_report(conn, the_query, "All films in the genre 'Animation' selected")
    # the_query = """SELECT * FROM films WHERE year=2015;"""
    # table_print_report(conn, the_query, "All films released in 2015 selected")
    # the_query = """SELECT * FROM films WHERE rating='PG';"""
    # table_print_report(conn, the_query, "All films rated 'PG' selected")
    # disconnect_from_database(conn)

def main():
    """Main function."""

    conn = connect_to_database()

    while True:
        choice_action = input("\n"+
                                "1. Add Record (Create)\n"+
                                "2. View All Records (Read)\n"+
                                "3. Update Record (Update)\n"+
                                "4. Delete Record (Delete)\n"+
                                "5. View Report\n"+
                                "6. Exit\n\n"
                              )

        try:
            choice_action = int(choice_action)
        except ValueError:
            print(f"{choice_action} is not a valid value.")
            continue

        match choice_action:
            case 1:
                query_add_record(conn)
            case 2:
                query_view_all_records(conn)
            case 3: 
                query_update_record(conn)
            case 4: 
                query_delete_record(conn, 37)
            case 5: 
                query_view_report(conn, "year", 2015)
            case 6:
                print("Exiting")
                break
            case _:
                print("error: cannot match case: main()") 
                exit()
    conn.close()
    disconnect_from_database(conn)

if __name__ == "__main__":
    main()
