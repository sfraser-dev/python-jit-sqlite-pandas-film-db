import pandas as pd

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def table_print_to_terminal(conn, description, query, query_to_read_db="use-query-argument"):
    """Performs a SQL query then writes the resultant view to the terminal.
       Uses pandas to format the tables."""

    print(f"\n{bcolors.OKGREEN}{description}{bcolors.ENDC}{bcolors.WARNING}{query}{bcolors.ENDC}\n")

    if query_to_read_db == "use-query-argument": 
        dql_query = pd.read_sql(query, conn)
    elif query_to_read_db == "just-select-all":
        dql_query = pd.read_sql("""SELECT * FROM films""", conn)
    else: 
        print("error: 'query_to_use' unknown")
    df = pd.DataFrame(dql_query)

    # Retro style: DataFrame to retro style (via to_markdown(), row index count removed. 
    print(df.to_markdown(index=0)) 

    # input(f"\n{bcolors.FAIL}Press Enter to continue...{bcolors.ENDC}\n")