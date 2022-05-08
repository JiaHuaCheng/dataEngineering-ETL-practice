# Data Engineering Project - Data Modeling with Postgres

In this project, we practice how to perform the ETL process. 
We divide our whole process into the following parts.
 
1. Use python script to connect Postgres DB then create tables.
2. Perform ETL process to JSON raw data, and insert data into tables.
3. Run test.ipynb to check the correctness of the data we insert.

## Usage

Execute the following command in the command line in order.

```python
# run the following code in the command line.
~ % python create_tables.py # create table in Postgres DB
~ % python etl.py # read JSON and perform ETL process
```


## File Descriptions

This repository shoud have 7 files and 1 folder.

* Folder
1. ./data; A directory where we store our JSON files. 

* File
1. "create_tables.py"; A python script for creating Postgres tables.
2. "etl.ipynb"; A notebook for implementing and testing ETL script. 
3. "etl.py"; A formal ETL process script for our data.
4. "sql_queries.py"; A python script using SQL to create tables and to insert data.
5. "test.ipynb"; A notebook for the data correctness testing.
6. "README.MD"; Description File including usage and summary.