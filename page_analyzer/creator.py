import psycopg2
import os
from dotenv import load_dotenv
import datetime


load_dotenv()
date_time = datetime.datetime.now()#datetime.date.today()
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
        cursor.execute(f"INSERT INTO all_site (urls_name) VALUES ('{url}');")
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
        cursor.execute("SELECT * FROM urls ORDER BY id DESC;")
        all_data = cursor.fetchall()
        return all_data
    conn.close()


def check_in_db(name):
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT * FROM urls WHERE name = '{name}';")
        name_data = cursor.fetchone()
        return name_data
    conn.close()


def add_to_url_checks(id, dict_data):
    date_time = datetime.datetime.now()
    with conn.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO url_checks 
            (url_id, created_at, status_code, h1, title, description)
            VALUES ('{id}', '{date_time}', 200, '{dict_data.get('h1', ' ')}', '{dict_data.get("title", ' ')}', '{dict_data.get("description", ' ')}');
            """
        )
        cursor.execute(
            f"""UPDATE all_site SET
            last_check = '{date_time}',
            status_code = '200'
            WHERE id = '{id}';"""
        )
    #conn.close()


def data_all_url_checks(id):
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT * FROM url_checks WHERE url_id = '{id}' ORDER BY id DESC;")
        data_ckecks = cursor.fetchall()
        return data_ckecks
    conn.close()


def data_all_all_site():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM all_site ORDER BY id DESC;")
        data_all_all_site = cursor.fetchall()
        return data_all_all_site
    conn.close()
