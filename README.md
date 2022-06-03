# Data Engineering Project - Data Modeling with Postgres

In this project, we practice how to perform the ETL process. 
We divide our whole process into the following parts.
 
1. Use python script to connect Postgres DB then create tables.
2. Perform ETL process to JSON raw data, and insert data into tables.
3. Run data_quality.py to check the correctness of the data we insert. (working on it)

## Usage

Execute the following command in the command line in order.

```python
# run the following code in the command line.
~ % python create_tables.py # create table in Postgres DB
~ % python etl.py # read JSON and perform ETL process
~ % python data_quality.py # ensure data quality (working on it)
```


## File Descriptions

This repository shoud have 7 files and 1 folder.

* Folder
1. ./data: A directory where we store our JSON files. 
2. ./backups: where we store jupyter notebook drafts.

* File
1. create_tables.py: A python script for creating Postgres tables.
2. etl.py: A formal ETL process script for our data.
3. data_quality.py: A python script contains entry_check, pk_check, type_check, upsertion_check. (working on it)
4. sql_queries.py: A python script using SQL to create tables and to insert data.
5. README.MD: Description File including usage and summary.