from table_adapt import *

def query_add_record(conn):
    the_description = "Added film 'Test Film' via "
    # sqlite integer and primary key combo will auto increment, no need to give the id.
    the_query = """INSERT INTO films(title, year, rating, duration, genre)
                    VALUES('Test Film', 2020, 'PG', 129, 'Comedy');"""
    table_adapt(conn, the_description, the_query)

def ask():
    film_title = get_text("Enter film title: ")
    film_year = get_int("Enter year film was released: ")
    film_rating = get_rating("Enter the film rating:\n\n"+
                             "1. PG (Parental Guidance)\n"+
                             "2. G (General Audience)\n"+
                             "3. R (Restricted)\n\n")
    film_duration = get_int(input("Enter the film duration (mins)."))
    film_genre = get_genre("Enter the genre of the film:\n\n"+ 
                             "1. Comedy\n"+
                             "2. Action"+
                             "3. Animation\n"+
                             "4. Fantasy\n"+
                             "5. Crime\n")

def get_text(question):
    while True:
        try:
            text = input(question)
            break
        except Exception as e:
            print(e)
            continue

def get_int(question):
    while True:
        try:
            val = int(input(question))
            break
        except ValueError:
            print("input unrecognised, please try again (integer expected)")
            continue

def get_rating(question):
    while True:
        choice_action = input(question)

        try:
            choice_action = int(choice_action)
        except ValueError:
            print(f"{choice_action} is not a valid value.")
            continue

        match choice_action:
            case 1:
                return "PG"
            case 2:
                return "G"
            case 3: 
                return "R"
            case _:
                print("error: cannot match case: get_rating()") 
                exit()

def get_genre(question):
    while True:
        choice_action = input(question)
        match choice_action:
            case 1:
                return "Comedy"
            case 2:
                return "Action"
            case 3: 
                return "Animation"
            case 4: 
                return "Fantasy"
            case 5: 
                return "Crime"
            case _:
                print("error: cannot match case: get_genre()") 
                exit()
