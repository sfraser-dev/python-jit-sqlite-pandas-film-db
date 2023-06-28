import pandas as pd
from tabulate import tabulate
from colors import *

def table_print_to_terminal(conn, query, query_to_read_db="use-query-argument"):
    """Performs a SQL query then writes the resultant view to the terminal.
       Uses pandas to format the tables."""

    # Default is to use the query passed as argument, but can just opt for
    # fixed query to print the entire table.
    if query_to_read_db == "use-query-argument": 
        dql_query = pd.read_sql(query, conn)
    elif query_to_read_db == "just-select-all":
        dql_query = pd.read_sql("""SELECT * FROM films""", conn)
    else: 
        print("error: 'query_to_use' unknown")
    df = pd.DataFrame(dql_query)

    # Retro style: DataFrame to retro style (via to_markdown(), row index count removed. 
    print(df.to_markdown(index=0)) 