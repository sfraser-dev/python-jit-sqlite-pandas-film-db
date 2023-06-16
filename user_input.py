from colors import *

def get_id():
    question = "Enter id of film to be deleted: "
    return get_int(question)

def get_year():
    question = "Enter film release year: "
    return get_int(question)

def get_duration():
    question = "Enter film duration (mins): "
    return get_int(question)

def get_int(question):
    """Sub menu for getting and checking user input integers."""
    while True:
        try:
            val = int(input(question))
            break
        except ValueError:
            print(f"{bcolors.FAIL}input error, please try again{bcolors.ENDC}")
            continue
        except Exception as e:
            print(e)
            continue 
    return val


def get_rating():
    """Sub menu for getting and checking a user input string."""
    question = "Enter film rating (PG, G, or R): "
    # Parental Guidance, General, Restricted
    the_rating = ""
    while True:
        try:
            user_input = input(question)
            text_check = user_input.lower()
            match text_check:
                case "pg":
                    the_rating = "PG"
                    break
                case "g":
                    the_rating = "G"
                    break
                case "r": 
                    the_rating = "R"
                    break
                case _:
                    print(f"{bcolors.FAIL}input error, please try again{bcolors.ENDC}")
                    continue
        except Exception as e:
            print(e)
            continue 
    return the_rating

def get_genre():
    """Sub menu for getting and checking a user input string."""
    question = "Enter film genre: Comedy, Action, Animation, Fantasy, Crime: "
    the_genre = ""
    while True:
        try:
            user_input = input(question)
            text_check = user_input.lower()
            if "com" in text_check:
                the_genre = "Comedy"
                break
            elif "act" in text_check:
                the_genre = "Action"
                break
            elif "ani" in text_check:
                the_genre = "Animation"
                break
            elif "fan" in text_check:
                the_genre = "Fantasy"
                break
            elif "cri" in text_check:
                the_genre = "Crime"
                break
            else:
                print(f"{bcolors.FAIL}input error, please try again{bcolors.ENDC}")
                continue
        except Exception as e:
            print(e)
            continue 
    return the_genre

def get_title():
    """Sub menu for getting and checking a user input string."""
    question = "Enter film title: "
    while True:
        try:
            text = input(question)
            break
        except Exception as e:
            print(e)
            continue 
    return text


