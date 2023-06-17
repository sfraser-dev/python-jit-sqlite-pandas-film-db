from table_adapt import *
from user_input import *

def primary_menu_item_3_update_record(conn):
    """Update a record/row in the database."""

    # Get id of film to update.
    print(f"{bcolors.WARNING}Updating film via id{bcolors.ENDC}")
    id = get_id()

    # Get what to update, title, year, rating, duration or genre?
    field_to_update = get_field()

    # Get value to be updated to.
    match field_to_update:
        case "title":
            update_value = get_title()
        case "year":
            update_value = get_year()
        case "rating":
            update_value = get_rating()
        case "duration": 
            update_value = get_duration()
        case "genre":
            update_value = get_genre()
        case _:
            print(f"{bcolors.FAIL}case error: primary_menu_item_3_update_record(){bcolors.ENDC}")

    # Setting an integer field with an int wrapped in 'single quotes' is fine. 
    # Setting a text field with a value not wrapped in 'single quotes" is not fine.
    # Thus wrapping all in 'single quotes'.
    the_query = f"""UPDATE films SET {field_to_update}='{update_value}' WHERE id={id};"""
    table_adapt(conn, the_query)
    print(f"\n{bcolors.OKGREEN}Film with id {id} updated{bcolors.ENDC}")