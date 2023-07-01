import psycopg2

def create_conn():
    conn = None
    try:
        conn = psycopg2.connect(
            database="your_database",
            user="your_username",
            password="your_password",
            host="127.0.0.1",
            port="5432"
        )
        print("Database connected successfully")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn

def close_conn(conn):
    if conn is not None:
        conn.close()
        print("Database connection closed.")