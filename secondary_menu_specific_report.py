from secondary_menu_items import *
from colors import *

def secondary_menu_specific_report(conn):
    """Top level menu for viewing a specific report."""
    choice_action = """1. View all records from a selected field
2. View all films from a selected year
3. View all films with a selected rating
4. View all films from a selected genre
5. Exit this sub-menu\n""" 
    
    while True:
        try:
            choice_action = int(input(choice_action))
            match choice_action:
                case 1:
                    secondary_menu_item_1()
                    continue 
                case 2:
                    secondary_menu_item_2()
                    continue
                case 3:
                    secondary_menu_item_3()
                    continue
                case 4:
                    secondary_menu_item_4()
                    continue
                case 5:
                    print("Exiting")
                    break
                case _:
                    print(f"{bcolors.FAIL}input error, please try again{bcolors.ENDC}")
                    continue
        except ValueError:
                print(f"{choice_action} is not a valid value.")
                continue