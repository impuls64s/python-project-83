import psycopg2
import os
from dotenv import load_dotenv
import datetime


load_dotenv()
# datetime.date.today() - если не нужно время
date_time = datetime.datetime.now()
DATABASE_URL = os.getenv("DATABASE_URL")


def add_to_database(url):
    conn = psycopg2.connect(DATABASE_URL)
    conn.autocommit = True
    with conn.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO urls (name, created_at)
                VALUES ('{url}', '{date_time}');
            """
        )
        cursor.execute(f"INSERT INTO all_site (urls_name) VALUES ('{url}');")
        cursor.execute(f"SELECT * FROM urls WHERE name = '{url}';")
        new_url = cursor.fetchone()
        conn.close()
        return new_url


def data_url(id):
    conn = psycopg2.connect(DATABASE_URL)
    conn.autocommit = True
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT * FROM urls WHERE id = {id};")
        all_urls = cursor.fetchone()
        conn.close()
    return all_urls


def check_in_db(name):
    conn = psycopg2.connect(DATABASE_URL)
    conn.autocommit = True
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT * FROM urls WHERE name = '{name}';")
        name_data = cursor.fetchone()
        conn.close()
        return name_data


def add_to_url_checks(id, dict_data):
    date_time = datetime.datetime.now()
    conn = psycopg2.connect(DATABASE_URL)
    conn.autocommit = True
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO url_checks"
            "(url_id, created_at, status_code, h1, title, description)"
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (id, date_time, 200, dict_data.get('h1', ''),
             dict_data.get("title", ''), dict_data.get("description", '')))
        cursor.execute(
            f"""UPDATE all_site SET
            last_check = '{date_time}',
            status_code = '200'
            WHERE id = '{id}';"""
        )
    conn.close()


def data_all_url_checks(id):
    conn = psycopg2.connect(DATABASE_URL)
    conn.autocommit = True
    with conn.cursor() as cursor:
        cursor.execute(
            f"SELECT * FROM url_checks WHERE url_id = '{id}' ORDER BY id DESC;"
        )
        data_ckecks = cursor.fetchall()
        conn.close()
        return data_ckecks


def data_all_all_site():
    conn = psycopg2.connect(DATABASE_URL)
    conn.autocommit = True
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM all_site ORDER BY id DESC;")
        data_all_all_site = cursor.fetchall()
        conn.close()
        return data_all_all_site
