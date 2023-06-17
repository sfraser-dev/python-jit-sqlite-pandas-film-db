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
    question = f"{bcolors.WARNING}\nEnter id of film: {bcolors.ENDC}"
    return get_input_int(question)

def get_year():
    question = f"{bcolors.WARNING}\nEnter film release year: {bcolors.ENDC}"
    return get_input_int(question)

def get_duration():
    question = f"{bcolors.WARNING}\nEnter film duration (mins): {bcolors.ENDC}"
    return get_input_int(question)

def get_field():
    wanted_text = ["title", "year", "rating", "duration", "genre"]
    question = f"""{bcolors.WARNING}\nSelect field:
1. Title
2. Year
3. Rating
4. Duration
5. Genre
{bcolors.ENDC}"""
    while True:
        val = get_input_int(question)
        if val in [1, 2, 3, 4, 5]:
            return wanted_text[val-1]
        else:
            print(f"{bcolors.FAIL}please select either 1, 2, 3, 4 or 5{bcolors.ENDC}")

def get_rating():
    # Parental Guidance, General, Restricted
    wanted_text = ["PG", "G", "R"]
    question = f"""{bcolors.WARNING}\nEnter film rating:
1. PG
2. G
3. R
{bcolors.ENDC}"""
    while True:
        val = get_input_int(question)
        if val in [1, 2, 3]:
            return wanted_text[val-1]
        else:
            print(f"{bcolors.FAIL}please select from 'PG', 'G' or 'R'{bcolors.ENDC}")

def get_genre():
    wanted_text = ["Comedy", "Action", "Animation", "Fantasy", "Crime"]
    question = f"""{bcolors.WARNING}\nEnter film genre:
1. Comedy
2. Action
3. Animation
4. Fantasy
5. Crime
{bcolors.ENDC}"""
    while True:
        val = get_input_int(question)
        if val in [1, 2, 3, 4, 5]:
            return wanted_text[val-1]
        else:
            print(f"{bcolors.FAIL}please select from 'Comedy', 'Action', 'Animation', 'Fantasy' or 'Crime'{bcolors.ENDC}")

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
    question = f"{bcolors.WARNING}\nEnter film title: {bcolors.ENDC}"
    return get_input_string(question)