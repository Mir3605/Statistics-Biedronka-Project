import sqlite3
import pandas as pd
import os


def execute_all_in(path : str):
    file_names = os.listdir(path)
    files_to_exec = []
    for name in file_names:
        with open(f'{path}/{name}') as file:
            sql_script = file.read()
        files_to_exec.append(sql_script)
    db = sqlite3.connect("Database/shops.db")
    cursor = db.cursor()
    for sql_script in files_to_exec:
        cursor.executescript(sql_script)
    db.commit()
    db.close()


def create_tables():
    execute_all_in('Database/Tables')


def create_views():
    execute_all_in('Database/Views')


def insert_communities_values():
    communities = pd.read_csv("Clear_data/Communities/all_data.csv", encoding='utf8', delimiter=';')
    db = sqlite3.connect("Database/shops.db")
    communities.to_sql('gminy', db, if_exists='append', index=False)
    db.commit()
    db.close()


def insert_shop_values():
    opening_hours = pd.read_csv("Clear_data/Shops/all_opening_hours.csv", encoding='utf8', delimiter=';')
    shops_data = pd.read_csv("Clear_data/Shops/all_shops.csv", encoding='utf8', delimiter=';')
    db = sqlite3.connect("Database/shops.db")
    opening_hours.to_sql('godziny_otwarcia', db, if_exists='append', index=False)
    shops_data.to_sql('sklepy', db, if_exists='append', index=False)
    db.commit()
    db.close()


def drop_tables():
    db = sqlite3.connect("Database/shops.db")
    cursor = db.cursor()
    cursor.execute('''
        DROP TABLE gminy
    ''')
    cursor.execute('''
        DROP TABLE sklepy
    ''')
    cursor.execute('''
    DROP TABLE godziny_otwarcia
    ''')
    db.commit()
    db.close()


def drop_views():
    db = sqlite3.connect("Database/shops.db")
    cursor = db.cursor()
    cursor.execute('''
            DROP VIEW liczba_sklepow
        ''')
    cursor.execute('''
            DROP VIEW sklepy_detale
        ''')
    db.commit()
    db.close()


def recreate_base():
    drop_tables()
    create_tables()
    create_views()
    insert_communities_values()
    insert_shop_values()
