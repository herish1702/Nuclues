import psycopg2

def connect_and_run_query(query):
    try:
        conn = psycopg2.connect(
            host="gj-postgresdev.postgres.database.azure.com",
            user="gjpgadmin",
            password="GjAdmin@247",
            dbname="nucleus247_dev",
            port=5432,
            sslmode="require"
        )
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchone()  
        cur.close()
        conn.close()
        return result[0] if result else None
    
    except psycopg2.Error as e:
        return f"Database connection error: {str(e)}"