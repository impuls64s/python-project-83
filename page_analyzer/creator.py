import psycopg2
import os
from dotenv import load_dotenv
import datetime


load_dotenv()
date_time = datetime.date.today()
DATABASE_URL = os.getenv("DATABASE_URL")
conn = psycopg2.connect(DATABASE_URL)
conn.autocommit = True


def add_to_database(url):
    with conn.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO urls (name, created_at)
                VALUES ('{url}', '{date_time}');
            """
        )
        cursor.execute(f"SELECT * FROM urls WHERE name = '{url}';")
        new_url = cursor.fetchone()
        return new_url 
    conn.close()


def data_url(id):
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT * FROM urls WHERE id = {id};")
        all_urls = cursor.fetchone()
        return all_urls
    conn.close()


def data_all():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM urls;")
        all_data = cursor.fetchall()
        return all_data
    conn.close()


def check_in_db(name):
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT * FROM urls WHERE name = '{name}';")
        name_data = cursor.fetchone()
        return name_data
    conn.close()

#print(check_in_db('http://mail.ru'))