from distutils.util import execute
import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *

def main():
    """
    - Connect to db and check data quality
        1. entry numbers test
        2. primary keys test
        3. types test
        4. upsertion test 
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=admin password=admin")
    cur = conn.cursor()
    
    table_list = ['users', 'artists', 'songplays', 'songs', 'time']
    for table_name in table_list:
        entry_numbers_test()
        primary_keys_test()
        types_test()
        upsertion_test()
    conn.close()

if __name__ == "__main__":
    main()