from colors import *

##### Get integer user inputs.
def get_input_int(question):
    """ Generic try/except for getting and checking user input integers."""
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

def get_id():
    question = "Enter id of film to be deleted: "
    return get_input_int(question)

def get_year():
    question = "Enter film release year: "
    return get_input_int(question)

def get_duration():
    question = "Enter film duration (mins): "
    return get_input_int(question)

##### Get string user inputs.
def get_input_string(question):
    """ Generic try/except for getting and checking user input strings."""
    while True:
        try:
            text = input(question)
            break
        except Exception as e:
            print(e)
            continue 
    return text

def get_title():
    question = "Enter film title: "
    return get_input_string(question)

def get_rating():
    # Parental Guidance, General, Restricted
    wanted_text = ["pg", "g", "r"]
    question = "Enter film rating ('PG', 'G', or 'R'): "
    while True:
        the_rating = get_input_string(question).lower()
        if the_rating in wanted_text:
            return the_rating.upper()
        else:
            print(f"{bcolors.FAIL}please select from 'PG', 'G' or 'R'{bcolors.ENDC}")

def get_genre():
    wanted_text = ["comedy", "action", "animation", "fantasy", "crime"]
    question = "Enter film genre ('Comedy', 'Action', 'Animation', 'Fantasy' or 'Crime'): "
    while True:
        the_genre = get_input_string(question).lower()
        # Enough to just match the first three letters of the word.
        for wt in wanted_text:
            if wt[:3] == the_genre[0:3]: 
                return wt.lower().title()
        else:
            print(f"{bcolors.FAIL}please select from 'Comedy', 'Action', 'Animation', 'Fantasy' or 'Crime'{bcolors.ENDC}")