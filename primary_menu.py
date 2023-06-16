from primary_menu_items import *
from connect import *
from colors import *

def main():
    """Main function."""

    conn = connect_to_database()

    # Top level menu loop.
    while True:
        choice_action = input("\n"+
                                "1. Add Record (Create)\n"+
                                "2. View All Records (Read)\n"+
                                "3. Update Record (Update)\n"+
                                "4. Delete Record (Delete)\n"+
                                "5. View Specific Report\n"+
                                "6. Exit\n"
                              )

        try:
            choice_action = int(choice_action)
            match choice_action:
                case 1:
                    primary_menu_item_1_add_record(conn)
                    continue
                case 2:
                    primary_menu_item_2_view_all_records(conn)
                    continue
                case 3: 
                    primary_menu_item_3_update_record(conn)
                    continue
                case 4: 
                    primary_menu_item_4_delete_record(conn)
                    continue
                case 5: 
                    secondary_menu_specific_report(conn)
                    continue
                case 6:
                    print("Exiting")
                    break
                case _:
                    print(f"{bcolors.FAIL}input error, please try again{bcolors.ENDC}")
                    continue
        except ValueError:
            print(f"{choice_action} is not a valid value.")
            continue

    # Close connection and disconnect from the database.
    conn.close()
    disconnect_from_database(conn)

if __name__ == "__main__":
    main()
