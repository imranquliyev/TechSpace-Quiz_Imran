import requests
import pymysql
from datetime import datetime

MOVIE = input("Enter the name of the film: ")

API_KEY = "5d9df2b8"
url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={MOVIE}"

# Database connection
connection = pymysql.connect(   
    host='127.0.0.1',
    user='root',
    password='12345',
    db='movies_db',
    port=3306,
    charset='utf8mb4', 
    cursorclass=pymysql.cursors.DictCursor
)

def fetch_movie_data(movie_title):
    response = requests.get(f"http://www.omdbapi.com/?apikey={API_KEY}&t={movie_title}")
    if response.status_code == 200:
        data = response.json()
        if data['Response'] == 'True':
            # Extract relevant data
            title = data.get('Title')
            released = data.get('Released')
            genre = data.get('Genre')
            director = data.get('Director')
            return (title, released, genre, director)
        else:
            print(f"Movie not found: {data.get('Error')}")
            return None
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

def store_movie_data(movie_info):
    if not movie_info:
        print("No movie data to store.")
        return
    try:
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO Movie_info (title, released, genre, director)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, movie_info)
            connection.commit()
            print("Movie data inserted successfully.")
    except pymysql.MySQLError as e:
        print(f"Error occurred: {e}")
    finally:
        connection.close()

# Fetch and store movie data
movie_info = fetch_movie_data(MOVIE)
store_movie_data(movie_info)
