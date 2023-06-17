from secondary_menu_items import *
from colors import *

def secondary_menu_specific_report(conn):
    """Top level menu for viewing a specific report."""
    question = """\n1. View all records from a selected field
2. View all films from a selected year
3. View all films with a selected rating
4. View all films from a selected genre
5. Exit this sub-menu\n""" 
    
    while True:
        try:
            user_choice = int(input(question))
            match user_choice:
                case 1:
                    secondary_menu_item_1(conn)
                    continue 
                case 2:
                    secondary_menu_item_2(conn)
                    continue
                case 3:
                    secondary_menu_item_3(conn)
                    continue
                case 4:
                    secondary_menu_item_4(conn)
                    continue
                case 5:
                    print("Exiting")
                    break
                case _:
                    print(f"{bcolors.FAIL}input error, please try again{bcolors.ENDC}")
                    continue
        except ValueError:
                print(f"{bcolors.FAIL}error: secondary_menu_specific_report(){bcolors.ENDC}")
                continue
    
    