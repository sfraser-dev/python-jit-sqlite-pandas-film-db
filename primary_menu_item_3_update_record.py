from table_adapt import *
from user_input import *

def primary_menu_item_3_update_record(conn):
    """Update a record/row in the database."""

    # Get id of film to update.
    question = "\nEnter id of film to be updated: "
    id = get_input_int(question)

    # Get what to update, title, year, rating, duration or genre?
    question = """\nSelect field to be updated:
1. Title
2. Year
3. Rating
4. Duration
5. Genre
"""
    field_to_update = get_field_to_update(question)
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

    the_description = f"Upating film with id={id}, changing '{field_to_update}' field to '{update_value}' via: "
    # Setting an integer field with an int wrapped in 'single quotes' is fine. 
    # Setting a text field with a value not wrapped in 'single quotes" is not fine.
    # Thus wrapping all in 'single quotes'.
    the_query = f"""UPDATE films SET {field_to_update}='{update_value}' WHERE id={id};"""
    table_adapt(conn, the_description, the_query)