import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="postgres",
        user="postgres",
        password="admin"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT NOW();")
    current_time = cursor.fetchone()
    print("Current time in DB:", current_time)

except psycopg2.Error as e:
    print("Database error:", e)

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()

#Current time in DB: (datetime.datetime(2025, 6, 3, 20, 1, 50, 360059, tzinfo=datetime.timezone(datetime.timedelta(seconds=18000))),)