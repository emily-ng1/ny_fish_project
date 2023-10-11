from flask import current_app, g
import psycopg2
from settings import DB_NAME, DB_USER, DB_PASSWORD, TEST_DB_NAME, TEST_DB_USER, TEST_DB_PASSWORD #Way1
import settings #Way2

test_conn = psycopg2.connect(dbname = settings.TEST_DB_NAME, user = settings.TEST_DB_USER, password=settings.TEST_DB_PASSWORD)
test_cursor=test_conn.cursor()

conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER, password=DB_PASSWORD, host="localhost", port=5432)
cursor=conn.cursor()

class DataEmptyError(Exception):
    pass


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
    #query = f"""INSERT INTO "{obj.__table__}" ({keys(obj)}) VALUES ({s_str}) ON CONFLICT ON CONSTRAINT {obj.__constraint__} DO NOTHING;"""

    #query=f"""SELECT datname FROM pg_database;"""
    #cursor.execute(query)
    #print(cursor.fetchall())

    #query =f"""SELECT * FROM public.{obj.__table__} LIMIT 10;"""

    # query=f'''SELECT *
    # FROM pg_catalog.pg_tables
    # WHERE schemaname != 'pg_catalog' AND
    # schemaname != 'information_schema';'''

    #query='SELECT current_database();' #[('emilyng',)]

    query='SELECT * FROM employees;'
    cursor.execute(query)
    print(cursor.fetchall())

    #cursor.execute(query, list(values(obj)))
    #conn.commit()

    # cursor.execute(f'SELECT * FROM {obj.__table__} ORDER BY id DESC LIMIT 1')
    # record = cursor.fetchone()
    # return build_from_record(type(obj), record)



def save_model_dates(conn, insert_Class, from_Class):
    statement=f'''
    INSERT INTO {insert_Class.__table__}(month, year)
    WITH distinct_month AS(
    SELECT DISTINCT month, year
    FROM {from_Class.__table__}
    )
    
    SELECT month, year
    FROM distinct_month
    ORDER BY
    (CASE
        WHEN month='January' THEN 1
        WHEN month='February' THEN 2
        WHEN month='March' THEN 3
        WHEN month='April' THEN 4
        WHEN month='May' THEN 5
        WHEN month='June' THEN 6
        WHEN month='July' THEN 7
        WHEN month='August' THEN 8
        WHEN month='September' THEN 9
        WHEN month='October' THEN 10
        WHEN month='November' THEN 11
        WHEN month='December' THEN 12
        ELSE 99 END), year
    ON CONFLICT ON CONSTRAINT {insert_Class.__constraint__} DO NOTHING;
    '''
    cursor=conn.cursor()
    cursor.execute(statement)
    conn.commit()

def save_model_waterbodies(conn, insert_Class, from_Class):
    statement=f'''
    INSERT INTO {insert_Class.__table__}(waterbody_name, waterbody_class, description, basin_name, water_quality_class)
    SELECT DISTINCT a.waterbody, b.waterbody_class, b.description, b.basin, b.water_quality_class
    FROM {from_Class.__table__} a
    INNER JOIN ny_water_qualities b ON a.waterbody = b.name
    ON CONFLICT ON CONSTRAINT {insert_Class.__constraint__} DO NOTHING;    
    '''
    cursor=conn.cursor()
    cursor.execute(statement)
    conn.commit()

def save_model_fishes(conn, insert_Class, from_Class_one, from_Class_two):
    statement=f'''
    INSERT INTO {insert_Class.__table__}(waterbody_id, date_id, species_name, size_inches, number)
    SELECT c.id, b.id, a.species, a.size_inches, a.number
    FROM ny_fishes a
    INNER JOIN {from_Class_one.__table__} b ON a.month=b.month AND a.year=b.year
    INNER JOIN {from_Class_two.__table__} c ON a.waterbody=c.waterbody_name
    ORDER BY c.id, b.id, a.species, a.size_inches, a.number
    ON CONFLICT ON CONSTRAINT {insert_Class.__constraint__} DO NOTHING;
    '''
    cursor=conn.cursor()
    cursor.execute(statement)
    conn.commit()