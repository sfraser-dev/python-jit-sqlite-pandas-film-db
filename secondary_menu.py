from secondary_menu_items import *
from colors import *

def secondary_menu(conn):
    """Top level menu for viewing a specific report."""
    question = f"""{bcolors.OKBLUE}
1. View all films from selected year
2. View all films with selected rating
3. View all films from selected genre
4. Exit this sub-menu\n{bcolors.ENDC}""" 
    
    while True:
        try:
            user_choice = int(input(question))
            match user_choice:
                case 1:
                    secondary_menu_item_1_year(conn)
                    continue 
                case 2:
                    secondary_menu_item_2_rating(conn)
                    continue
                case 3:
                    secondary_menu_item_3_genre(conn)
                    continue
                case 4:
                    print("Exiting")
                    break
                case _:
                    print(f"{bcolors.FAIL}input range error, please input 1, 2, 3 or 4{bcolors.ENDC}")
                    continue
        except ValueError:
                print(f"{bcolors.FAIL}input type error, please input 1, 2, 3 or 4{bcolors.ENDC}")
                continue
    
    