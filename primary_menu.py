from primary_menu_items import *
from connect import *
from colors import *

def main():
    """Main function."""

    conn = connect_to_database()
    
    question = f"""{bcolors.OKCYAN}
1. Add Record
2. View All Records
3. Update Record
4. Delete Record
5. View Specific Report
6. Exit Program\n{bcolors.ENDC}"""

    # Top level menu loop.
    while True:
        try:
            user_choice = int(input(question))
            match user_choice:
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
                    secondary_menu(conn)
                    continue
                case 6:
                    print("Exiting program")
                    break
                case _:
                    print(f"{bcolors.FAIL}input range error, please select 1, 2, 3, 4, 5 or 6{bcolors.ENDC}")
                    continue
        except ValueError:
            print(f"{bcolors.FAIL}input type error, please 1, 2, 3, 4, 5 or 6{bcolors.ENDC}")
            continue

    # Close connection and disconnect from the database.
    conn.close()
    disconnect_from_database(conn)

if __name__ == "__main__":
    main()
