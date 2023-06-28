from colors import *

##### Get integer user inputs.
def get_input_int(question, option):
    """ Generic try/except for getting and checking user input integers."""
    while True:
        try:
            val = int(input(question))
            break
        except ValueError:
            match option:
                case "id":
                    print(f"{bcolors.FAIL}input type error, please input a valid id{bcolors.ENDC}")
                case "year":
                    print(f"{bcolors.FAIL}input type error, please input a valid year{bcolors.ENDC}")
                case "duration":
                    print(f"{bcolors.FAIL}input type error, please input a valid duration{bcolors.ENDC}")
                case "list":
                    print(f"{bcolors.FAIL}input type error, please input a number from the shown list{bcolors.ENDC}")
                case _:
                    print(f"{bcolors.FAIL}input type error in get_input_int(), unknown option{bcolors.ENDC}")
            continue
        except Exception as e:
            print(e)
            continue 
    return val

def get_id():
    question = f"{bcolors.WARNING}\nEnter film id: {bcolors.ENDC}"
    return get_input_int(question, "id")

def get_year():
    question = f"{bcolors.WARNING}\nEnter film release year: {bcolors.ENDC}"
    return get_input_int(question, "year")

def get_duration():
    question = f"{bcolors.WARNING}\nEnter film duration (mins): {bcolors.ENDC}"
    return get_input_int(question, "duration")

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
        val = get_input_int(question, "list")
        if val in [1, 2, 3, 4, 5]:
            return wanted_text[val-1]
        else:
            print(f"{bcolors.FAIL}input range error, please input a number from the shown list{bcolors.ENDC}")

def get_rating():
    # Parental Guidance, General, Restricted
    wanted_text = ["PG", "G", "R"]
    question = f"""{bcolors.WARNING}\nEnter film rating:
1. PG
2. G
3. R
{bcolors.ENDC}"""
    while True:
        val = get_input_int(question, "list")
        if val in [1, 2, 3]:
            return wanted_text[val-1]
        else:
            print(f"{bcolors.FAIL}input range error, please input a number from the shown list{bcolors.ENDC}")

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
        val = get_input_int(question, "list")
        if val in [1, 2, 3, 4, 5]:
            return wanted_text[val-1]
        else:
            print(f"{bcolors.FAIL}input range error, please input a number from the shown list{bcolors.ENDC}")

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