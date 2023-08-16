from flask import current_app, g
import psycopg2
from settings import DB_NAME, DB_USER, DB_PASSWORD, TEST_DB_NAME, TEST_DB_USER, TEST_DB_PASSWORD #Way1
import settings #Way2

test_conn = psycopg2.connect(dbname = settings.TEST_DB_NAME, user = settings.TEST_DB_USER, password=settings.TEST_DB_PASSWORD)
test_cursor=test_conn.cursor()

conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER, password=DB_PASSWORD)
cursor=conn.cursor()

#Build db
def get_db():
    if "db" not in g:
        g.db = psycopg2.connect(dbname = current_app.config['DB_NAME'],
                                user = current_app.config['DB_USER'], 
                                password = current_app.config['DB_PASSWORD']) 
    return g.db


#Build instances from records
def build_from_record(Class, record):
    if not record: return None

    obj=Class()
    attr=dict(zip(Class.columns, record))
    obj.__dict__=attr
    return obj

def build_from_records(Class, records):
    return [build_from_record(Class, record) for record in records]


#Build find and find all
def find(Class, id, conn):
    statement=f"SELECT * FROM {Class.__table__} WHERE id=%s;"
    cursor=conn.cursor()
    cursor.execute(statement, (id,))
    record=cursor.fetchone()
    return build_from_record(Class, record)

def find_all(Class, conn):
    statement=f"SELECT * FROM {Class.__table__};"
    cursor=conn.cursor()
    cursor.execute(statement)
    records=cursor.fetchall()
    return build_from_records(Class, records)


#Build drop tables
def drop_records(cursor, conn, table_name):
    cursor.execute(f"DELETE FROM {table_name};")
    conn.commit()

def drop_tables(table_names, conn, cursor):
    for table_name in table_names:
        drop_records(cursor, conn, table_name)

def drop_all_tables(conn, cursor):
    table_names=["ny_fishes", "ny_water_qualities"]
    drop_tables(table_names, conn, cursor)


#Build save
def keys(obj):
    venue_attrs = obj.__dict__
    selected = [attr for attr in obj.columns if attr in venue_attrs.keys()]
    return ', '.join(selected)

def values(obj):
    venue_attrs = obj.__dict__
    return [venue_attrs[attr] for attr in obj.columns if attr in venue_attrs.keys()]

def save(obj, conn, cursor):
    s_str = ', '.join(len(values(obj)) * ['%s'])
    venue_str = f"""INSERT INTO {obj.__table__} ({keys(obj)}) VALUES ({s_str});"""
    cursor.execute(venue_str, list(values(obj)))
    conn.commit()
    
    cursor.execute(f'SELECT * FROM {obj.__table__} ORDER BY id DESC LIMIT 1')
    record = cursor.fetchone()
    return build_from_record(type(obj), record)