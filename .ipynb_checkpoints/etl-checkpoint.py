import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    Extract json columns from ./data/song_data folder and insert into songs table, and artists table.
    
            Parameters:
                    cur: an object allows python to execute Postgres command.
                    filepath: indicates where we store our source data.
            Returns: 
                    None
    """
    
    df = pd.read_json(filepath, lines=True)

    artist_data = df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']].values[0]
    artist_data = artist_data.tolist() 
    cur.execute(artist_table_insert, artist_data)
    
    song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']].values[0]
    song_data = song_data.tolist()
    cur.execute(song_table_insert, song_data)
    


def process_log_file(cur, filepath):
    """
    Extract json columns from ./data/log_data folder and insert into time table, songplays, and users table.
    
            Parameters:
                    cur: an object allows python to execute Postgres command.
                    filepath: indicates where we store our source data.
            Returns: 
                    None
    """

    df = pd.read_json(filepath, lines=True)
    df = df[df['page'] == 'NextSong']
    df['ts'] = pd.to_datetime(df['ts'], unit='ms')
    
    t = pd.to_datetime(df['ts'], unit='ms')
    time_data = (t, t.dt.hour, t.dt.day, t.dt.week, t.dt.month, t.dt.year , t.dt.weekday)
    column_labels = ['start_time', 'hour', 'day', 'week_of_year', 'month', 'year', 'weekday']

    time_df = pd.DataFrame(dict(zip(column_labels, time_data)))
    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))


    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    
    for index, row in df.iterrows():
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        songplay_data = (row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    1. Parse filepath to get absolute path for each file. 
    2. Pass to the process_func which extracts data from input json file and insert into table.
    
            Parameters:
                    cur: an object which allows python to execute Postgres command.
                    conn: an object of database
                    filepath: indicates where we store our source data.
                    func: reference to the process_song_file/process_log_file function
            Returns: 
                    None
    """    

    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """
    
    This program is for parsing json files to insert data into database. 
    
    """    
    
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()