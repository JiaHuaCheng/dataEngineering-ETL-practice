# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""

    CREATE TABLE IF NOT EXISTS songplays 
    
    (   songplay_id   SERIAL    PRIMARY KEY,
        start_time    TIMESTAMP NOT NULL     REFERENCES time(start_time),
        userId        INT       NOT NULL     REFERENCES users(userId),
        level         TEXT,
        song_id       TEXT      REFERENCES songs(song_id),
        artist_id     TEXT      REFERENCES artists(artist_id),
        sessionId     INT,
        location      TEXT,
        userAgent     TEXT
    );
        
""")

user_table_create = ("""

    CREATE TABLE IF NOT EXISTS users (
        userId        INT       PRIMARY KEY,
        firstName     TEXT      NOT NULL,
        lastName      TEXT      NOT NULL,
        gender        TEXT,
        level         TEXT)
        
""")

song_table_create = ("""

    CREATE TABLE IF NOT EXISTS songs (
        song_id       TEXT      PRIMARY KEY,
        title         TEXT      NOT NULL,
        artist_id     TEXT      NOT NULL      REFERENCES artists(artist_id),
        year          INT,
        duration      NUMERIC   NOT NULL)
        
""")

artist_table_create = ("""

    CREATE TABLE IF NOT EXISTS artists (
        artist_id        TEXT      PRIMARY KEY,
        artist_name      TEXT      NOT NULL,
        artist_location  TEXT,
        artist_latitude  DOUBLE PRECISION,
        artist_longitude DOUBLE PRECISION)
        
""")

time_table_create = ("""

    CREATE TABLE IF NOT EXISTS time (
        start_time      timestamp  PRIMARY KEY,
        hour            SMALLINT,
        day             SMALLINT,
        week_of_year    SMALLINT,
        month           SMALLINT,
        year            SMALLINT,
        weekday         SMALLINT)
        
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (start_time, userId, level, song_id, artist_id, sessionId, location, userAgent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

user_table_insert = ("""
    INSERT INTO users (userId, firstName, lastName, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (userId) DO UPDATE SET level=EXCLUDED.level
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")  

artist_table_insert = ("""
    INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude, artist_longitude)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

time_table_insert = ("""
    INSERT INTO time (start_time, hour, day, week_of_year, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("""
    SELECT songs.song_id, artists.artist_id 
    FROM songs JOIN artists ON
    songs.artist_id = artists.artist_id
    WHERE songs.title = %s AND artists.artist_name = %s AND songs.duration = %s
""")


# QUERY LISTS

#create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]

create_table_queries = [user_table_create, artist_table_create, time_table_create, song_table_create, songplay_table_create]

drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]